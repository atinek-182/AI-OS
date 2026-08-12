import os
import sys
import json
import re

# Standard UTF-8 output encoding for Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\HP\Downloads\Components"
MANIFEST_PATH = os.path.join(BASE_DIR, "component_manifest.json")
REGISTRY_PATH = os.path.join(BASE_DIR, "components_ai_registry.json")
THUMBNAILS_DIR = os.path.join(BASE_DIR, "public", "thumbnails")

os.makedirs(THUMBNAILS_DIR, exist_ok=True)

CATEGORIES = [
    "01-text-and-typography",
    "02-navigation-and-menus",
    "03-buttons-and-interactions",
    "04-images-galleries-and-sliders",
    "05-scrollytelling-and-scrolltrigger",
    "06-cursors-and-mouse-effects",
    "07-webgl-3d-and-canvas-shaders",
    "08-full-site-clones-and-preloaders",
    "09-utilities-and-miscellaneous"
]

CATEGORY_NAMES = {
    "01-text-and-typography": "Typography & Text",
    "02-navigation-and-menus": "Navigation & Menus",
    "03-buttons-and-interactions": "Buttons & Interactions",
    "04-images-galleries-and-sliders": "Galleries & Sliders",
    "05-scrollytelling-and-scrolltrigger": "Scrollytelling & Motion",
    "06-cursors-and-mouse-effects": "Cursors & Mouse Effects",
    "07-webgl-3d-and-canvas-shaders": "WebGL & Canvas Shaders",
    "08-full-site-clones-and-preloaders": "Preloaders & Full Sites",
    "09-utilities-and-miscellaneous": "Utilities & Misc"
}

def scan_component(comp_dir, name, category, comp_id):
    abs_path = os.path.join(BASE_DIR, category, name)
    rel_path = f"{category}/{name}"
    
    # Entry point discovery
    html_files = []
    has_package_json = os.path.exists(os.path.join(abs_path, "package.json"))
    
    for root, dirs, files in os.walk(abs_path):
        # Exclude node_modules or .git
        if "node_modules" in dirs:
            dirs.remove("node_modules")
        if ".git" in dirs:
            dirs.remove(".git")
            
        for f in files:
            if f.endswith(".html") and not f.startswith("._") and "__MACOSX" not in root:
                full_f = os.path.join(root, f)
                rel_f = os.path.relpath(full_f, abs_path).replace("\\", "/")
                html_files.append(rel_f)
                
    # Sort html_files so index.html comes first
    html_files.sort(key=lambda x: (0 if x == "index.html" else (1 if x.endswith("index.html") else 2), x))
    
    primary_entry = html_files[0] if html_files else None
    
    # Detect Tech Stack & Libraries
    tech_stack = set()
    code_content = ""
    
    # Read primary entry or package.json for keywords
    if primary_entry:
        entry_abs = os.path.join(abs_path, primary_entry)
        try:
            with open(entry_abs, "r", encoding="utf-8", errors="ignore") as file:
                code_content += file.read()
        except Exception:
            pass
            
    if has_package_json:
        try:
            with open(os.path.join(abs_path, "package.json"), "r", encoding="utf-8", errors="ignore") as file:
                code_content += file.read()
        except Exception:
            pass

    content_lower = code_content.lower()
    
    if "three" in content_lower or "three.js" in content_lower:
        tech_stack.add("Three.js")
    if "gsap" in content_lower or "scrolltrigger" in content_lower or "tweenmax" in content_lower:
        tech_stack.add("GSAP")
    if "anime" in content_lower or "anime.js" in content_lower:
        tech_stack.add("Anime.js")
    if "webgl" in content_lower or "shader" in content_lower or ".glsl" in content_lower or "fragmentshader" in content_lower:
        tech_stack.add("WebGL")
    if "canvas" in content_lower or "2dcontext" in content_lower or "getcontext('2d')" in content_lower:
        tech_stack.add("Canvas")
    if "lenis" in content_lower:
        tech_stack.add("Lenis")
    if "pixi" in content_lower:
        tech_stack.add("Pixi.js")
    if "react" in content_lower:
        tech_stack.add("React")
    if "vite" in content_lower:
        tech_stack.add("Vite")
    if not tech_stack:
        tech_stack.add("CSS/JS")
        
    # Health status classification
    health_note = "Pending Verification"
    if primary_entry:
        if len(html_files) > 1:
            status = "MULTI-DEMO"
            status_color = "blue"
        else:
            status = "STATIC READY"
            status_color = "green"
    elif has_package_json:
        status = "NPM BUILD REQD"
        status_color = "amber"
        health_note = "Requires npm install & dev server build script"
    else:
        status = "NO ENTRY"
        status_color = "red"
        health_note = "Missing HTML entry point"
        
    formatted_id = f"COMP-{comp_id:03d}"
    thumbnail_path = f"public/thumbnails/{formatted_id}.png"
    
    # Prompt string for 1-click clipboard copy
    ai_prompt = (
        f"Adapt Component {formatted_id} ({name}) from {rel_path} into Next.js/React TypeScript (.tsx). "
        f"Tech stack: {', '.join(sorted(tech_stack))}. "
        f"Ensure 'use client', CSS Modules isolation (styles.module.css), and useEffect GPU memory cleanup."
    )
    
    return {
        "id": formatted_id,
        "index": comp_id,
        "name": name,
        "category": category,
        "category_name": CATEGORY_NAMES.get(category, category),
        "rel_path": rel_path,
        "abs_path": abs_path,
        "primary_entry": primary_entry,
        "entry_url": f"{rel_path}/{primary_entry}" if primary_entry else "",
        "all_entries": html_files,
        "has_package_json": has_package_json,
        "tech_stack": sorted(list(tech_stack)),
        "status": status,
        "status_color": status_color,
        "health_note": health_note,
        "thumbnail": thumbnail_path,
        "ai_prompt": ai_prompt
    }

def main():
    print("[COMPONENT BUILDER] Scanning C:\\Users\\HP\\Downloads\\Components...")
    
    components_by_cat = {cat: [] for cat in CATEGORIES}
    
    # List subdirectories cleanly
    global_index = 1
    registry = []
    
    for cat in CATEGORIES:
        cat_path = os.path.join(BASE_DIR, cat)
        if not os.path.exists(cat_path):
            continue
        items = sorted(os.listdir(cat_path))
        for item in items:
            item_path = os.path.join(cat_path, item)
            if os.path.isdir(item_path):
                comp_data = scan_component(item_path, item, cat, global_index)
                registry.append(comp_data)
                global_index += 1
                
    # Save Registry
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
        
    print(f"[REGISTRY CREATED] Scanned {len(registry)} components into components_ai_registry.json")
    
    # Build Dashboard HTML
    generate_dashboard_html(registry)

def generate_dashboard_html(registry):
    dashboard_path = os.path.join(BASE_DIR, "index.html")
    
    # Calculate stats
    total_comp = len(registry)
    static_ready = sum(1 for c in registry if c["status"] in ("STATIC READY", "MULTI-DEMO"))
    npm_reqd = sum(1 for c in registry if c["status"] == "NPM BUILD REQD")
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZORIXEL Component Studio Dashboard — 175+ Vault</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-obsidian: #0D0E12;
            --bg-card: #161922;
            --bg-card-hover: #1E2230;
            --border-subtle: #262B3D;
            --border-hover: #D61C2C;
            --text-linen: #FAF8F5;
            --text-muted: #8E96AD;
            --crimson-accent: #D61C2C;
            --burgundy-accent: #6D001A;
            --gold-accent: #C5A059;
            --status-green: #10B981;
            --status-amber: #F59E0B;
            --status-blue: #3B82F6;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-obsidian);
            color: var(--text-linen);
            font-family: 'Outfit', sans-serif;
            min-height: 100vh;
            padding-bottom: 60px;
        }}

        /* Toast Alert */
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: var(--crimson-accent);
            color: #FFFFFF;
            padding: 12px 24px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            box-shadow: 0 10px 25px rgba(214, 28, 44, 0.4);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 9999;
        }}
        #toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}

        /* Header Bar */
        header {{
            background: rgba(13, 14, 18, 0.95);
            border-bottom: 1px solid var(--border-subtle);
            position: sticky;
            top: 0;
            z-index: 100;
            backdrop-filter: blur(10px);
            padding: 20px 40px;
        }}

        .header-container {{
            max-width: 1600px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            flex-wrap: wrap;
        }}

        .brand-title {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}

        .brand-logo {{
            background: var(--crimson-accent);
            color: #FFF;
            font-weight: 800;
            font-size: 18px;
            padding: 8px 14px;
            border-radius: 4px;
            letter-spacing: 1px;
        }}

        .brand-text h1 {{
            font-size: 22px;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: var(--text-linen);
        }}

        .brand-text p {{
            font-size: 13px;
            color: var(--text-muted);
        }}

        .stats-bar {{
            display: flex;
            gap: 20px;
        }}

        .stat-badge {{
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            padding: 8px 16px;
            border-radius: 6px;
            text-align: center;
        }}

        .stat-value {{
            font-size: 18px;
            font-weight: 700;
            color: var(--text-linen);
            font-family: 'JetBrains Mono', monospace;
        }}

        .stat-label {{
            font-size: 11px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        /* Search & Filter Toolbar */
        .controls-section {{
            max-width: 1600px;
            margin: 30px auto 0;
            padding: 0 40px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}

        .search-box {{
            position: relative;
            width: 100%;
        }}

        .search-box input {{
            width: 100%;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            padding: 16px 20px;
            border-radius: 8px;
            color: var(--text-linen);
            font-size: 16px;
            font-family: 'Outfit', sans-serif;
            outline: none;
            transition: border-color 0.2s;
        }}

        .search-box input:focus {{
            border-color: var(--crimson-accent);
        }}

        .category-tabs {{
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 8px;
            scrollbar-width: thin;
        }}

        .tab-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            color: var(--text-muted);
            padding: 10px 18px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s;
        }}

        .tab-btn:hover, .tab-btn.active {{
            background: var(--crimson-accent);
            color: #FFFFFF;
            border-color: var(--crimson-accent);
        }}

        /* Components Grid */
        .grid-container {{
            max-width: 1600px;
            margin: 30px auto;
            padding: 0 40px;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 24px;
        }}

        .card {{
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: all 0.3s ease;
        }}

        .card:hover {{
            border-color: var(--crimson-accent);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
        }}

        .card-preview {{
            width: 100%;
            height: 210px;
            background: #0A0B0E;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .card-preview img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: opacity 0.3s;
        }}

        .card-preview-fallback {{
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
            font-size: 12px;
            text-align: center;
            padding: 20px;
        }}

        .card-badge-id {{
            position: absolute;
            top: 12px;
            left: 12px;
            background: rgba(13, 14, 18, 0.85);
            border: 1px solid var(--border-subtle);
            color: var(--text-linen);
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
            font-size: 11px;
            padding: 4px 8px;
            border-radius: 4px;
        }}

        .card-badge-status {{
            position: absolute;
            top: 12px;
            right: 12px;
            font-size: 10px;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 4px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .status-green {{ background: rgba(16, 185, 129, 0.2); color: #34D399; border: 1px solid #10B981; }}
        .status-blue {{ background: rgba(59, 130, 246, 0.2); color: #60A5FA; border: 1px solid #3B82F6; }}
        .status-amber {{ background: rgba(245, 158, 11, 0.2); color: #FBBF24; border: 1px solid #F59E0B; }}

        .card-body {{
            padding: 20px;
            display: flex;
            flex-direction: column;
            flex: 1;
            justify-content: space-between;
            gap: 16px;
        }}

        .card-header-info h3 {{
            font-size: 16px;
            font-weight: 700;
            color: var(--text-linen);
            margin-bottom: 6px;
            line-height: 1.3;
        }}

        .card-category {{
            font-size: 12px;
            color: var(--text-muted);
        }}

        .tech-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}

        .tech-pill {{
            background: #11131A;
            border: 1px solid var(--border-subtle);
            color: var(--gold-accent);
            font-size: 11px;
            font-family: 'JetBrains Mono', monospace;
            padding: 3px 8px;
            border-radius: 4px;
        }}

        .card-actions {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 10px;
        }}

        .btn {{
            padding: 10px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            border: none;
        }}

        .btn-launch {{
            background: var(--crimson-accent);
            color: #FFFFFF;
        }}

        .btn-launch:hover {{
            background: #B91424;
        }}

        .btn-copy {{
            background: var(--bg-obsidian);
            border: 1px solid var(--border-subtle);
            color: var(--text-linen);
        }}

        .btn-copy:hover {{
            border-color: var(--text-linen);
            background: var(--bg-card-hover);
        }}

        .multi-demo-select {{
            grid-column: span 2;
            background: var(--bg-obsidian);
            border: 1px solid var(--border-subtle);
            color: var(--text-linen);
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12px;
            outline: none;
            cursor: pointer;
        }}
    </style>
</head>
<body>

    <div id="toast">Copied prompt for AI to clipboard!</div>

    <header>
        <div class="header-container">
            <div class="brand-title">
                <div class="brand-logo">ZORIXEL</div>
                <div class="brand-text">
                    <h1>Component Studio Dashboard</h1>
                    <p>175+ Codrops & Awwwards Component Vault · Localhost Server http://127.0.0.1:8080</p>
                </div>
            </div>
            <div class="stats-bar">
                <div class="stat-badge">
                    <div class="stat-value">{total_comp}</div>
                    <div class="stat-label">Total Vault</div>
                </div>
                <div class="stat-badge">
                    <div class="stat-value" style="color: #34D399;">{static_ready}</div>
                    <div class="stat-label">Static Ready</div>
                </div>
                <div class="stat-badge">
                    <div class="stat-value" style="color: #FBBF24;">{npm_reqd}</div>
                    <div class="stat-label">NPM Required</div>
                </div>
            </div>
        </div>
    </header>

    <div class="controls-section">
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="Search 175 components by name, tech stack (Three.js, GSAP, WebGL), or ID (COMP-042)...">
        </div>
        <div class="category-tabs" id="categoryTabs">
            <button class="tab-btn active" data-cat="ALL">All Categories ({total_comp})</button>
"""

    for cat_slug, cat_name in CATEGORY_NAMES.items():
        cat_count = sum(1 for c in registry if c["category"] == cat_slug)
        html_content += f'            <button class="tab-btn" data-cat="{cat_slug}">{cat_name} ({cat_count})</button>\n'

    html_content += """        </div>
    </div>

    <div class="grid-container" id="componentsGrid">
"""

    for item in registry:
        tech_pills = "".join([f'<span class="tech-pill">{t}</span>' for t in item["tech_stack"]])
        
        # Action button
        if item["entry_url"]:
            launch_html = f'<a href="{item["entry_url"]}" target="_blank" class="btn btn-launch">Launch Demo</a>'
        else:
            launch_html = f'<button disabled class="btn btn-launch" style="opacity:0.5; cursor:not-allowed;">NPM Required</button>'
            
        # Multi demo select
        multi_demo_html = ""
        if len(item["all_entries"]) > 1:
            multi_demo_html = '<select class="multi-demo-select" onchange="if(this.value) window.open(this.value, \'_blank\')">\n'
            multi_demo_html += '  <option value="">Switch Demo Variant (' + str(len(item["all_entries"])) + ' demos)...</option>\n'
            for entry_file in item["all_entries"]:
                url = f"{item['rel_path']}/{entry_file}"
                multi_demo_html += f'  <option value="{url}">{entry_file}</option>\n'
            multi_demo_html += '</select>\n'

        import html as html_lib
        esc_prompt = html_lib.escape(item["ai_prompt"], quote=True)
        
        html_content += f"""        <div class="card" data-cat="{item['category']}" data-search="{item['id']} {item['name']} {item['category_name']} {' '.join(item['tech_stack'])}".toLowerCase()>
            <div class="card-preview">
                <img src="{item['thumbnail']}" alt="{item['name']}" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
                <div class="card-preview-fallback" style="display:none;">
                    <div>{item['id']}</div>
                    <div style="margin-top:6px; color: var(--gold-accent);">{item['name']}</div>
                </div>
                <div class="card-badge-id">{item['id']}</div>
                <div class="card-badge-status status-{item['status_color']}">{item['status']}</div>
            </div>
            <div class="card-body">
                <div class="card-header-info">
                    <h3>{item['name']}</h3>
                    <div class="card-category">{item['category_name']}</div>
                </div>
                <div class="tech-pills">
                    {tech_pills}
                </div>
                {multi_demo_html}
                <div class="card-actions">
                    {launch_html}
                    <button class="btn btn-copy" data-prompt="{esc_prompt}">Copy for AI</button>
                </div>
            </div>
        </div>
"""

    html_content += """    </div>

    <script>
        // Live Search Filter
        const searchInput = document.getElementById('searchInput');
        const cards = document.querySelectorAll('.card');
        const tabBtns = document.querySelectorAll('.tab-btn');
        let currentCategory = 'ALL';

        function filterGrid() {
            const query = searchInput.value.toLowerCase().trim();
            cards.forEach(card => {
                const matchesCat = (currentCategory === 'ALL' || card.getAttribute('data-cat') === currentCategory);
                const matchesSearch = !query || card.getAttribute('data-search').includes(query);
                if (matchesCat && matchesSearch) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        searchInput.addEventListener('input', filterGrid);

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                tabBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentCategory = btn.getAttribute('data-cat');
                filterGrid();
            });
        });

        document.addEventListener('click', function(e) {
            const btn = e.target.closest('.btn-copy');
            if (btn) {
                const text = btn.getAttribute('data-prompt');
                if (text) {
                    if (navigator.clipboard && navigator.clipboard.writeText) {
                        navigator.clipboard.writeText(text).then(function() {
                            showToast('Copied prompt for AI to clipboard!');
                        }).catch(function() {
                            fallbackCopy(text);
                        });
                    } else {
                        fallbackCopy(text);
                    }
                }
            }
        });

        function fallbackCopy(text) {
            var ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.left = '-9999px';
            document.body.appendChild(ta);
            ta.select();
            try {
                document.execCommand('copy');
                showToast('Copied prompt for AI to clipboard!');
            } catch(err) {
                alert('Copy failed: ' + err);
            }
            document.body.removeChild(ta);
        }

        function showToast(msg) {
            const toast = document.getElementById('toast');
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(function() { toast.classList.remove('show'); }, 2500);
        }
    </script>
</body>
</html>
"""

    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"[DASHBOARD CREATED] Successfully wrote {dashboard_path}")

if __name__ == "__main__":
    main()
