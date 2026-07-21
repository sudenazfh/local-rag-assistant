"""Render ROADMAP_fixed.md -> HTML -> PDF (via headless Edge). Throwaway tool."""
import subprocess
from pathlib import Path
from markdown_it import MarkdownIt

HERE = Path(__file__).parent
md_file = HERE / "ROADMAP_fixed.md"
html_file = HERE / "ROADMAP_fixed.html"
pdf_file = HERE / "ROADMAP_fixed.pdf"

CSS = """
body { font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.5;
       max-width: 820px; margin: 0 auto; padding: 24px; color: #1a1a1a; }
h1, h2, h3 { line-height: 1.25; }
h2 { border-bottom: 2px solid #ddd; padding-bottom: 4px; margin-top: 32px; }
code { font-family: Consolas, 'Courier New', monospace; background: #f2f2f2;
       padding: 1px 4px; border-radius: 3px; font-size: 0.9em; }
pre { background: #1e1e1e; color: #e6e6e6; padding: 14px; border-radius: 6px;
      overflow-x: auto; font-size: 0.85em; }
pre code { background: none; color: inherit; padding: 0; }
blockquote { border-left: 4px solid #f0c000; background: #fffbe6; margin: 12px 0;
             padding: 8px 14px; }
table { border-collapse: collapse; }
th, td { border: 1px solid #ccc; padding: 6px 10px; }
"""

md = MarkdownIt("gfm-like").disable("linkify")
body = md.render(md_file.read_text(encoding="utf-8"))
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
html_file.write_text(html, encoding="utf-8")
print(f"HTML written: {html_file}")

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
subprocess.run([
    EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file}", html_file.as_uri(),
], check=True)
print(f"PDF written: {pdf_file}")
