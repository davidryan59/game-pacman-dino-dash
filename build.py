#!/usr/bin/env python3
"""Wrap index.html in a full HTML document for Netlify.

The Artifact platform supplies its own <head>, so index.html ships as a
fragment. Netlify serves the file raw, so it needs the document around it.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Dino Dash - a purple-maze arcade run: outrun dinosaurs, cats and eagles, mine three relics per level, clear seven levels.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon.svg">
<style>*{box-sizing:border-box}body{margin:0;font:14px/1.5 system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
'''

# Netlify's zip deploy does not infer types, so every path states its own
HEADERS = '''/
  Content-Type: text/html; charset=UTF-8

/index.html
  Content-Type: text/html; charset=UTF-8

/favicon.svg
  Content-Type: image/svg+xml; charset=UTF-8
'''

def main():
    page = (HERE / "index.html").read_text()
    doc = HEAD + page + "\n</body>\n</html>\n"
    doc = doc.replace('</style>\n\n<div class="shell">',
                      '</style>\n</head>\n<body>\n<div class="shell">', 1)
    if "</head>" not in doc:
        raise SystemExit("head was never closed: the <style>/<div> seam moved")
    dist = HERE / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "index.html").write_text(doc)
    (dist / "_headers").write_text(HEADERS)
    print("dist/index.html", len(doc), "bytes")

if __name__ == "__main__":
    main()
