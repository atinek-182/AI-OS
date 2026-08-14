import os
import re

WORKSPACE_ROOT = r"d:\AI-OS"

SCAN_ROOTS = [
    os.path.join(WORKSPACE_ROOT, ".agents"),
    os.path.join(WORKSPACE_ROOT, "context"),
    os.path.join(WORKSPACE_ROOT, "references"),
    os.path.join(WORKSPACE_ROOT, "brain-aios"),
    os.path.join(WORKSPACE_ROOT, "second-brain-zorixel"),
    os.path.join(WORKSPACE_ROOT, "decisions"),
    os.path.join(WORKSPACE_ROOT, "scripts"),
    os.path.join(WORKSPACE_ROOT, "projects"),
    os.path.join(WORKSPACE_ROOT, "clients"),
    os.path.join(WORKSPACE_ROOT, "brainstorms"),
]

ROOT_FILES = [
    os.path.join(WORKSPACE_ROOT, "AGENTS.md"),
    os.path.join(WORKSPACE_ROOT, "GEMINI.md"),
    os.path.join(WORKSPACE_ROOT, "hot.md"),
    os.path.join(WORKSPACE_ROOT, "MEMORY.md"),
    os.path.join(WORKSPACE_ROOT, "EXPANSIONS.md"),
    os.path.join(WORKSPACE_ROOT, "LOOPS.md"),
    os.path.join(WORKSPACE_ROOT, "WORKSPACE_MAP.md"),
]

REPLACEMENTS = {
    ".agents/skills/mattpocock-domain-modeling": ".agents/skills/mattpocock-domain-modeling",
    ".agents/skills/grill-me": ".agents/skills/grill-me",
    ".agents/skills/grill-me": ".agents/skills/grill-me",
    ".agents/skills/grill-me": ".agents/skills/grill-me",
    ".agents/skills/mattpocock-to-spec": ".agents/skills/mattpocock-to-spec",
    ".agents/skills/mattpocock-to-tickets": ".agents/skills/mattpocock-to-tickets",
    ".agents/skills/mattpocock-wayfinder": ".agents/skills/mattpocock-wayfinder",
    ".agents/skills/mattpocock-teach": ".agents/skills/mattpocock-teach",
    ".agents/skills/mattpocock-teach": ".agents/skills/mattpocock-teach",
    ".agents/skills/test-driven-development": ".agents/skills/test-driven-development",
    ".agents/skills/browser-testing-with-devtools": ".agents/skills/browser-testing-with-devtools-with-devtools",
    ".agents/skills/storm-research-project": ".agents/skills/storm-research-project-project",
    ".agents/skills/code-review-and-quality": ".agents/skills/code-review-and-quality-and-quality",
    ".agents/skills/using-agent-skills": ".agents/skills/using-agent-skills",
    ".agents/skills/diagnosing-bugs": ".agents/skills/diagnosing-bugs",
    ".agents/skills/incremental-implementation": ".agents/skills/incremental-implementation",
    "brain-aios/wiki/experiences/postmortems/": "brain-aios/wiki/experiences/postmortems/",
    "brain-aios/wiki/mcp-servers/gws-api.md": "brain-aios/wiki/mcp-servers/gws-api.md",
    "brain-aios/wiki/mcp-servers/notion-api.md": "brain-aios/wiki/mcp-servers/notion-api.md",
    "brain-aios/wiki/mcp-servers/github-api.md": "brain-aios/wiki/mcp-servers/github-api.md",
    "brain-aios/wiki/mcp-servers/figma-api.md": "brain-aios/wiki/mcp-servers/figma-api.md",
    "brain-aios/wiki/mcp-servers/context7-api.md": "brain-aios/wiki/mcp-servers/context7-api.md",
    "brain-aios/wiki/mcp-servers/magic-api.md": "brain-aios/wiki/mcp-servers/magic-api.md",
    "brain-aios/wiki/mcp-servers/playwright-api.md": "brain-aios/wiki/mcp-servers/playwright-api.md",
    "brain-aios/wiki/mcp-servers/chrome-devtools-api.md": "brain-aios/wiki/mcp-servers/chrome-devtools-api.md",
    "brain-aios/wiki/strategy/3ms-framework.md": "brain-aios/wiki/strategy/3ms-framework.md",
    "brain-aios/wiki/sops/aios-architecture-guide.md": "brain-aios/wiki/sops/aios-architecture-guide.md",
    "brain-aios/wiki/sops/aios-user-manual.md": "brain-aios/wiki/sops/aios-user-manual.md",
    "brain-aios/wiki/sops/antigravity-skills-guide.md": "brain-aios/wiki/sops/antigravity-skills-guide.md",
    "brain-aios/wiki/sops/utility-scripts.md": "brain-aios/wiki/sops/utility-scripts.md",
    "brain-aios/wiki/sops/global-rules-conflict-resolution.md": "brain-aios/wiki/sops/global-rules-conflict-resolution.md",
    "second-brain-zorixel/wiki/brand/voice.md": "second-brain-zorixel/wiki/brand/voice.md",
    "second-brain-zorixel/wiki/brand/zorixel-brand-identity.md": "second-brain-zorixel/wiki/brand/zorixel-brand-identity.md",
    "references/awwwards-research-vault/data/23-sites-matrix.json": "references/awwwards-research-vault/data/23-sites-matrix.json",
}

total_fixed_instances = 0
total_files_fixed = 0

all_target_files = list(ROOT_FILES)
for sroot in SCAN_ROOTS:
    if os.path.exists(sroot):
        for root, dirs, files in os.walk(sroot):
            if "node_modules" in dirs:
                dirs.remove("node_modules")
            if ".git" in dirs:
                dirs.remove(".git")
            for file in files:
                if file.endswith((".md", ".py", ".json", ".js", ".ts", ".html", ".css")):
                    all_target_files.append(os.path.join(root, file))

for file_path in all_target_files:
    if not os.path.exists(file_path):
        continue
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        continue
        
    modified = False
    for old_pat, new_pat in REPLACEMENTS.items():
        if old_pat in content:
            # count occurrences
            count = content.count(old_pat)
            total_fixed_instances += count
            content = content.replace(old_pat, new_pat)
            modified = True
            
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        total_files_fixed += 1

print(f"Universal Workspace Integrity Sweep Complete:")
print(f"  Total Scanned Files: {len(all_target_files)}")
print(f"  Files Updated: {total_files_fixed}")
print(f"  Total Link/Path Instances Refactored: {total_fixed_instances}")
