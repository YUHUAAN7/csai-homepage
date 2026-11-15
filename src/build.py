# -*- coding: utf-8 -*-
"""CSAI 홈페이지 빌드.

    python3 src/build.py

src/의 내용으로 사이트 전체(한국어는 루트, 영어 /en/, 중국어 /zh/)를 다시 만든다.
문구를 고치려면 src/pages_home.py · src/pages_sub.py의 L("한국어", "English", "中文")를 고치고 다시 실행한다.
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import core  # noqa: E402
from core import C, LANGS, SITE, HTML_LANG, url_abs  # noqa: E402
import hero_art  # noqa: E402
import pages_home  # noqa: E402
import pages_sub  # noqa: E402

PAGES = [
    ("index", pages_home.home), ("about", pages_sub.about), ("research", pages_sub.research), ("focus", pages_sub.focus),
    ("advisory", pages_sub.advisory), ("academy", pages_sub.academy), ("global", pages_sub.global_), ("news", pages_sub.news),
    ("insight", pages_sub.insight), ("contact", pages_sub.contact), ("policy", pages_sub.policy),
]

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#B8862A"/><stop offset=".55" stop-color="#F6D896"/><stop offset="1" stop-color="#D9A441"/></linearGradient></defs><rect width="64" height="64" rx="12" fill="#071A3A"/><path d="M8 50C12 26 30 10 54 9 36 15 22 28 16 51z" fill="url(#g)"/><text x="36" y="48" text-anchor="middle" font-family="Georgia,serif" font-size="34" font-weight="700" fill="#fff">C</text></svg>'''

NOT_FOUND = '''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>페이지를 찾을 수 없습니다 | CSAI</title><meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css">
<style>.nf{min-height:100vh;display:grid;place-items:center;background:linear-gradient(120deg,#040E26,#0B2452);color:#fff;text-align:center;padding:24px}.nf h1{font-size:clamp(28px,5vw,44px);margin:18px 0 10px}.nf p{color:#D3DEF2;margin-bottom:26px}.nf .row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}</style></head>
<body><main class="nf"><div><div class="eyebrow" style="justify-content:center;color:#E8BC62">CSAI · 404</div>
<h1>페이지를 찾을 수 없습니다</h1><p>Page not found · 找不到该页面</p>
<div class="row"><a class="btn btn-gold" href="/">홈으로</a><a class="btn btn-line" href="/en/index.html">English</a><a class="btn btn-line" href="/zh/index.html">中文</a></div></div></main></body></html>
'''


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    for name in ("site.css", "site.js"):
        shutil.copyfile(os.path.join(HERE, "assets", name), os.path.join(ROOT, "assets", name))
    write("assets/hero.svg", hero_art.build())
    write("assets/favicon.svg", FAVICON)

    count = 0
    for lang in LANGS:
        C.lang, C.search = lang, []
        prefix = "" if lang == "ko" else f"{lang}/"
        for slug, fn in PAGES:
            write(f"{prefix}{slug}.html", fn())
            count += 1
        # 검색 색인: 같은 주소·제목은 한 번만
        seen, idx = set(), []
        for d in C.search:
            key = (d["t"], d["u"])
            if d["t"] and key not in seen:
                seen.add(key)
                idx.append(d)
        write(f"assets/search-{lang}.js", "window.CSAI_SEARCH=" + json.dumps(idx, ensure_ascii=False, separators=(",", ":")) + ";\n")

    urls = []
    for slug, _ in PAGES:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url_abs(l, slug)}"/>' for l in LANGS)
        for lang in LANGS:
            urls.append(f"<url><loc>{url_abs(lang, slug)}</loc>{alts}</url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /src/\n\nSitemap: {SITE}/sitemap.xml\n")
    write("404.html", NOT_FOUND)
    print(f"built {count} pages in {len(LANGS)} languages")


if __name__ == "__main__":
    main()
