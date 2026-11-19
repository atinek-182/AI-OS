import urllib.request
import re
import json

url = 'https://mktlm.obys.agency/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

title = re.findall(r'<title>(.*?)</title>', html, re.I)
print("PAGE TITLE:", title)

# Look for canonical, meta, etc.
metas = re.findall(r'<meta\s+([^>]+)>', html, re.I)
print("\n--- METAS (first 10) ---")
for m in metas[:10]:
    print("META:", m)

# Look for links
links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
internal_links = set()
for l in links:
    if l.startswith('/') or 'mktlm.obys.agency' in l:
        internal_links.add(l)
print("\n--- INTERNAL LINKS ---")
for l in sorted(internal_links):
    print("LINK:", l)

# Look for scripts
scripts = re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', html, re.I)
print("\n--- SCRIPT SOURCES ---")
for s in sorted(set(scripts)):
    print("SCRIPT:", s)

# Look for CSS stylesheets
styles = re.findall(r'<link[^>]*rel=[\'"]stylesheet[\'"][^>]*href=[\'"]([^\'"]+)[\'"]', html, re.I)
if not styles:
    styles = re.findall(r'<link[^>]*href=[\'"]([^\'"]+\.css[^\'"]*)[\'"]', html, re.I)
print("\n--- CSS STYLESHEETS ---")
for st in sorted(set(styles)):
    print("CSS:", st)

# Check fonts in CSS or links
fonts = re.findall(r'url\([\'"]?([^\'")]+\.(?:woff2|woff|ttf|otf))[\'"]?\)', html, re.I)
print("\n--- FONTS IN HTML ---")
for f in sorted(set(fonts)):
    print("FONT:", f)
