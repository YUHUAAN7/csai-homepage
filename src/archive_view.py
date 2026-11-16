# -*- coding: utf-8 -*-
"""누적 자료(src/archive.py · tenday.py · episodes.py)를 화면으로 그리는 함수.

- 모든 목록은 날짜가 늦은 것부터 나온다.
- 길어지면 최근 몇 건만 펼치고 나머지는 '이전 항목 더 보기'로 접는다(지우지 않는다).
- archive_page_items() 는 모든 메뉴의 항목을 한 줄 형식으로 모아 전체 아카이브(archive.html)에 쓴다.
"""
import datetime

from core import C, L, P, e, reg, icon, btn, SUBSCRIBE, ARCHIVE
import archive as A_

MONTHLY_PDF = "https://chinamacro.kr/issues/{id}.pdf"


def T(d):
    """{"ko","en","zh"} 에서 현재 언어 값. 비면 한국어."""
    if not isinstance(d, dict):
        return d or ""
    return d.get(C.lang) or d.get("ko") or ""


def today():
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).date().isoformat()


def newest(items, key="date"):
    return sorted(items, key=lambda x: x.get(key, ""), reverse=True)


def fdate(item, key="date"):
    if item.get("label"):
        return e(item["label"])
    return e(item.get(key, "").replace("-", "."))


def href(link):
    """(href, 외부 여부)"""
    if isinstance(link, (list, tuple)):
        return P(link[0], link[1] if len(link) > 1 else ""), False
    if link == "NAEIL_SEARCH":
        from content import NAEIL_SEARCH
        return NAEIL_SEARCH, True
    return e(link), True


def a(link, text, cls=""):
    h, ext = href(link)
    c = f' class="{cls}"' if cls else ""
    t = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a href="{h}"{c}{t}>{text}</a>'


def fold(shown, hidden, wrap_open, wrap_close, label=None):
    """앞부분은 펼치고 나머지는 접는다."""
    out = wrap_open + "".join(shown) + wrap_close
    if hidden:
        lab = label or L(f"이전 항목 {len(hidden)}건 더 보기", f"{len(hidden)} earlier items", f"查看更早的 {len(hidden)} 条")
        out += f'<details class="more-list"><summary>{lab}</summary>{wrap_open}{"".join(hidden)}{wrap_close}</details>'
    return out


def year_groups(rows, list_open, list_close):
    """rows: [(year, html)] 를 연도별 소제목으로 묶는다(순서 유지)."""
    groups = []
    for y, h in rows:
        if not groups or groups[-1][0] != y:
            groups.append((y, []))
        groups[-1][1].append(h)
    return "".join(f'<div class="yr-group" data-yr="{y}"><h3 class="yr">{y}</h3>{list_open}{"".join(hs)}{list_close}</div>' for y, hs in groups)


# ── 월간 중국경제포커스 ───────────────────────────────────────────
def monthly_title(m):
    if m.get("title"):
        return e(T(m["title"]))
    y, mo = m["id"].split("-")
    return L(f"{y}년 {int(mo)}월호", f"{datetime.date(int(y), int(mo), 1).strftime('%B')} {y}", f"{y}年{int(mo)}月号")


def monthly_pdf(m):
    return m.get("pdf") or MONTHLY_PDF.format(id=m["id"])


def monthly_latest():
    ms = newest(A_.MONTHLY)
    return ms[0] if ms else None


def monthly_list(limit=6):
    rows = []
    for m in newest(A_.MONTHLY):
        no = L(f"제{m['no']}호", f"No. {m['no']}", f"第{m['no']}期") if m.get("no") else ""
        note = T(m.get("label_note"))
        sub = " · ".join(x for x in [no, e(note)] if x)
        pts = ""
        if m.get("points"):
            pts = "<p>" + " / ".join(e(x) for x in T(m["points"])) + "</p>"
        links = a(monthly_pdf(m), "PDF")
        if m.get("web"):
            links += " · " + a(m["web"], L("웹으로 읽기", "Read online", "在线阅读"))
        aid = "monthly-" + m["id"]
        reg(L("월간 「중국경제포커스」 ", "China Economy Focus ", "月刊《中国经济聚焦》") + monthly_title(m), sub, P("focus", aid), L("월간", "Monthly", "月刊"))
        rows.append(f'<li id="{aid}"><time>{fdate(m)}</time><div><h3>{a(monthly_pdf(m), monthly_title(m))}</h3><p>{sub}{" · " if sub else ""}{links}</p>{pts}</div>'
                    f'<span class="kind">{L("월간", "Monthly", "月刊")}</span></li>')
    return fold(rows[:limit], rows[limit:], '<ul class="articles">', "</ul>",
                L("지난 호 더 보기", "More past issues", "查看更多往期"))


# ── 심층보고 ─────────────────────────────────────────────────────
def deepdive_list():
    rows = []
    for d in newest(A_.DEEPDIVE):
        t = e(T(d["title"]))
        reg(L("심층보고 No.", "Deep Dive No. ", "深度报告第") + str(d["no"]) + L(" — ", " — ", "号——") + t, T(d.get("note")), P("focus", d["id"]), "Deep Dive")
        title = a(d["link"], t) if d.get("link") else t
        inq = f' <a href="{P("contact", "general")}">{L("문의하기", "Inquire", "咨询")}</a>' if d.get("inquiry") else ""
        rows.append(f'<li id="{d["id"]}"><time>No. {d["no"]}<br>{fdate(d)}</time><div><h3>{title}</h3><p>{e(T(d.get("note")))}{inq}</p></div>'
                    f'<span class="kind">{L("심층보고", "Deep Dive", "深度报告")}</span></li>')
    return fold(rows[:6], rows[6:], '<ul class="articles">', "</ul>")


# ── CSAI 연구보고서 ──────────────────────────────────────────────
def report_card(r):
    inq = (' · <a href="' + P("contact") + '" style="font-weight:700;color:var(--navy-700)">' + L("전문 문의", "Request the full report", "索取全文") + " →</a>") if r.get("inquiry") else ""
    reg(T(r["title"]), T(r.get("summary")), P("research", r["id"]), L("연구보고서", "Report", "研究报告"))
    return ('<div class="card" id="' + r["id"] + '"><div class="num">' + e(r.get("series", "")) + " · " + fdate(r).replace("-", ".")[:7] + "</div><h3>"
            + e(T(r["title"])) + "</h3>" + ("<p><b>" + e(T(r["subtitle"])) + "</b></p>" if r.get("subtitle") else "")
            + ("<p>" + e(T(r["summary"])) + "</p>" if r.get("summary") else "")
            + ('<p style="font-size:14px;color:var(--ink-2)">' + e(T(r["toc"])) + "</p>" if r.get("toc") else "")
            + '<p style="font-size:13.500px;color:var(--muted)">' + e(T(r.get("meta"))) + inq + "</p></div>")


def reports_block():
    rs = newest(A_.REPORTS)
    if not rs:
        return ""
    cards = [report_card(r) for r in rs]
    out = cards[0]
    if len(cards) > 1:
        out += (f'<details class="more-list"><summary>{L(f"이전 연구보고서 {len(cards) - 1}건", f"{len(cards) - 1} earlier reports", f"更早的研究报告 {len(cards) - 1} 份")}</summary>'
                + '<div style="display:grid;gap:18px;margin-top:14px">' + "".join(cards[1:]) + "</div></details>")
    return out


# ── 칼럼·기고·외부 보고서 ────────────────────────────────────────
def _kinds():
    return {"col": L("칼럼", "Column", "专栏"), "rep": L("연구보고서", "Report", "研究报告"), "pub": L("정기간행물", "Periodical", "期刊")}


def writing_li(w, kinds, ko):
    title = a(w["link"], e(w["title"]))
    title = title.replace("<a ", '<a lang="ko" ', 1)
    more = ""
    if w.get("more"):
        more = " · " + a(w["more"][0], e(T(w["more"][1])))
    reg(w["title"], T(w.get("source")), P("research", "reports"), kinds[w["kind"]])
    when = fdate(w) if w.get("date") else L("연재 중", "Ongoing", "连载中")
    return f'<li data-t="{w["kind"]}"><time>{when}</time><div><h3>{title}</h3><p>{e(T(w.get("source")))}{ko}{more}</p></div><span class="kind">{kinds[w["kind"]]}</span></li>'


def writings(limit=None):
    kinds = _kinds()
    ko = "" if C.lang == "ko" else L("", " · in Korean", " · 韩文")
    rows = [writing_li(A_.WRITINGS_ONGOING, kinds, ko)] + [writing_li(w, kinds, ko) for w in newest(A_.WRITINGS)]
    if limit:
        rows = rows[:limit]
    filt = (f'<div class="filters" role="group" data-for="articles" aria-label="{L("유형", "Type", "类型")}">'
            f'<button type="button" aria-pressed="true" data-f="all">{L("전체", "All", "全部")}</button>'
            + "".join(f'<button type="button" aria-pressed="false" data-f="{k}">{v}</button>' for k, v in kinds.items()) + "</div>")
    return filt + f'<ul class="articles" id="articles">{"".join(rows)}</ul>'


# ── 판단 기록 ───────────────────────────────────────────────────
def _status(s):
    return {
        "open": ("st-open", L("점검 대기", "Pending review", "待检验")),
        "hit": ("st-hit", L("맞음", "Held", "应验")),
        "miss": ("st-miss", L("빗나감", "Missed", "未应验")),
        "partial": ("st-part", L("일부 맞음", "Partly held", "部分应验")),
        "withdrawn": ("st-miss", L("거둠", "Withdrawn", "已撤回")),
    }.get(s or "open")


def judgment_body(j, chips):
    cls, lab = _status(j.get("status"))
    link = (" · " + a(j["link"], L("근거 글 보기", "Read the note", "查看依据"))) if j.get("link") else ""
    res = ""
    if j.get("result"):
        res = f'<p><b>{L("점검 결과", "Outcome", "检验结果")}</b> {e(T(j["result"]))}' + (f' ({e(j["reviewed"].replace("-", "."))})' if j.get("reviewed") else "") + "</p>"
    return (f'<p><b>{chips[0]}</b> {fdate(j)} <span class="st {cls}">{lab}</span></p>'
            f'<p><b>{chips[1]}</b> {e(T(j["text"]))}</p>'
            f'<p><b>{chips[2]}</b> {e(T(j.get("evidence")))}</p>'
            f'<p><b>{chips[3]}</b> {e(T(j.get("invalid")))}</p>'
            f'<p><b>{chips[4]}</b> {e(T(j.get("review")))}{link}</p>' + res)


def judgments_html(chips, show_all=True):
    js = newest(A_.JUDGMENTS)
    if not js:
        return ""
    for j in js:
        reg(T(j["text"]), T(j.get("evidence")), P("insight", j["id"]), L("판단 기록", "Judgment record", "判断记录"))
    out = f'<div class="rec-item" id="{js[0]["id"]}">' + judgment_body(js[0], chips) + "</div>"
    rest = js[1:] if show_all else []
    if rest:
        items = "".join(f'<details class="rec-old" id="{j["id"]}"><summary>{fdate(j)} · {e(T(j["text"]))} <span class="st {_status(j.get("status"))[0]}">{_status(j.get("status"))[1]}</span></summary>'
                        f'<div class="rec-item">{judgment_body(j, chips)}</div></details>' for j in rest)
        out += f'<h4 class="rec-past">{L(f"지난 판단 {len(rest)}건", f"{len(rest)} earlier judgments", f"往期判断 {len(rest)} 条")}</h4>' + items
    hits = sum(1 for j in js if j.get("status") == "hit")
    closed = sum(1 for j in js if j.get("status") in ("hit", "miss", "partial", "withdrawn"))
    out += (f'<p class="rec-score">{L("누적", "To date", "累计")} {len(js)}{L("건", "", "条")} · {L("점검 완료", "reviewed", "已检验")} {closed} · {L("맞음", "held", "应验")} {hits}</p>')
    return out


# ── 기관 소식 ───────────────────────────────────────────────────
def notices_html(limit=None):
    rows = [f'<li><b>{fdate(n)}</b><span>{a(n["link"], e(T(n["title"])))}</span></li>' if n.get("link") else f'<li><b>{fdate(n)}</b><span>{e(T(n["title"]))}</span></li>'
            for n in newest(A_.NOTICES)]
    if limit:
        return '<ul class="hist wide">' + "".join(rows[:limit]) + "</ul>"
    return fold(rows[:8], rows[8:], '<ul class="hist wide">', "</ul>")


# ── 행사 일정 ───────────────────────────────────────────────────
def events_html(full=True):
    t = today()
    up = sorted([x for x in A_.EVENTS if x["date"] >= t], key=lambda x: x["date"])
    past = newest([x for x in A_.EVENTS if x["date"] < t])
    li = lambda x: (f'<li><b>{fdate(x)}</b><span>' + (a(x["link"], e(T(x["title"]))) if x.get("link") else e(T(x["title"])))
                    + (f'<br><small>{e(T(x["result"]))}</small>' if x.get("result") else "") + "</span></li>")
    if not full:
        sel = [x for x in up if x.get("home")] or up[:2]
        return '<ul class="hist wide">' + "".join(li(x) for x in sel[:2]) + "</ul>"
    out = '<ul class="hist wide">' + ("".join(li(x) for x in up) or f'<li><b>—</b><span>{L("확정된 다음 일정은 곧 올립니다.", "Upcoming dates will be posted soon.", "后续日程确定后公布。")}</span></li>') + "</ul>"
    if past:
        out += (f'<details class="more-list"><summary>{L(f"지난 행사 {len(past)}건", f"{len(past)} past events", f"往期活动 {len(past)} 场")}</summary>'
                + '<ul class="hist wide">' + "".join(li(x) for x in past) + "</ul></details>")
    return out


# ── 전체 아카이브 ────────────────────────────────────────────────
def archive_kinds():
    return [("monthly", L("월간 포커스", "Monthly", "月刊")), ("flash", L("열흘 노트", "Ten-Day Note", "旬报")),
            ("deepdive", L("심층보고", "Deep Dive", "深度报告")), ("report", L("연구보고서", "Reports", "研究报告")),
            ("judgment", L("판단 기록", "Judgments", "判断记录")), ("video", L("영상 해설", "Video notes", "视频解读")),
            ("writing", L("칼럼·기고", "Columns", "专栏与评论")), ("news", L("기관 소식", "News", "机构动态")),
            ("event", L("행사", "Events", "活动"))]


def archive_items():
    """[(date, kind, title_html, sub_html)]"""
    from tenday import TENDAY
    from episodes import EPISODES
    out = []
    for m in A_.MONTHLY:
        out.append((m["date"], "monthly", a(monthly_pdf(m), L("월간 「중국경제포커스」 ", "China Economy Focus — ", "月刊《中国经济聚焦》") + monthly_title(m)), e(T(m.get("label_note")))))
    for n in TENDAY:
        aid = n.get("anchor") or "note-" + n["id"]
        out.append((n.get("asof") or n["id"], "flash", a(["focus", aid], e(T(n["title"]))), e(T(n["period"]))))
    for d in A_.DEEPDIVE:
        out.append((d["date"], "deepdive", a(["focus", d["id"]], f"No. {d['no']} · " + e(T(d["title"]))), e(T(d.get("note")))))
    for r in A_.REPORTS:
        out.append((r["date"], "report", a(["research", r["id"]], e(T(r["title"]))), e(T(r.get("subtitle")))))
    for j in A_.JUDGMENTS:
        out.append((j["date"], "judgment", a(["insight", j["id"]], e(T(j["text"]))), _status(j.get("status"))[1]))
    for ep in EPISODES:
        out.append((ep["date"], "video", a(ep.get("youtube") or ["videos"], e(ep["title"])), ""))
    for w in A_.WRITINGS:
        out.append((w["date"], "writing", a(w["link"], e(w["title"])), e(T(w.get("source")))))
    for n in A_.NOTICES:
        out.append((n["date"], "news", a(n["link"], e(T(n["title"]))) if n.get("link") else e(T(n["title"])), ""))
    t = today()
    for x in A_.EVENTS:
        tag = L("예정", "Upcoming", "即将举行") if x["date"] >= t else L("지난 행사", "Past", "已举行")
        out.append((x["date"], "event", e(T(x["title"])), tag, x.get("label")))
    return out


def archive_page_body():
    kinds = dict(archive_kinds())
    items = sorted(archive_items(), key=lambda x: x[0], reverse=True)
    counts = {}
    for it in items:
        counts[it[1]] = counts.get(it[1], 0) + 1
    filt = (f'<div class="filters" role="group" data-for="archive-list" aria-label="{L("종류", "Type", "类型")}">'
            f'<button type="button" aria-pressed="true" data-f="all">{L("전체", "All", "全部")} {len(items)}</button>'
            + "".join(f'<button type="button" aria-pressed="false" data-f="{k}">{v} {counts[k]}</button>' for k, v in archive_kinds() if counts.get(k))
            + "</div>")
    rows = []
    for it in items:
        d, k, title, sub = it[:4]
        lab = it[4] if len(it) > 4 and it[4] else d.replace("-", ".")
        rows.append((d[:4], f'<li data-t="{k}"><time>{e(lab)}</time><div><h3>{title}</h3>' + (f"<p>{sub}</p>" if sub else "") + f'</div><span class="kind">{kinds[k]}</span></li>'))
    return filt + '<div id="archive-list">' + year_groups(rows, '<ul class="articles">', "</ul>") + "</div>"
