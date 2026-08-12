import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

json_path = r"d:\AI-OS\scratch\awwwards_ingestion_raw\awwwards_blog\all_awwwards_case_studies.json"
with open(json_path, "r", encoding="utf-8", errors="replace") as f:
    data = json.load(f)

print(f"Total Case Studies: {len(data)}\n")
for idx, item in enumerate(data):
    title = item.get("title", "Untitled")
    url = item.get("url", "")
    print(f"[{idx+1:03d}] {title}")
