import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

json_path = r"d:\AI-OS\scratch\awwwards_ingestion_raw\awwwards_blog\all_awwwards_case_studies.json"
with open(json_path, "r", encoding="utf-8", errors="replace") as f:
    data = json.load(f)

for idx in [4, 19]:
    item = data[idx]
    print(f"=== Entry {idx+1}: {item.get('title')} ===")
    print(f"URL: {item.get('url')}")
    print(f"Content Length: {len(item.get('content', ''))}")
    print(f"Snippet:\n{item.get('content', '')[:1000]}\n")
