import os
import sys
import json
import urllib.request
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RAW_DIR = r"d:\AI-OS\scratch\awwwards_ingestion_raw"
ASSETS_DIR = os.path.join(RAW_DIR, "assets")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

urls = [
    {
        "id": "medium_how_to_win_an_awwward",
        "title": "How to Win an Awwward — Beautiful Web Design",
        "url": "https://medium.com/design-bootcamp/how-to-win-an-awwward-beautiful-webdesign-8194451b4f7a?sharedUserId=atinek900"
    },
    {
        "id": "medium_guide_building_awwwards_worthy_websites",
        "title": "A Guide on Building Awwwards-Worthy Websites",
        "url": "https://medium.com/@alex.streza/a-guide-on-building-awwwards-worthy-websites-c4fa710b1c43?sharedUserId=atinek900"
    },
    {
        "id": "designyourway_extended_font",
        "title": "What is an Extended Font?",
        "url": "https://www.designyourway.net/blog/what-is-an-extended-font/"
    }
]

# We will use playwright in Python to scrape full page HTML and render JS properly
from playwright.sync_api import sync_playwright

def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        for item in urls:
            print(f"[START] Scraping {item['title']} -> {item['url']}")
            page = context.new_page()
            try:
                page.goto(item['url'], wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(3000) # Give extra time for images and DOM
                
                # Get text content, HTML, and extract paragraphs, headings, code, and images
                title = page.title()
                
                # Extract text blocks
                content_md = page.evaluate('''() => {
                    let result = [];
                    let article = document.querySelector('article') || document.body;
                    let elements = article.querySelectorAll('h1, h2, h3, h4, p, pre, code, ul, ol, img, blockquote');
                    
                    elements.forEach(el => {
                        let tag = el.tagName.toLowerCase();
                        if (tag === 'h1') result.push('# ' + el.innerText.trim());
                        else if (tag === 'h2') result.push('\\n## ' + el.innerText.trim());
                        else if (tag === 'h3') result.push('\\n### ' + el.innerText.trim());
                        else if (tag === 'h4') result.push('\\n#### ' + el.innerText.trim());
                        else if (tag === 'p') result.push(el.innerText.trim());
                        else if (tag === 'blockquote') result.push('> ' + el.innerText.trim());
                        else if (tag === 'pre' || tag === 'code') {
                            if (el.tagName.toLowerCase() === 'pre') {
                                result.push('\\n```\\n' + el.innerText.trim() + '\\n```\\n');
                            }
                        }
                        else if (tag === 'ul' || tag === 'ol') {
                            let items = el.querySelectorAll('li');
                            items.forEach(li => result.push('- ' + li.innerText.trim()));
                        }
                        else if (tag === 'img') {
                            let src = el.getAttribute('src') || el.getAttribute('data-src');
                            let alt = el.getAttribute('alt') || 'Image';
                            if (src && !src.startsWith('data:')) {
                                result.push(`![${alt}](${src})`);
                            }
                        }
                    });
                    return result.join('\\n\\n');
                }''')
                
                output_file = os.path.join(RAW_DIR, f"{item['id']}.md")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"# {title}\n")
                    f.write(f"Source: {item['url']}\n\n")
                    f.write(content_md)
                
                print(f"[SUCCESS] Saved raw markdown to {output_file} (length: {len(content_md)} chars)")
                
            except Exception as e:
                print(f"[ERROR] Failed scraping {item['url']}: {e}")
            finally:
                page.close()
                
        browser.close()

if __name__ == "__main__":
    scrape()
