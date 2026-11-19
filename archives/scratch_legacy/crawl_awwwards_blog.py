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

def crawl_blog_index():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        base_url = "https://www.awwwards.com/blog/case-study/"
        print(f"[START] Crawling index page: {base_url}")
        
        page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(3000)
        
        # Extract article links, titles, descriptions, and pagination details
        data = page.evaluate('''() => {
            let articles = [];
            let links = document.querySelectorAll('a[href*="/blog/"], a[href*="/case-study/"], .box-item a, article a');
            links.forEach(a => {
                let href = a.href;
                let title = a.innerText.trim() || a.getAttribute('title') || '';
                if (href && (href.includes('/blog/') || href.includes('/case-study/')) && title.length > 5) {
                    if (!articles.some(item => item.href === href)) {
                        articles.push({ href: href, title: title });
                    }
                }
            });
            
            // Check pagination links
            let pagLinks = [];
            document.querySelectorAll('.pagination a, a[href*="page"]').forEach(p => {
                pagLinks.push({ href: p.href, text: p.innerText.trim() });
            });
            
            return { articles: articles, pagination: pagLinks };
        }''')
        
        print(f"[INDEX FOUND] Found {len(data['articles'])} case study article links on page 1.")
        print(f"[PAGINATION] Found pagination: {data['pagination']}")
        
        with open(os.path.join(RAW_DIR, "page1_index.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        browser.close()

if __name__ == "__main__":
    crawl_blog_index()
