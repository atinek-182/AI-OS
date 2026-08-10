import os
import sys
import json
import re
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RAW_DIR = r"d:\AI-OS\scratch\awwwards_ingestion_raw\awwwards_blog"
ASSETS_DIR = os.path.join(RAW_DIR, "assets")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def crawl_awwwards_case_studies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        all_case_studies = []
        
        # Crawl pages 1 to 5
        for page_num in range(1, 6):
            url = f"https://www.awwwards.com/blog/case-study/?page={page_num}" if page_num > 1 else "https://www.awwwards.com/blog/case-study/"
            print(f"\n[PAGE {page_num}] Navigating to {url}")
            
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(3000)
                
                # Extract cards specifically targeting .card-blog__title a and a[href$=".html"]
                items = page.evaluate('''() => {
                    let results = [];
                    let links = document.querySelectorAll('.card-blog__title a, a[href$=".html"]');
                    links.forEach(a => {
                        let href = a.href;
                        let title = a.innerText.trim();
                        if (href && href.endsWith('.html') && title.length > 3) {
                            if (!results.some(r => r.href === href)) {
                                results.push({ title: title, href: href });
                            }
                        }
                    });
                    return results;
                }''')
                
                print(f"[PAGE {page_num}] Found {len(items)} case study links.")
                for item in items:
                    if not any(cs['href'] == item['href'] for cs in all_case_studies):
                        all_case_studies.append(item)
                        
            except Exception as e:
                print(f"[ERROR] Crawling page {page_num}: {e}")
                
        print(f"\n[TOTAL CASE STUDIES DISCOVERED] Found {len(all_case_studies)} unique case studies.")
        
        index_file = os.path.join(RAW_DIR, "all_awwwards_case_studies.json")
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(all_case_studies, f, indent=2)
            
        # Fetch up to 10 case studies in Batch 1 for high-quality synthesis
        fetched_count = 0
        for cs in all_case_studies:
            print(f"\n[FETCHING {fetched_count+1}/{len(all_case_studies)}] {cs['title']} -> {cs['href']}")
            try:
                page.goto(cs['href'], wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(3000)
                
                content = page.evaluate('''() => {
                    let main = document.querySelector('article') || document.querySelector('.post-single') || document.querySelector('.wrapper-detail') || document.body;
                    let blocks = [];
                    let codeSnippets = [];
                    let images = [];
                    
                    let elements = main.querySelectorAll('h1, h2, h3, h4, p, pre, code, blockquote, img');
                    elements.forEach(el => {
                        let tag = el.tagName.toLowerCase();
                        if (tag === 'h1') blocks.push('# ' + el.innerText.trim());
                        else if (tag === 'h2') blocks.push('\\n## ' + el.innerText.trim());
                        else if (tag === 'h3') blocks.push('\\n### ' + el.innerText.trim());
                        else if (tag === 'h4') blocks.push('\\n#### ' + el.innerText.trim());
                        else if (tag === 'p') {
                            let txt = el.innerText.trim();
                            if (txt.length > 5) blocks.push(txt);
                        }
                        else if (tag === 'blockquote') blocks.push('> ' + el.innerText.trim());
                        else if (tag === 'pre' || tag === 'code') {
                            let codeTxt = el.innerText.trim();
                            blocks.push('\\n```\\n' + codeTxt + '\\n```\\n');
                            codeSnippets.push(codeTxt);
                        }
                        else if (tag === 'img') {
                            let src = el.src || el.getAttribute('data-src');
                            if (src && !src.startsWith('data:')) images.push(src);
                        }
                    });
                    
                    return {
                        markdown: blocks.join('\\n\\n'),
                        codeSnippets: codeSnippets,
                        images: images
                    };
                }''')
                
                slug = re.sub(r'[^a-z0-9]+', '_', cs['title'].lower()).strip('_')[:60]
                out_path = os.path.join(RAW_DIR, f"{slug}.md")
                
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(f"# {cs['title']}\n")
                    f.write(f"Source: {cs['href']}\n\n")
                    f.write(content['markdown'])
                    
                print(f"[SUCCESS] Saved raw case study to {out_path} ({len(content['markdown'])} chars)")
                fetched_count += 1
                
                if fetched_count >= 10:
                    print("\n[BATCH 1 COMPLETE] Extracted 10 case study markdowns for human review gate.")
                    break
                    
            except Exception as e:
                print(f"[ERROR] Fetching {cs['href']}: {e}")
                
        browser.close()

if __name__ == "__main__":
    crawl_awwwards_case_studies()
