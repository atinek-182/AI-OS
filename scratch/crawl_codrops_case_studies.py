import os
import sys
import json
import re
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RAW_DIR = r"d:\AI-OS\scratch\awwwards_ingestion_raw\codrops"
ASSETS_DIR = os.path.join(RAW_DIR, "assets")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def crawl_codrops():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        all_codrops = []
        
        # Crawl pages 1 to 5
        for page_num in range(1, 6):
            url = f"https://tympanus.net/codrops/tag/case-study/page/{page_num}/" if page_num > 1 else "https://tympanus.net/codrops/tag/case-study/"
            print(f"\n[CODROPS PAGE {page_num}] Navigating to {url}")
            
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(3000)
                
                # Extract links matching date pattern
                items = page.evaluate('''() => {
                    let results = [];
                    let links = document.querySelectorAll('a[href*="/codrops/20"]');
                    links.forEach(a => {
                        let href = a.href;
                        let title = a.innerText.trim();
                        // Match URL pattern: /codrops/YYYY/MM/DD/slug/
                        if (href && /\\/codrops\\/20\\d{2}\\/\\d{2}\\/\\d{2}\\//.test(href) && title.length > 5) {
                            if (!results.some(r => r.href === href)) {
                                results.push({ title: title, href: href });
                            }
                        }
                    });
                    return results;
                }''')
                
                print(f"[CODROPS PAGE {page_num}] Discovered {len(items)} articles.")
                for item in items:
                    if not any(c['href'] == item['href'] for c in all_codrops):
                        all_codrops.append(item)
                        
            except Exception as e:
                print(f"[ERROR] Crawling Codrops page {page_num}: {e}")
                
        print(f"\n[TOTAL CODROPS ARTICLES] Found {len(all_codrops)} unique case studies.")
        
        index_file = os.path.join(RAW_DIR, "all_codrops_case_studies.json")
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(all_codrops, f, indent=2)
            
        # Fetch up to 10 articles for Batch 1
        fetched_count = 0
        for cs in all_codrops:
            print(f"\n[FETCHING CODROPS {fetched_count+1}/{len(all_codrops)}] {cs['title']} -> {cs['href']}")
            try:
                page.goto(cs['href'], wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(3000)
                
                content = page.evaluate('''() => {
                    let main = document.querySelector('article') || document.querySelector('.ct-post') || document.body;
                    let blocks = [];
                    let codeSnippets = [];
                    let demoLinks = [];
                    
                    let elements = main.querySelectorAll('h1, h2, h3, h4, p, pre, code, blockquote, a');
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
                        else if (tag === 'a') {
                            let href = el.href;
                            if (href && (href.includes('github.com') || href.includes('codepen.io') || href.includes('tympanus.net/Development/') || href.includes('tympanus.net/Tutorials/'))) {
                                demoLinks.push({ text: el.innerText.trim() || 'Demo/Repo', href: href });
                            }
                        }
                    });
                    
                    return {
                        markdown: blocks.join('\\n\\n'),
                        codeSnippets: codeSnippets,
                        demoLinks: demoLinks
                    };
                }''')
                
                slug = re.sub(r'[^a-z0-9]+', '_', cs['title'].lower()).strip('_')[:60]
                out_path = os.path.join(RAW_DIR, f"{slug}.md")
                
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(f"# {cs['title']}\n")
                    f.write(f"Source: {cs['href']}\n\n")
                    if content['demoLinks']:
                        f.write("## Demos & GitHub Repositories\n")
                        for d in content['demoLinks']:
                            f.write(f"- [{d['text']}]({d['href']})\n")
                        f.write("\n")
                    f.write(content['markdown'])
                    
                print(f"[SUCCESS] Saved Codrops case study to {out_path} ({len(content['markdown'])} chars)")
                fetched_count += 1
                
                if fetched_count >= 10:
                    print("\n[WAVE 3 BATCH 1 COMPLETE] Extracted 10 Codrops case study markdowns.")
                    break
                    
            except Exception as e:
                print(f"[ERROR] Fetching Codrops article {cs['href']}: {e}")
                
        browser.close()

if __name__ == "__main__":
    crawl_codrops()
