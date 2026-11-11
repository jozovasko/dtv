#!/usr/bin/env python3
from pathlib import Path
import markdown
import jinja2

BASE = Path(__file__).resolve().parent
CONTENT_DIR = BASE / "content"
TEMPLATES_DIR = BASE / "templates"

def parse_frontmatter(text):
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            raw_meta = parts[1]
            body = parts[2]
            for line in raw_meta.strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body.strip()

def build():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("page.html")
    
    md_files = list(CONTENT_DIR.rglob("*.md"))
    print(f"[*] Kompilujem {len(md_files)} Markdown súborov v DTV...")
    
    for md_file in md_files:
        meta, body_md = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        body_html = markdown.markdown(body_md, extensions=['extra', 'tables'])
        
        page_html = template.render(
            title=meta.get("title", "DTV FabLab"),
            subtitle=meta.get("subtitle", ""),
            badge=meta.get("badge", ""),
            body_html=body_html
        )
        
        # Ukladáme priamo do koreňa DTV pre HTTP server
        out_file = BASE / (md_file.stem + ".html")
        out_file.write_text(page_html, encoding="utf-8")
        print(f"  -> Vygenerované: {out_file.name}")

    print("[OK] DTV portál úspešne skompilovaný.")

if __name__ == "__main__":
    build()
