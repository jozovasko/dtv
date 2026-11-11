#!/usr/bin/env python3
import re
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

def transform_markdown_to_cards(body_md):
    # Ak Markdown obsahuje H3 odkazy formátu: ### [Názov](URL)
    # premeníme ich na pekné HTML dlaždice (karty)
    blocks = re.split(r'(?m)^###\s+', body_md)
    if len(blocks) <= 1:
        return markdown.markdown(body_md, extensions=['extra', 'tables'])
        
    intro_html = markdown.markdown(blocks[0], extensions=['extra']) if blocks[0].strip() else ""
    cards_html = ['<div class="grid">']
    
    for block in blocks[1:]:
        lines = block.strip().splitlines()
        header_line = lines[0]
        rest = "\n".join(lines[1:])
        
        # Parsovanie [Názov](URL)
        match = re.match(r'\[(.*?)\]\((.*?)\)', header_line)
        if match:
            title, url = match.group(1), match.group(2)
        else:
            title, url = header_line, "#"
            
        badge_text = ""
        # Kontrola prvého riadku popisu na prítomnosť kurzívy *Badge*
        desc_lines = []
        for l in rest.splitlines():
            if not badge_text and l.strip().startswith('*') and l.strip().endswith('*'):
                badge_text = l.strip().strip('*')
            else:
                desc_lines.append(l)
                
        desc_html = markdown.markdown("\n".join(desc_lines))
        badge_html = f'<span class="badge">{badge_text}</span>' if badge_text else ''
        target = 'target="_blank"' if url.startswith('http') else ''
        
        card = f'''
        <div class="card">
          <div>
            {badge_html}
            <h3>{title}</h3>
            {desc_html}
          </div>
          <a href="{url}" class="btn" {target}>Otvoriť &rarr;</a>
        </div>
        '''
        cards_html.append(card)
        
    cards_html.append('</div>')
    return intro_html + "\n" + "\n".join(cards_html)

def build():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("page.html")
    
    md_files = list(CONTENT_DIR.rglob("*.md"))
    for md_file in md_files:
        meta, body_md = parse_frontmatter(md_file.read_text(encoding="utf-8"))
        body_html = transform_markdown_to_cards(body_md)
        
        page_html = template.render(
            title=meta.get("title", "DTV FabLab"),
            subtitle=meta.get("subtitle", ""),
            badge=meta.get("badge", ""),
            body_html=body_html
        )
        out_file = BASE / (md_file.stem + ".html")
        out_file.write_text(page_html, encoding="utf-8")
        print(f"  -> Skompilované: {out_file.name}")
    print("[OK] Zostavenie DTV prebehlo úspešne.")

if __name__ == "__main__":
    build()
