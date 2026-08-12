import os
import sys
import http.server
import socketserver
import urllib.parse
import mimetypes

# Standard UTF-8 output encoding for Windows OS
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"C:\Users\HP\Downloads\Components"
PORT = 8080

class SecureComponentRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def guess_type(self, path):
        # Force strict JavaScript MIME type over Windows Registry corruption
        clean_p = path.split('?')[0].split('#')[0]
        ext = os.path.splitext(clean_p)[1].lower()
        if ext in ('.js', '.mjs', '.ts', '.jsx', '.tsx'):
            return 'application/javascript'
        if ext == '.css':
            return 'text/css'
        if ext == '.webp':
            return 'image/webp'
        if ext in ('.glsl', '.wgsl'):
            return 'text/plain'
        if ext == '.json':
            return 'application/json'
        if ext in ('.woff', '.woff2'):
            return f'font/{ext[1:]}'
        return super().guess_type(path)

    def translate_path(self, path):
        # Prevent directory traversal
        parsed_path = urllib.parse.unquote(path)
        clean_path = parsed_path.lstrip('/')
        full_path = os.path.normpath(os.path.join(BASE_DIR, clean_path))
        
        # Verify traversal safety
        try:
            common = os.path.commonpath([BASE_DIR, full_path])
            if common != BASE_DIR:
                print(f"[SECURITY REJECT] Traversal attempt blocked: {path}")
                return os.path.join(BASE_DIR, "404.html")
        except ValueError:
            return os.path.join(BASE_DIR, "404.html")

        # If file exists, return directly
        if os.path.exists(full_path):
            return full_path

        # Subfolder Asset Fallback (public/, dist/, src/, img/, assets/)
        parts = clean_path.split('/')
        if len(parts) >= 3:
            category = parts[0]
            comp_folder = parts[1]
            asset_subpath = '/'.join(parts[2:])
            
            comp_base = os.path.join(BASE_DIR, category, comp_folder)
            if os.path.exists(comp_base):
                for subfolder in ['public', 'dist', 'src', 'img', 'assets']:
                    candidate = os.path.normpath(os.path.join(comp_base, subfolder, asset_subpath))
                    if os.path.exists(candidate):
                        return candidate

        return full_path

    def end_headers(self):
        # Enable CORS for local cross-origin assets & ES modules
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        if args and len(args) > 1 and str(args[1]) not in ('200', '304'):
            print(f"[SERVER LOG] {format % args}")

def run_server():
    server_address = ('127.0.0.1', PORT)
    with socketserver.TCPServer(server_address, SecureComponentRequestHandler) as httpd:
        print(f"[COMPONENT STUDIO SERVER] Serving C:\\Users\\HP\\Downloads\\Components on http://127.0.0.1:{PORT}")
        print("[SECURITY OS] Strict JS MIME Override Active. Bound to 127.0.0.1.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[COMPONENT STUDIO SERVER] Shutting down cleanly.")
            httpd.server_close()

if __name__ == "__main__":
    run_server()
