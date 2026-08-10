import urllib.request
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RAW_DIR = r"d:\AI-OS\scratch\awwwards_ingestion_raw"

urls = [
    ("medium_how_to_win_an_awwward.md", "https://medium.com/design-bootcamp/how-to-win-an-awwward-beautiful-webdesign-8194451b4f7a?sharedUserId=atinek900"),
    ("medium_guide_building_awwwards_worthy_websites.md", "https://medium.com/@alex.streza/a-guide-on-building-awwwards-worthy-websites-c4fa710b1c43?sharedUserId=atinek900")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

for fname, url in urls:
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8')
            
            # Simple clean up of HTML to text/markdown
            # Extract paragraphs, section headers, h1-h4
            clean_text = []
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
            title = title_match.group(1) if title_match else fname
            clean_text.append(f"# {title}\nSource: {url}\n")
            
            # Find all headings and paragraphs
            items = re.findall(r'<(h1|h2|h3|h4|p|pre|blockquote)[^>]*>(.*?)</\1>', html, re.DOTALL | re.IGNORECASE)
            for tag, content in items:
                # Strip HTML tags from content
                text = re.sub(r'<[^>]+>', '', content).strip()
                if not text:
                    continue
                if tag.lower() == 'h1':
                    clean_text.append(f"# {text}")
                elif tag.lower() == 'h2':
                    clean_text.append(f"## {text}")
                elif tag.lower() == 'h3':
                    clean_text.append(f"### {text}")
                elif tag.lower() == 'h4':
                    clean_text.append(f"#### {text}")
                elif tag.lower() == 'p':
                    clean_text.append(text)
                elif tag.lower() == 'blockquote':
                    clean_text.append(f"> {text}")
                elif tag.lower() == 'pre':
                    clean_text.append(f"```\n{text}\n```")
            
            out_path = os.path.join(RAW_DIR, fname)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(clean_text))
            print(f"[SUCCESS] Saved {fname} with {len(clean_text)} blocks ({len(html)} raw bytes)")
    except Exception as e:
        print(f"[ERROR] Fetching {url}: {e}")
