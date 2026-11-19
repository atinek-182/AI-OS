import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

json_path = r"d:\AI-OS\scratch\awwwards_ingestion_raw\awwwards_blog\all_awwwards_case_studies.json"
with open(json_path, "r", encoding="utf-8", errors="replace") as f:
    data = json.load(f)

matches = []
for idx, item in enumerate(data):
    title = item.get("title", "")
    content = item.get("content", "")
    text = (title + " " + content).lower()
    if "good fella" in text or "fella" in text:
        matches.append((idx, title))

print(f"Good Fella matches in JSON: {len(matches)}")
for m in matches:
    print(f"  [{m[0]}] {m[1]}")
