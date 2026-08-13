import os
import json

BASE_DIR = r"C:\Users\HP\Downloads\Components"
REGISTRY_PATH = os.path.join(BASE_DIR, "components_ai_registry.json")

TARGET_IDS = [
    "COMP-001", "COMP-021", "COMP-022", "COMP-023", "COMP-024", "COMP-025", "COMP-029",
    "COMP-044", "COMP-054", "COMP-055", "COMP-056", "COMP-067", "COMP-080", "COMP-081",
    "COMP-082", "COMP-083", "COMP-084", "COMP-086", "COMP-089", "COMP-092", "COMP-093",
    "COMP-095", "COMP-096", "COMP-109", "COMP-110", "COMP-111", "COMP-117", "COMP-121",
    "COMP-122", "COMP-128", "COMP-130", "COMP-132", "COMP-133", "COMP-135", "COMP-137",
    "COMP-138", "COMP-140", "COMP-141", "COMP-142", "COMP-144", "COMP-146", "COMP-147",
    "COMP-148", "COMP-149", "COMP-150", "COMP-151", "COMP-154", "COMP-158", "COMP-160",
    "COMP-163", "COMP-166", "COMP-173", "COMP-174"
]

with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
    registry = json.load(f)

print(f"Total target components to inspect: {len(TARGET_IDS)}")
target_dict = {item["id"]: item for item in registry if item["id"] in TARGET_IDS}

for comp_id in TARGET_IDS:
    item = target_dict.get(comp_id)
    if item:
        print(f"{item['id']} | {item['name']} | Status: {item['status']} | Entry: {item['entry_url']}")
        print(f"   Path: {item['abs_path']}")
        print(f"   All Entries: {item['all_entries']}")
    else:
        print(f"{comp_id} NOT FOUND!")
