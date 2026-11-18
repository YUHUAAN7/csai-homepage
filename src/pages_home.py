# -*- coding: utf-8 -*-
"""메인 페이지(기획안 Ⅵ의 10개 섹션)와 여러 페이지가 함께 쓰는 콘텐츠 조각."""
from core import *
from content import *

# ── 여러 페이지에서 함께 쓰는 내용 ─────────────────────────────






















# ── 메인 페이지 ────────────────────────────────────────────────


def mini_frame_art():
    return ('<svg class="q-art" viewBox="0 0 210 150" aria-hidden="true"><g fill="none" stroke="#2F6FD6" stroke-width="1.500" opacity=".55">'
            '<path d="M50 36h44M132 36h22v26M154 92v22h-22M94 114H72"/><path d="M50 114V78" stroke-dasharray="3 4"/></g>'
            '<g fill="#fff" stroke="#12336F" stroke-width="1.500"><rect x="10" y="22" width="40" height="28" rx="4"/><rect x="94" y="22" width="40" height="28" rx="4"/>'
            '<rect x="134" y="62" width="40" height="30" rx="4"/><rect x="92" y="100" width="40" height="28" rx="4"/></g>'
            '<rect x="10" y="100" width="62" height="28" rx="4" fill="#D9A441"/><g fill="#12336F"><circle cx="30" cy="36" r="4"/><circle cx="114" cy="36" r="4"/>'
            '<circle cx="154" cy="77" r="4"/><circle cx="112" cy="114" r="4"/></g><circle cx="41" cy="114" r="4" fill="#fff"/></svg>')


def mission_art():
    globe = ('<svg class="mission-globe" viewBox="0 0 400 400" aria-hidden="true"><g fill="none" stroke="#7FB0F5" stroke-width="2" stroke-dasharray="1 8" stroke-linecap="round">'
             '<circle cx="200" cy="200" r="190"/><ellipse cx="200" cy="200" rx="60" ry="190"/><ellipse cx="200" cy="200" rx="125" ry="190"/>'
             '<ellipse cx="200" cy="200" rx="190" ry="34"/><ellipse cx="200" cy="110" rx="165" ry="28"/><ellipse cx="200" cy="290" rx="165" ry="28"/></g></svg>')
    swoosh = ('<svg class="mission-swoosh" viewBox="0 0 320 200" preserveAspectRatio="xMaxYMax meet" aria-hidden="true"><defs><linearGradient id="sw" x1="0" y1="1" x2="1" y2="0">'
              '<stop offset="0" stop-color="#A9781F" stop-opacity="0"/><stop offset=".5" stop-color="#F6D896"/><stop offset="1" stop-color="#D9A441"/></linearGradient></defs>'
              '<path d="M40 200C150 170 250 110 320 20v14C260 120 160 180 60 200z" fill="url(#sw)"/></svg>')
    return globe + swoosh


def home():
    C.slug = "index"
    slides = [
        ("INSIGHT WITHOUT BORDERS",
         L("중국의 정책을<br><em>한국의 결정</em>으로 번역한다.", "Translating China's policy<br>into <em>Korean decisions</em>.", "把中国的政策，<br>翻译成<em>韩国的决策</em>。"),
         L("CSAI는 중국의 경제·정책을 깊이 분석하고, 한국 기업과 기관의 전략적 의사결정을 지원합니다.",
           "CSAI analyses China's economy and policy in depth and supports the strategic decisions of Korean companies and institutions.",
           "CSAI深入分析中国经济与政策，为韩国企业和机构的战略决策提供支持。"),
         btn(L("연구보고서 보기", "Explore Research", "查看研究报告"), P("research", "reports")) + btn(L("더 알아보기", "About CSAI", "了解更多"), P("about"), "line")),
        (message()["eyebrow"] + L(" ", " · ", " ") + message()["name"], message()["title"], message()["lede"],
         btn(message()["cta1"], "#principles") + btn(message()["cta2"], "#focus", "line")),
        (L("거시경제연구소 · 월간 중국경제포커스", "China Economy Focus · Monthly", "宏观经济研究所 · 月刊《中国经济聚焦》"),
         L("중국의 한 달을<br><em>한 권</em>으로 읽습니다.", "One month of China,<br>in <em>one issue</em>.", "一个月的中国，<br>浓缩成<em>一期</em>。"),
         L("매월 둘째 주 화요일 아침, 중국 거시·산업·공급망의 한 달을 한 권으로 정리해 보내드립니다. 기사마다 한국 시사점을 붙입니다.",
           "Every second Tuesday: China's macro, industry and supply chains in one issue, each article ending with what it means for Korea.",
           "每月第二个星期二，汇总中国宏观、产业与供应链动态，每篇附韩国启示。"),
         btn(L("무료 구독하기", "Subscribe free", "免费订阅"), SUBSCRIBE, ext=True) + btn(L("거시경제연구소 보기", "Explore China Economy Focus", "进入宏观经济研究所"), P("focus"), "line")),
    ]
    s_html = "".join(
        f'<div class="slide{" on" if i == 0 else ""}"><div class="eyebrow">{eb}</div><{"h1" if i == 0 else "h2"} class="hero-h">{h}</{"h1" if i == 0 else "h2"}>'
        f'<p class="lede">{p}</p><div class="cta">{c}</div></div>' for i, (eb, h, p, c) in enumerate(slides))

    hero = f'''<section class="hero" aria-label="{L("메인 비주얼", "Main visual", "主视觉")}">
  <div class="hero-art" aria-hidden="true"></div>
  <div class="wrap">
    {s_html}
    <div class="hero-ctrl"><span id="slideNo">01 / 03</span>
      <button type="button" class="prev" data-slide="prev" aria-label="{L("이전", "Previous", "上一张")}">{icon("arrow", 18)}</button>
      <button type="button" data-slide="next" aria-label="{L("다음", "Next", "下一张")}">{icon("arrow", 18)}</button>
      <span class="hero-bar"><i></i></span></div>
  </div>
</section>'''

    svc = [("chart", L("중국경제 연구", "China research", "中国经济研究"), P("research")),
           ("users", L("기업 자문", "Business advisory", "企业咨询"), P("advisory")),
           ("cap", L("교육·아카데미", "Academy", "教育学院"), P("academy")),
           ("globe", L("글로벌 협력", "Global network", "全球合作"), P("global"))]
    quick = f'''<section class="quick" aria-label="{L("바로가기", "Quick links", "快捷入口")}">
  <div class="wrap quick-grid">
    <div class="qcard"><div class="ql">RESEARCH</div>
      <h3>{L("중국 경제는 어떻게 작동하는가", "How China's economy works", "中国经济如何运行")}</h3>
      <p>{L("정책에서 금융·지방재정·산업·대외부문까지, 신호와 돈이 흐르는 길을 따라 읽는 분석 프레임", "An analytical frame that follows signals and money from policy through finance, local budgets, industry and the external sector.", "沿着信号与资金的流向，从政策到金融、地方财政、产业与对外部门的分析框架。")}</p>
      {more(L("자세히 보기", "Read more", "了解详情"), "#machine")}{mini_frame_art()}</div>
    <div class="qcard has-mag"><div class="ql">{L("거시경제연구소", "CHINA ECONOMY FOCUS", "宏观经济研究所")}</div>
      <h3>{L("월간 「중국경제포커스」<br>2026년 11월호", "Monthly China Economy Focus<br>November 2026", "月刊《中国经济聚焦》<br>2026年11月号")}</h3>
      <p>{L("중국 경제의 핵심 이슈와 한국 시사점을 담았습니다.", "Key issues in China's economy and what they mean for Korea.", "聚焦中国经济核心议题及其对韩国的启示。")}</p>
      {more(L("구독 신청", "Subscribe", "订阅"), SUBSCRIBE, ext=True)}
      <div class="mag" aria-hidden="true"><small>CSAI</small><b>{L("중국경제<br>포커스", "China<br>Economy<br>Focus", "中国经济<br>聚焦")}</b><span>2026. 11</span></div></div>
    <div class="qcard"><div class="ql">OUR SERVICES</div>
      <div class="svc-mini">{"".join(f'<a href="{h}">{icon(ic, 26)}<span>{t}</span>{icon("arrow", 15)}</a>' for ic, t, h in svc)}</div></div>
  </div>
</section>'''

    mission = f'''<section class="mission" id="about" aria-label="About CSAI">
  {mission_art()}
  <div class="wrap">
    <div><small>{L("CSAI의 미션", "Our mission", "CSAI的使命")}</small>
      <p class="say">{L("중국을 가장 깊이 읽는 거시경제 통찰로,<br>한국과 세계의 기업·기관이 더 <b>나은 결정</b>을 내리도록 돕는다.",
                         "With the deepest macroeconomic reading of China,<br>we help companies and institutions in Korea and the world make <b>better decisions</b>.",
                         "以对中国最深入的宏观经济洞察，<br>帮助韩国与世界的企业和机构做出<b>更好的决策</b>。")}</p></div>
    <div class="rule" aria-hidden="true"></div>
    <div class="sig"><div><strong>CSAI</strong><span>Insight without Borders</span></div>{btn(L("CSAI 소개 보기", "About CSAI", "关于CSAI"), P("about"), "line")}</div>
  </div>
</section>'''
    reg(L("CSAI의 미션", "Our mission", "CSAI的使命"), L("중국을 가장 깊이 읽는 거시경제 통찰로, 한국과 세계의 기업·기관이 더 나은 결정을 내리도록 돕는다.", "We help companies and institutions make better decisions.", "帮助企业和机构做出更好的决策。"), P("about", "vision"), "About CSAI")

    about = sec("values", "ABOUT CSAI",
                L("판단·데이터·접근을 쌓아 가는 연구기관", "A research institute built on judgment, data and access", "积累判断、数据与渠道的研究机构"),
                L("CSAI는 중국의 거시경제와 정책을 분석해 한국 기업·기관의 의사결정으로 연결합니다. 정책을 지켜보는 데서 그치지 않고, 판단의 기록과 데이터, 현지 맥락에 대한 이해를 쌓아 갑니다.",
                  "CSAI analyses China's macro economy and policy and connects it to the decisions of Korean companies and institutions. Beyond monitoring policy, we build up a record of judgments, data and an understanding of local context.",
                  "CSAI分析中国宏观经济与政策，并将其与韩国企业和机构的决策相连接。我们不止于跟踪政策，更持续积累判断记录、数据以及对当地语境的理解。"),
                f'<h3 class="sub-h" style="margin:0 0 22px">{boundary_title()}</h3>{boundary_block(full=False)}'
                f'<h3 class="sub-h" style="margin-bottom:22px">{L("핵심가치", "Core values", "核心价值")}</h3>{core_values_cards(evidence=False)}'
                f'<h3 class="sub-h" style="margin-bottom:22px">{L("차별화 자산: 판단 · 데이터 · 접근", "What sets us apart: judgment, data, access", "差异化资产：判断 · 数据 · 渠道")}</h3>{asset_cards()}'
                f'<div class="sec-foot">{more(L("CSAI 소개 보기", "About CSAI", "关于CSAI"), P("about"))}</div>')

    areas = "".join(
        f'<a class="card" href="{P("research", a)}"><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3><p>{d}</p><div class="tags">{"".join(f"<span>{x}</span>" for x in tg[:4])}</div></a>'
        for a, ic, t, d, tg in research_areas())
    research = sec("research", "RESEARCH", L("무엇을 연구하는가", "What we study", "研究领域"),
                   L("거시경제, 정책·규제, 산업·공급망 세 축으로 중국을 읽고, 모든 분석을 한국의 질문으로 마무리합니다.",
                     "We read China along three axes — macroeconomics, policy & regulation, industry & supply chains — and close every analysis with the Korean question.",
                     "从宏观经济、政策与监管、产业与供应链三条主线解读中国，所有分析最终回到韩国的问题。"),
                   f'<div class="g3">{areas}</div>{future_finance(compact=True)}<div class="sec-foot">{btn(L("연구보고서 전체 보기", "View all research", "查看全部研究"), P("research", "reports"), "navy")}{more(L("연구·칼럼 보기", "Research & commentary", "研究与评论"), "#columns")}</div>',
                   "alt")
    machine = sec("machine", "FRAMEWORK", L("중국 경제는 어떻게 작동하는가", "How China's economy works", "中国经济如何运行"), machine_lede(), machine_block())
    columns = sec("columns", "RESEARCH & COMMENTARY", L("연구·칼럼", "Research & Commentary", "研究与评论"), columns_lede(),
                  articles() + columns_note() + f'<div class="sec-foot">{more(L("연구·분석 전체 보기", "All research", "查看全部研究"), P("research"))}</div>', "alt")

    focus = sec("focus", L("거시경제연구소", "China Economy Focus", "宏观经济研究所"),
                L("중국경제를 꾸준히 읽는 콘텐츠 채널", "A steady channel for reading China's economy", "持续解读中国经济的内容频道"),
                L("거시경제연구소는 CSAI의 콘텐츠 채널입니다. 월간 「중국경제포커스」를 중심으로 열흘 노트·심층보고·영상을 차례로 넓혀 갑니다.",
                  "China Economy Focus is the content channel of CSAI's Macroeconomic Institute. It is built around the monthly issue and is expanding into the Ten-Day Note, deep dives and video.",
                  "宏观经济研究所是CSAI的内容频道，以月刊《中国经济聚焦》为核心，逐步拓展旬报、深度报告与视频。"),
                f'<div class="split"><div>{issue_card()}</div><div>{content_types()}{pillars()}{signal_box()}</div></div>'
                f'<div class="sec-foot">{more(L("거시경제연구소 전체 보기", "Explore China Economy Focus", "进入宏观经济研究所"), P("focus"))}</div>')

    reg(L("연구소장's Insight", "Director's Insight", "所长观点"), L("중국을 읽는 원칙과 판단 기록", "Principles and the judgment record", "解读中国的原则与判断记录"), P("insight"), "Insight")
    insight = message_section("#principles", "#focus")
    princ = sec("principles", "PRINCIPLES", L("중국을 읽는 원칙", "Principles for reading China", "解读中国的原则"), principles_lede(),
                principles_grid() + record_box(light=True) + f'<div class="sec-foot">{more(L("연구소장 Insight 전체 보기", "All of Director\'s Insight", "查看全部所长观点"), P("insight"))}</div>', "alt")
    bio = "".join(f"<p>{x}</p>" for x in bio_paragraphs())
    books = sec("books", "BOOKS", L("대표저서", "Selected books", "代表著作"), books_lede(), books_html())
    director = sec("director", "LEADERSHIP", message()["name"], "",
                   f'<div class="about2"><div class="bio">{bio}</div>{timeline()}</div>'
                   f'<div class="sec-foot">{more(L("원장 소개 전체 보기", "Leadership", "院长简介"), P("about", "leadership"))}</div>', "alt")

    sv = "".join(f'<div class="card"><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in services())
    advisory = sec("advisory", "BUSINESS ADVISORY", L("중국 관련 의사결정을 지원합니다", "Support for China-related decisions", "为涉华决策提供支持"),
                   L("중국의 정책·시장·공급망 변화 앞에서 기업이 내려야 하는 전략적 결정을, 거시·산업·정책 분석으로 뒷받침합니다.",
                     "We back the strategic decisions companies face amid shifts in China's policy, markets and supply chains with macro, industry and policy analysis.",
                     "面对中国政策、市场与供应链的变化，以宏观、产业与政策分析支持企业的战略决策。"),
                   cta_band("CEO China Brief", L("CSAI의 대표 프로그램. 경영진이 한 달에 두 번, 중국의 변화가 우리 회사에 무엇을 뜻하는지 원장에게 직접 듣는 초청형 브리핑입니다.", "Our flagship: twice a month, executives hear directly from the President what changes in China mean for their company. By invitation.", "CSAI旗舰项目：高管每月两次直接聆听院长解读中国变化对本企业的意义。邀请制。"), L("자세히 보기", "Learn more", "了解详情"), P("advisory", "brief"), flush=True)
                   + f'<div class="g3" style="margin-top:24px">{sv}</div><p class="note" style="margin-top:18px">{scope_note()}</p>'
                   f'<div class="sec-foot">{btn(L("기업 문의", "Business Inquiry", "企业咨询"), P("contact", "advisory"), "navy")}{more(L("자문 분야 자세히", "About our advisory", "了解咨询服务"), P("advisory"))}</div>')

    def tick(items):
        return '<ul class="ticks">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
    duo = f'''<div class="g2">
  <div class="card"><div class="badge-ico">{icon("cap", 26)}</div><h3>{L("교육·아카데미", "Academy", "教育学院")}</h3>
    <p>{L("중국 경제와 정책, 디지털 금융을 주제로 한 교육 프로그램을 준비하고 있습니다.", "Programmes on China's economy and policy, and on digital finance, are in preparation.", "以中国经济与政策、数字金融为主题的教育项目正在筹备中。")}</p>
    {tick([L("CEO 중국경제 전략 과정", "CEO programme on China's economy and strategy", "CEO中国经济战略课程"), L("공급망 리스크 과정", "Supply-chain risk programme", "供应链风险课程"), L("금융기관 중국 리스크 과정", "China-risk programme for financial institutions", "金融机构中国风险课程"), L("기업 맞춤 교육", "Corporate training", "企业定制培训"), L("디지털 금융 교육", "Digital finance training", "数字金融培训")])}
    {more(L("프로그램 보기", "Explore Programs", "查看课程"), P("academy"))}</div>
  <div class="card"><div class="badge-ico">{icon("globe", 26)}</div><h3>{L("글로벌 협력", "Global Network", "全球合作")}</h3>
    <p>{L("해외 연구기관·전문가와의 공동연구, 포럼, 특별기고 등 협력의 창구를 엽니다.", "A window for cooperation with overseas institutes and experts: joint research, forums and contributed articles.", "面向海外研究机构与专家，开放联合研究、论坛与特约撰稿等合作渠道。")}</p>
    {tick([L("협력기관", "Partner institutions", "合作机构"), L("전문가 네트워크", "Expert network", "专家网络"), L("포럼·행사", "Forums & events", "论坛与活动")])}
    {more(L("협력 제안하기", "Partnership", "合作提案"), P("global"))}</div>
</div>'''
    academy = sec("academy-global", "ACADEMY & GLOBAL", L("교육과 국제협력", "Education and international cooperation", "教育与国际合作"), "", duo, "alt")

    media = [(L("내일신문 「금요논단」", "Naeil Shinmun — Friday column", "《明日新闻》周五专栏"), L("칼럼 연재 중", "Ongoing column", "专栏连载中"), NAEIL_SEARCH),
             (L("유튜브 「안유화의 경제투자론」", "YouTube — An Yuhua's Economy & Investment", "YouTube《安玉花的经济投资论》"), L("매주 화요일 새 영상", "New video every Tuesday", "每周二更新"), YOUTUBE),
             (L("연합인포맥스 「안유화 쇼」", "Yonhap Infomax — The An Yuhua Show", "韩联社 Infomax《安玉花秀》"), L("경제 방송 진행", "Broadcast host", "财经节目主持"), "https://www.youtube.com/watch?v=rvKXDS1vyRA"),
             (L("팟캐스트 「안경투」", "Podcast — An Yuhua's Economy & Investment", "播客《安玉花的经济投资论》"), L("팟빵", "Podbbang", "Podbbang"), PODCAST)]
    mlist = "".join(f'<li><a href="{u}" target="_blank" rel="noopener"><span>{t}<small>{s}</small></span>{icon("ext", 16)}</a></li>' for t, s, u in media)
    news = sec("news", "NEWS & EVENTS", L("소식과 미디어", "News & media", "动态与媒体"), "", f'''<div class="g3">
  <div class="newscol"><h3>{icon("news", 20)}{L("기관 소식", "News", "机构动态")}</h3>{notices()}</div>
  <div class="newscol"><h3>{icon("play", 20)}{L("언론·미디어", "Media", "媒体")}</h3><ul>{mlist}</ul></div>
  <div class="newscol"><h3>{icon("cal", 20)}{L("행사 일정", "Events", "活动日程")}</h3>{events_list(False)}</div>
</div>
<h3 class="sub-h" id="videos">{L("영상·강연", "Videos & Talks", "视频与演讲")}</h3><p class="sub-p">{videos_lede()}</p>{player()}{media_cards()}
<div class="sec-foot">{btn(L("영상 해설 읽기", "Read the video notes", "阅读视频解读"), P("videos"), "navy")}{more(L("전체 보기", "View all news", "查看全部"), P("news"))}</div>''')

    band = f'''<section class="band" id="subscribe"><div class="wrap">
  <div class="col"><h2>{L("뉴스레터 구독", "Subscribe to the newsletter", "订阅通讯")}</h2>
    <p>{L("월간 「중국경제포커스」를 이메일로 받아 보세요. 무료입니다.", "Get the monthly China Economy Focus by email. It is free.", "通过邮件接收月刊《中国经济聚焦》，免费订阅。")}</p>
    {btn(L("무료 구독하기", "Subscribe", "免费订阅"), SUBSCRIBE, ext=True)}</div>
  <div class="col"><h2>{L("문의·협력 제안", "Inquiries & partnership", "咨询与合作")}</h2>
    <p>{L("기업 자문, 교육, 국제협력, 강연·인터뷰 요청을 목적별로 접수합니다.", "Business advisory, training, international cooperation, and speaking or interview requests — each has its own form.", "企业咨询、培训、国际合作及演讲采访邀请，按类别受理。")}</p>
    {btn("Contact CSAI", P("contact"), "line")}</div>
  <div class="col qr-col"><img src="{A("assets/qr.svg")}" width="132" height="132" alt="{L("csai.re.kr 홈페이지 QR 코드", "QR code for csai.re.kr", "csai.re.kr 网站二维码")}" loading="lazy">
    <p>{L("휴대폰 카메라로 찍으면<br>홈페이지가 열립니다.", "Scan with your phone<br>to open this site.", "用手机扫码<br>即可打开本网站。")}<br><b>www.csai.re.kr</b></p></div>
</div></section>'''

    body = hero + quick + mission + about + research + machine + columns + focus + insight + princ + books + director + advisory + academy + news + band
    desc = L("CSAI는 중국의 경제·정책을 깊이 분석하고, 한국 기업과 기관의 전략적 의사결정을 지원합니다. 연구·분석, 거시경제연구소, 기업 자문, 교육, 글로벌 협력.",
             "CSAI analyses China's economy and policy in depth and supports the strategic decisions of Korean companies and institutions.",
             "CSAI深入分析中国经济与政策，为韩国企业和机构的战略决策提供支持。")
    return page("index", "CSAI", desc, body)
