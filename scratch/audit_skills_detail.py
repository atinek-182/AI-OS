import os

skills_dir = r"d:\AI-OS\.agents\skills"
items = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
print(f"Total skills: {len(items)}")

consolidation_pairs = [
    ("grill-me", ["grilling", "grill-with-docs", "to-questionnaire"]),
    ("mattpocock-to-spec", ["to-spec"]),
    ("mattpocock-to-tickets", ["to-tickets"]),
    ("mattpocock-wayfinder", ["wayfinder"]),
    ("mattpocock-teach", ["teach", "ask-matt"]),
    ("mattpocock-domain-modeling", ["setup-matt-pocock-skills"]),
    ("test-driven-development", ["tdd"]),
    ("browser-testing-with-devtools", ["browser-testing"]),
    ("storm-research-project", ["storm-research"]),
    ("code-review-and-quality", ["code-review"]),
    ("using-agent-skills", ["using-superpowers"]),
    ("diagnosing-bugs", ["wait-what"]),
    ("incremental-implementation", ["implement"]),
]

for master, slaved_list in consolidation_pairs:
    print(f"\nMaster: {master}")
    master_path = os.path.join(skills_dir, master, "SKILL.md")
    print(f"  Master exists: {os.path.exists(master_path)}")
    for slave in slaved_list:
        slave_path = os.path.join(skills_dir, slave)
        print(f"  Slave: {slave} (exists: {os.path.exists(slave_path)})")
