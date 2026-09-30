import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = r"C:\Users\antoni\Dola\clones\G0DM0D3"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
        
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)
    # Check if index.html exists
    if not os.path.exists("index.html"):
        print(f"Error: index.html not found in {DIRECTORY}")
        sys.exit(1)
        
    print("="*60)
    print(" G0DM0D3 Local Multi-LLM Runner")
    print(f" Directory: {DIRECTORY}")
    print(f" URL: http://localhost:{PORT}")
    print(" Features: Side-by-Side ChatGPT, Claude, Gemini, Grok")
    print(" Modes: GODMODE CLASSIC, ULTRAPLINIAN (60 models), AutoTune")
    print("="*60)
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Server started on http://localhost:{PORT}")
            webbrowser.open(f"http://localhost:{PORT}/index.html")
            print("Press Ctrl+C to stop.")
            httpd.serve_forever()
    except OSError as e:
        print(f"Port {PORT} already in use or error: {e}")
        webbrowser.open(f"http://localhost:{PORT}/index.html")

if __name__ == "__main__":
    main()
