# -*- coding: utf-8 -*-
"""CSAI 홈페이지 빌드 공통 모듈: 언어 선택, 링크, 아이콘, 머리말·꼬리말."""
import html
import re

SITE = "https://www.csai.re.kr"
LANGS = ["ko", "en", "zh"]
HTML_LANG = {"ko": "ko", "en": "en", "zh": "zh-Hans"}
MAIL = "contact@chinamacro.kr"
# 방문 통계(Cloudflare Web Analytics, 쿠키 없음). 원장이 가입해 받은 토큰을 넣으면 모든 페이지에 켜진다. 비어 있으면 꺼짐.
ANALYTICS_TOKEN = "e774c0e87a9d471b81018d67e21732a6"
SUBSCRIBE = "https://page.stibee.com/subscriptions/522211"
ARCHIVE = "https://chinamacro.kr"
YOUTUBE = "https://www.youtube.com/@anyuhuatv"
BLOG = "https://blog.naver.com/anyuhuatv"
PODCAST = "https://www.podbbang.com/channels/1791158"
FACEBOOK = "https://www.facebook.com/yuhua.an.1"


def _asset_ver():
    import hashlib, os
    h = hashlib.md5()
    for n in ("site.css", "site.js"):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", n), "rb") as f:
            h.update(f.read())
    return h.hexdigest()[:8]


ASSET_VER = _asset_ver()


class Ctx:
    lang = "ko"
    slug = "index"
    search = []


C = Ctx()


def L(ko, en=None, zh=None):
    """현재 언어의 문구를 고른다. en/zh를 비우면 한국어 원문을 그대로 쓴다."""
    if C.lang == "en":
        return ko if en is None else en
    if C.lang == "zh":
        return (ko if en is None else en) if zh is None else zh
    return ko


def e(s):
    return html.escape(str(s), quote=True)


def A(path):
    """자산 경로(언어 폴더에서는 한 단계 위)."""
    return ("" if C.lang == "ko" else "../") + path


def P(slug, anchor=""):
    """같은 언어 안의 페이지 링크."""
    return f"{slug}.html" + (f"#{anchor}" if anchor else "")


def sub_href(slug, anchor):
    """하위 메뉴 링크. 뉴스·자료의 '연구소장's Insight'는 전용 페이지의 메시지 화면으로 보낸다."""
    if slug == "news" and anchor == "insight":
        return P("insight", "insight")
    if slug == "focus" and anchor == "notes":
        return P("videos")
    if slug == "news" and anchor == "archive":
        return P("archive")
    return P(slug, anchor)


def lang_href(target, slug):
    f = f"{slug}.html"
    if C.lang == "ko":
        return f if target == "ko" else f"{target}/{f}"
    if target == "ko":
        return f"../{f}"
    return f if target == C.lang else f"../{target}/{f}"


def url_abs(lang, slug):
    base = SITE + ("/" if lang == "ko" else f"/{lang}/")
    return base + ("" if slug == "index" else f"{slug}.html")


def reg(title, text, url, cat=""):
    """사이트 검색용 색인에 한 줄 추가."""
    strip = lambda s: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()
    C.search.append({"t": strip(title), "s": strip(text)[:160], "u": url, "c": strip(cat)})


# ── 아이콘(선 아이콘, currentColor) ─────────────────────────────
_I = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "chart": '<path d="M4 20h16"/><rect x="5" y="12" width="3" height="6"/><rect x="10.5" y="8" width="3" height="10"/><rect x="16" y="4" width="3" height="14"/><path d="M4 9l5-4 4 2 6-5"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.4 2.7-6 6-6s6 2.6 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M16 14.2c2.9.3 5 2.6 5 5.8"/>',
    "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11.5V16c0 1.4 2.7 3 6 3s6-1.6 6-3v-4.5"/><path d="M22 9v6"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.8 3 2.8 15 0 18M12 3c-2.8 3-2.8 15 0 18"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
    "bolt": '<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "play": '<circle cx="12" cy="12" r="9"/><path d="M10 8.5v7l6-3.5z"/>',
    "scale": '<path d="M12 4v16M6 20h12M5 8h14"/><path d="M5 8l-3 6c0 1.6 1.4 2.6 3 2.6S8 15.600 8 14zM19 8l-3 6c0 1.600 1.400 2.600 3 2.600s3-1 3-2.600z"/>',
    "link": '<path d="M10 14a4 4 0 005.700 0l3-3a4 4 0 00-5.700-5.700l-1 1"/><path d="M14 10a4 4 0 00-5.700 0l-3 3a4 4 0 005.700 5.700l1-1"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.500 8.500l-2 5-5 2 2-5z"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.500-3.400 7.800-8 9-4.600-1.200-8-4.500-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "factory": '<path d="M3 21V10l6 4v-4l6 4V5h4v16z"/><path d="M7 17h2M12 17h2M17 17h0"/>',
    "news": '<rect x="3" y="4" width="15" height="16" rx="1.500"/><path d="M18 8h3v10a2 2 0 01-2 2M7 8h7M7 12h7M7 16h4"/>',
    "pin": '<path d="M12 21s7-6.200 7-11.500A7 7 0 005 9.500C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500"/>',
    "ext": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 01-1 1H5a1 1 0 01-1-1V7a1 1 0 011-1h5"/>',
}


def icon(name, size=20, cls=""):
    return (f'<svg class="ico {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.600" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>')


def logo(uid="a"):
    return (f'<svg class="logo" viewBox="0 0 150 48" role="img" aria-label="CSAI">'
            f'<defs><linearGradient id="lg{uid}" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#B8862A"/>'
            f'<stop offset=".55" stop-color="#F6D896"/><stop offset="1" stop-color="#D9A441"/></linearGradient></defs>'
            f'<path d="M2 40C7 19 26 5 52 4 33 9 17 21 9 41z" fill="url(#lg{uid})"/>'
            f'<text x="27" y="38" font-family="\'Noto Serif KR\',\'Noto Serif CJK KR\',Georgia,serif" font-size="33" '
            f'font-weight="700" letter-spacing=".5" fill="#fff">CSAI</text></svg>')


def nav():
    return [
        ("about", L("연구원 소개", "About", "关于CSAI"), L("연구원 소개", "About CSAI", "关于CSAI"), [
            ("overview", L("개요", "Overview", "概况")), ("vision", L("비전·미션", "Vision & Mission", "愿景与使命")),
            ("leadership", L("리더십", "Leadership", "领导层")), ("organization", L("조직", "Organization", "组织架构")),
            ("contact", L("연락처", "Contact", "联系方式"))]),
        ("research", L("연구·분석", "Research", "研究分析"), L("연구·분석", "Research", "研究分析"), [
            ("framework", L("분석 프레임", "Framework", "分析框架")), ("macro", L("거시경제", "Macroeconomics", "宏观经济")),
            ("policy", L("정책·규제", "Policy & Regulation", "政策与监管")),
            ("industry", L("산업·공급망", "Industry & Supply Chain", "产业与供应链")),
            ("reports", L("연구보고서", "Research Reports", "研究报告"))]),
        ("focus", L("거시경제연구소", "China Economy Focus", "宏观经济研究所"),
         L("거시경제연구소", "China Economy Focus", "宏观经济研究所"), [
            ("latest", L("최신", "Latest", "最新")), ("flash", L("Flash · 열흘 노트", "Flash · Ten-Day Note", "Flash · 旬报")),
            ("monthly", L("월간 중국경제포커스", "Monthly", "月刊《中国经济聚焦》")),
            ("deepdive", L("심층보고", "Deep Dive", "深度报告")),
            ("video", L("영상·뉴스레터", "Video & Newsletter", "视频与通讯")),
            ("notes", L("영상 해설", "Video notes", "视频解读"))]),
        ("advisory", L("기업 자문", "Advisory", "企业咨询"), L("기업 자문·컨설팅", "Business Advisory & Consulting", "企业咨询与顾问"), [
            ("brief", L("CEO China Brief", "CEO China Brief", "CEO China Brief")),
            ("services", L("기업 자문", "Advisory", "企业咨询")), ("consulting", L("기업 컨설팅", "Consulting", "企业顾问项目")),
            ("themes", L("자문 주제", "Case Themes", "咨询主题")), ("inquiry", L("기업 문의", "Inquiry", "企业咨询联系"))]),
        ("academy", L("교육·아카데미", "Academy", "教育学院"), L("교육·아카데미", "Academy", "教育学院"), [
            ("programs", L("프로그램", "Programs", "课程项目")), ("executive", L("임원 과정", "Executive Education", "高管课程")),
            ("corporate", L("기업 맞춤 교육", "Corporate Training", "企业定制培训")),
            ("inquiry", L("교육 문의", "Inquiry", "培训咨询"))]),
        ("global", L("글로벌 협력", "Global", "全球合作"), L("글로벌 협력", "Global Network", "全球合作"), [
            ("partners", L("협력기관", "Partners", "合作机构")), ("experts", L("전문가", "Experts", "专家")),
            ("events", L("포럼·행사", "Events & Forums", "论坛与活动")),
            ("inquiry", L("협력 문의", "Cooperation Inquiry", "合作咨询"))]),
        ("news", L("뉴스·자료", "News & Insights", "新闻与资料"), L("뉴스·자료", "News & Insights", "新闻与资料"), [
            ("news", L("기관 소식", "News", "机构动态")), ("media", L("언론·미디어", "Media", "媒体")),
            ("insight", L("연구소장's Insight", "Director's Insight", "所长观点")),
            ("publications", L("자료실", "Publications", "资料室")),
            ("archive", L("전체 아카이브", "Archive", "全部档案"))]),
    ]


def header(active):
    items, mob = [], []
    for slug, short, full, subs in nav():
        cur = ' aria-current="page"' if slug == active else ""
        drop = "".join(f'<a href="{sub_href(slug, a)}">{e(t)}</a>' for a, t in subs)
        items.append(f'<div class="nav-item"><a class="nav-top" href="{P(slug)}"{cur}>{e(short)}{icon("chev", 14)}</a>'
                     f'<div class="drop">{drop}</div></div>')
        mob.append(f'<div class="mnav-group"><a class="mnav-top" href="{P(slug)}">{e(full)}</a><div class="mnav-sub">{drop}</div></div>')
    langs = "".join(
        f'<a href="{lang_href(l, C.slug)}" lang="{HTML_LANG[l]}"{" aria-current=\"true\"" if l == C.lang else ""}>{t}</a>'
        for l, t in (("ko", "KO"), ("en", "EN"), ("zh", "中文")))
    return f'''<a class="skip" href="#main">{L("본문 바로가기", "Skip to content", "跳到正文")}</a>
<header class="hdr" id="hdr">
  <div class="wrap hdr-in">
    <a class="brand" href="{P("index")}" aria-label="CSAI {L("홈", "home", "首页")}">{logo("h")}</a>
    <nav class="nav" aria-label="{L("주 메뉴", "Main menu", "主菜单")}">{"".join(items)}</nav>
    <div class="tools">
      <button class="icon-btn" type="button" data-search-open aria-label="{L("검색", "Search", "搜索")}">{icon("search", 20)}</button>
      <div class="langs" aria-label="Language">{langs}</div>
      <a class="btn btn-gold btn-sm" href="{P("contact")}">Contact {icon("arrow", 16)}</a>
      <button class="icon-btn burger" type="button" id="burger" aria-expanded="false" aria-controls="mnav" aria-label="{L("메뉴", "Menu", "菜单")}">{icon("menu", 24)}</button>
    </div>
  </div>
  <div class="mnav" id="mnav" hidden>
    <div class="wrap">
      {"".join(mob)}
      <div class="mnav-foot"><div class="langs">{langs}</div><a class="btn btn-gold" href="{P("contact")}">Contact {icon("arrow", 16)}</a></div>
    </div>
  </div>
</header>'''


def footer():
    cols = []
    for slug, short, full, subs in nav():
        links = "".join(f'<li><a href="{sub_href(slug, a)}">{e(t)}</a></li>' for a, t in subs)
        cols.append(f'<div><h3><a href="{P(slug)}">{e(full)}</a></h3><ul>{links}</ul></div>')
    return f'''<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <div class="ftr-brand">
        {logo("f")}
        <p class="ftr-slogan">Insight without Borders</p>
        <p class="ftr-line">{L("중국의 정책을 한국의 결정으로 번역한다.", "Translating China into Korean decisions.", "把中国的政策，翻译成韩国的决策。")}</p>
        <p class="ftr-line">{L("중국을 데이터와 원칙으로 읽습니다.", "Reading China through data and principles.", "以数据与原则解读中国。")}</p>
        <div class="ftr-mail"><code id="mail">{MAIL}</code><button type="button" class="copy" data-copy="#mail" data-done="{L("복사됨", "Copied", "已复制")}">{L("복사", "Copy", "复制")}</button></div>
        <p class="ftr-note">{L("강연·자문·인터뷰 요청", "Speaking, advisory and interview requests", "演讲·咨询·采访邀请")}</p>
      </div>
      <nav class="ftr-map" aria-label="{L("사이트맵", "Sitemap", "网站地图")}">{"".join(cols)}</nav>
    </div>
    <div class="ftr-chan">
      <a href="{SUBSCRIBE}" target="_blank" rel="noopener">{L("뉴스레터 구독", "Newsletter", "订阅通讯")}</a>
      <a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a>
      <a href="{BLOG}" target="_blank" rel="noopener">{L("네이버 블로그", "Naver Blog", "Naver 博客")}</a>
      <a href="{PODCAST}" target="_blank" rel="noopener">{L("팟캐스트", "Podcast", "播客")}</a>
      <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a>
      <a href="{ARCHIVE}" target="_blank" rel="noopener">chinamacro.kr</a>
    </div>
    <div class="ftr-legal">
      <span>© 2026 CSAI · {L("주식회사 중국증권행정연구원 (사업자 425-81-00149)", "China Securities Administration Institute Co., Ltd. (Business reg. no. 425-81-00149)", "株式会社中国证券行政研究院（营业执照号 425-81-00149）")} · www.csai.re.kr</span>
      <span class="ftr-pol"><a href="{P("policy", "privacy")}">{L("개인정보 처리방침", "Privacy", "隐私政策")}</a><a href="{P("policy", "terms")}">{L("이용약관", "Terms", "使用条款")}</a><a href="{P("policy", "disclaimer")}">{L("면책·저작권", "Disclaimer", "免责与版权")}</a></span>
    </div>
    <p class="ftr-disc">{L("본 사이트의 내용은 정보 제공을 위한 것이며, 특정 종목·상품의 매수·매도 권유나 투자 자문이 아닙니다.", "Content on this site is for information only. It is not investment advice or a recommendation to buy or sell any security or product.", "本网站内容仅供参考，不构成任何证券或产品的买卖建议或投资咨询。")}</p>
  </div>
</footer>
<div class="sov" id="sov" hidden>
  <div class="sov-box" role="dialog" aria-modal="true" aria-label="{L("사이트 검색", "Site search", "站内搜索")}">
    <div class="sov-bar">{icon("search", 20)}<input id="sq" type="search" placeholder="{L("검색어를 입력하세요", "Search this site", "请输入关键词")}" autocomplete="off" data-idx="{A("assets/search-" + C.lang + ".js")}"><button class="icon-btn" type="button" data-search-close aria-label="{L("닫기", "Close", "关闭")}">{icon("close", 20)}</button></div>
    <ul class="sov-res" id="sres" data-empty="{L("검색 결과가 없습니다. 다른 낱말로 찾아보세요.", "No results. Try another word.", "没有找到结果，请换个关键词。")}" data-hint="{L("메뉴·보고서·콘텐츠 제목에서 찾습니다.", "Searches menus, reports and content titles.", "在菜单、报告和内容标题中搜索。")}"></ul>
  </div>
</div>'''


def page(slug, title, desc, body, active=""):
    full_title = "CSAI" if slug == "index" else f"{title} | CSAI"
    if slug == "index":
        full_title = L("CSAI — 중국의 정책을 한국의 결정으로 번역한다", "CSAI — Translating China into Korean decisions", "CSAI — 把中国的政策翻译成韩国的决策")
    alts = "".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{url_abs(l, slug)}">' for l in LANGS)
    zh_font = "&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@600;700" if C.lang == "zh" else ""
    return f'''<!doctype html>
<html lang="{HTML_LANG[C.lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url_abs(C.lang, slug)}">
{alts}<link rel="alternate" hreflang="x-default" href="{url_abs("ko", slug)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="CSAI">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url_abs(C.lang, slug)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#071A3A">
<link rel="icon" href="{A("assets/favicon.svg")}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@500;600;700&family=Noto+Sans+KR:wght@400;500;700{zh_font}&display=swap">
<link rel="stylesheet" href="{A("assets/site.css")}?v={ASSET_VER}">
</head>
<body class="p-{slug}">
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="{A("assets/site.js")}?v={ASSET_VER}" defer></script>{analytics_tag()}
</body>
</html>
'''


# ── 본문 조각 ────────────────────────────────────────────────
def btn(label, href, kind="gold", ext=False, extra=""):
    t = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="btn btn-{kind} {extra}" href="{href}"{t}>{label} {icon("arrow", 16)}</a>'


def more(label, href, ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="more" href="{href}"{t}>{label} {icon("arrow", 16)}</a>'


def soon(text=""):
    tag = L("준비 중", "Coming soon", "筹备中")
    return f'<div class="soon"><span class="tag-soon">{tag}</span><p>{text}</p></div>'


def sec(sid, eyebrow, title, lede, body, cls=""):
    reg(title, lede, P(C.slug, sid), eyebrow)
    p = f"<p>{lede}</p>" if lede else ""
    return (f'<section class="sec {cls}" id="{sid}"><div class="wrap"><div class="sec-head"><div class="eyebrow">{eyebrow}</div>'
            f'<h2>{title}</h2>{p}</div>{body}</div></section>')


def page_hero(slug, eyebrow, title, lede, subs=None):
    if subs is None:
        subs = next((s[3] for s in nav() if s[0] == slug), [])
    tabs = "".join(f'<a href="{sub_href(slug, a) if (slug, a) in (("news", "insight"), ("focus", "notes"), ("news", "archive")) else "#" + a}">{e(t)}</a>' for a, t in subs)
    sub = f'<div class="subnav" id="subnav"><div class="wrap"><div class="subnav-in">{tabs}</div></div></div>' if tabs else ""
    reg(title, lede, P(slug), "CSAI")
    return f'''<section class="phero">
  <div class="wrap">
    <div class="crumbs"><a href="{P("index")}">CSAI</a><span>/</span><span>{title}</span></div>
    <div class="eyebrow">{eyebrow}</div>
    <h1>{title}</h1>
    <p class="phero-lede">{lede}</p>
  </div>
</section>{sub}'''


def analytics_tag():
    if not ANALYTICS_TOKEN:
        return ""
    return ('\n<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{"token": "' + ANALYTICS_TOKEN + '"}\'></script>')


def cta_band(title, text, label, href, flush=False, ext=False):
    st = ' style="margin-top:0"' if flush else ""
    return f'<div class="cta-box"{st}><div><h3>{title}</h3><p>{text}</p></div>{btn(label, href, "gold", ext=ext)}</div>'
