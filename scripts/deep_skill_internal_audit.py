import os
import re

WORKSPACE_ROOT = r"d:\AI-OS"
SKILLS_DIR = os.path.join(WORKSPACE_ROOT, ".agents", "skills")

OLD_FOLDER_NAMES = [
    "setup-matt-pocock-skills",
    "grilling",
    "grill-with-docs",
    "to-spec",
    "to-tickets",
    "wayfinder",
    "teach",
    "ask-matt",
    "tdd",
    "browser-testing",
    "storm-research",
    "code-review",
    "using-superpowers",
    "wait-what",
    "implement",
    "to-questionnaire",
    "errors-and-lessons"
]

REPLACEMENTS = {
    ".agents/skills/mattpocock-domain-modeling/": ".agents/skills/mattpocock-domain-modeling/",
    ".agents/skills/grill-me/": ".agents/skills/grill-me/",
    ".agents/skills/grill-me/": ".agents/skills/grill-me/",
    ".agents/skills/grill-me/": ".agents/skills/grill-me/",
    ".agents/skills/mattpocock-to-spec/": ".agents/skills/mattpocock-to-spec/",
    ".agents/skills/mattpocock-to-tickets/": ".agents/skills/mattpocock-to-tickets/",
    ".agents/skills/mattpocock-wayfinder/": ".agents/skills/mattpocock-wayfinder/",
    ".agents/skills/mattpocock-teach/": ".agents/skills/mattpocock-teach/",
    ".agents/skills/mattpocock-teach/": ".agents/skills/mattpocock-teach/",
    ".agents/skills/test-driven-development/": ".agents/skills/test-driven-development/",
    ".agents/skills/browser-testing-with-devtools/": ".agents/skills/browser-testing-with-devtools-with-devtools/",
    ".agents/skills/storm-research-project/": ".agents/skills/storm-research-project-project/",
    ".agents/skills/code-review-and-quality/": ".agents/skills/code-review-and-quality-and-quality/",
    ".agents/skills/using-agent-skills/": ".agents/skills/using-agent-skills/",
    ".agents/skills/diagnosing-bugs/": ".agents/skills/diagnosing-bugs/",
    ".agents/skills/incremental-implementation/": ".agents/skills/incremental-implementation/",
    "brain-aios/wiki/experiences/postmortems/": "brain-aios/wiki/experiences/postmortems/",
}

stale_findings = []
fixed_count = 0

for root, dirs, files in os.walk(SKILLS_DIR):
    for file in files:
        if file.endswith((".md", ".json", ".py", ".ts", ".js")):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
                
            modified = False
            for old_pat, new_pat in REPLACEMENTS.items():
                if old_pat in content:
                    stale_findings.append((file_path, old_pat, new_pat))
                    content = content.replace(old_pat, new_pat)
                    modified = True
                    
            if modified:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                fixed_count += 1

print(f"Total stale path instances found and fixed: {len(stale_findings)}")
print(f"Total files updated: {fixed_count}")
for fp, old_p, new_p in stale_findings[:20]:
    rel = os.path.relpath(fp, WORKSPACE_ROOT)
    print(f"  Fixed {old_p} -> {new_p} in {rel}")
