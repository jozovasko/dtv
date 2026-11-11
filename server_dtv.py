#!/usr/bin/env python3
import http.server
import json
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PORT = 8084
BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"

EDITOR_HTML = '''<!DOCTYPE html>
<html lang="sk">
<head>
  <meta charset="UTF-8">
  <title>DTV Kánonický Editor</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.css">
  <script src="https://cdn.jsdelivr.net/npm/easymde/dist/easymde.min.js"></script>
  <style>
    body { font-family: system-ui, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
    select, button { padding: 8px 16px; border-radius: 6px; font-weight: 600; font-size: 0.9rem; cursor: pointer; }
    select { background: #1e293b; color: #f8fafc; border: 1px solid #475569; }
    .btn-save { background: #0284c7; color: white; border: none; }
    .btn-save:hover { background: #0369a1; }
    .EasyMDEContainer { background: white; color: black; border-radius: 6px; }
    #status { margin-left: 15px; font-weight: bold; font-size: 0.9rem; }
  </style>
</head>
<body>
  <div class="header">
    <div>
      <h2>⚙️ Vizuálny Editor obsahu DTV</h2>
      <label>Vyberte stránku: </label>
      <select id="fileSelect" onchange="loadFile()">
        <option value="msba.md">msba.md (Krúžok MSBA)</option>
        <option value="index.md">index.md (Hlavný rozcestník)</option>
      </select>
    </div>
    <div>
      <span id="status"></span>
      <button class="btn-save" onclick="saveFile()">💾 Uložiť &amp; Publikovať na GitHub</button>
      <a href="/" target="_blank" style="color: #38bdf8; margin-left: 15px; text-decoration: none;">🔍 Otvoriť web &rarr;</a>
    </div>
  </div>

  <textarea id="markdownEditor"></textarea>

  <script>
    const easyMDE = new EasyMDE({
      element: document.getElementById('markdownEditor'),
      spellChecker: false,
      autosave: { enabled: false },
      toolbar: ["bold", "italic", "heading", "|", "quote", "unordered-list", "ordered-list", "|", "link", "image", "table", "|", "preview", "side-by-side", "fullscreen"]
    });

    function loadFile() {
      const filename = document.getElementById('fileSelect').value;
      fetch('/api/load?file=' + filename)
        .then(res => res.text())
        .then(text => easyMDE.value(text));
    }

    function saveFile() {
      const filename = document.getElementById('fileSelect').value;
      const content = easyMDE.value();
      const status = document.getElementById('status');
      status.style.color = '#eab308';
      status.textContent = '⏳ Zapisujem a odosielam na GitHub...';

      fetch('/api/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: json = JSON.stringify({ file: filename, content: content })
      })
      .then(res => res.json())
      .then(data => {
        if(data.ok) {
          status.style.color = '#22c55e';
          status.textContent = '✅ Uložené, skompilované a odoslané na GitHub!';
        } else {
          status.style.color = '#ef4444';
          status.textContent = '❌ Chyba: ' + data.error;
        }
      })
      .catch(err => {
        status.style.color = '#ef4444';
        status.textContent = '❌ Zlyhalo spojenie.';
      });
    }

    window.onload = loadFile;
  </script>
</body>
</html>
'''

class DTVHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ['/editor', '/editor/']:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(EDITOR_HTML.encode('utf-8'))
            return
        elif parsed.path == '/api/load':
            qs = parse_qs(parsed.query)
            fname = qs.get('file', ['msba.md'])[0]
            target = CONTENT_DIR / Path(fname).name
            if target.exists():
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(target.read_bytes())
            else:
                self.send_error(404, "File not found")
            return
        super().do_GET()

    def do_POST(self):
        if self.path == '/api/save':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            data = json.loads(body)
            fname = Path(data.get('file', 'msba.md')).name
            content = data.get('content', '')
            
            target = CONTENT_DIR / fname
            target.write_text(content, encoding='utf-8')
            
            # Autonómny rebuild a Git push
            try:
                subprocess.run(["python3", str(BASE_DIR / "build_dtv.py")], check=True)
                subprocess.run(["git", "-C", str(BASE_DIR), "add", "-A"], check=True)
                subprocess.run(["git", "-C", str(BASE_DIR), "commit", "-m", f"update(editor): {fname}"], check=False)
                subprocess.run(["git", "-C", str(BASE_DIR), "push", "origin", "main"], check=False)
                res = {"ok": True}
            except Exception as e:
                res = {"ok": False, "error": str(e)}
                
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(res).encode('utf-8'))
            return
        self.send_error(404)

if __name__ == '__main__':
    server = http.server.ThreadingHTTPServer(('0.0.0.0', PORT), DTVHandler)
    server.serve_forever()
