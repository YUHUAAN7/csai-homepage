# -*- coding: utf-8 -*-
"""하위 페이지: 연구원 소개, 연구·분석, 거시경제연구소, 기업 자문, 아카데미, 글로벌 협력, 뉴스·자료,
연구소장's Insight, 문의, 정책."""
from core import *
from content import *








# ── 연구원 소개 ────────────────────────────────────────────────






def about():
    C.slug = "about"
    lede = L("CSAI는 중국의 거시경제와 정책을 분석해 한국 기업·기관의 의사결정으로 연결하는 연구기관입니다.",
             "CSAI is a research institute that analyses China's macro economy and policy and connects that analysis to the decisions of Korean companies and institutions.",
             "CSAI是一家分析中国宏观经济与政策，并将其转化为韩国企业和机构决策依据的研究机构。")
    title = L("연구원 소개", "About CSAI", "关于CSAI")
    b = page_hero("about", "ABOUT CSAI", title, lede)

    H = [
        ("2015.07", L("주식회사 중국증권행정연구원 설립", "China Securities Administration Institute Co., Ltd. founded", "中国证券行政研究院株式会社成立"), ""),
        ("2016.09", L("연합뉴스, 안유화 박사를 ‘중국 금융 스페셜리스트’로 소개", "Yonhap News profiles Dr An Yuhua as a “China finance specialist”", "韩联社以“中国金融专家”介绍安玉花博士"), "https://www.yna.co.kr/view/AKR20160913157700371"),
        ("2024.08", L("전기신문 보도: 중국의 친환경 기술 선점과 한·중 협력", "Electimes: China's lead in green technology and Korea–China cooperation", "《电气新闻》报道：中国抢占绿色技术与韩中合作"), "https://www.electimes.com/news/articleView.html?idxno=341779"),
        ("2025.04", L("전기신문 보도: 미·중 패권 경쟁과 한국의 ‘삼중 트랙’ 대응", "Electimes: US–China rivalry and Korea's “three-track” response", "《电气新闻》报道：美中霸权竞争与韩国的“三轨”应对"), "https://www.electimes.com/news/articleView.html?idxno=353203"),
        ("2025.06", L("의정부시 인공지능 포럼 기조강연", "Keynote at the Uijeongbu City AI Forum", "在议政府市人工智能论坛作主旨演讲"), "https://www.wikitree.co.kr/articles/1060824"),
        ("2025.09", L("아시아투데이 보도: AI·디지털자산과 한국 기업의 기회", "Asia Today: AI, digital assets and the opportunity for Korean companies", "《今日亚洲》报道：AI·数字资产与韩国企业的机会"), "https://www.asiatoday.co.kr/kn/view.php?key=20250907002221015"),
        ("2025.09", L("한국일보 한국아카데미 14기 강의", "Lecture at the Hankook Ilbo Korea Academy, 14th class", "在《韩国日报》韩国学院第14期授课"), "https://www.hankookilbo.com/news/article/A2025091710450002426"),
        ("2026.03", L("매일경제와 「디지털자산·AI 융합 최고위과정」 공동 주관 (1·2기 운영, 3기 2027년 3월 개강)", "Co-organising the “Digital Assets and AI” executive programme with Maeil Business Newspaper (1st and 2nd classes run; 3rd opens March 2027)", "与《每日经济》共同主办“数字资产·AI融合高层课程”（已办第1、2期，第3期2027年3月开课）"), "https://m.mk.co.kr/amp/11979976"),
        ("2026.09", L("뉴시스·매일경제 보도: “한국의 골든타임은 3~5년”", "Newsis and Maeil Business: “Korea's golden time is three to five years”", "纽西斯·《每日经济》报道：“韩国的黄金时间是3至5年”"), "https://www.newsis.com/view/NISX20260910_0003783819"),
    ]
    hist = ('<h3 style="font-size:20px;margin:30px 0 4px">' + L("연혁", "History", "沿革") + '</h3><ul class="hist">'
            + "".join("<li><b>" + d + "</b><span>" + (('<a href="' + u + '" target="_blank" rel="noopener">' + t + "</a>") if u else t) + "</span></li>" for d, t, u in H) + "</ul>")
    b += sec("overview", "OVERVIEW", L("기관 개요", "Overview", "机构概况"), "", f'''<div class="split">
  <div class="bio"><p>{L("중국증권행정연구원(CSAI)은 중국의 정책과 시장을 원문과 데이터로 읽어, 한국의 기업과 기관이 더 나은 결정을 내리도록 돕는 독립 거시경제 싱크탱크입니다. 연구·분석, 월간 「중국경제포커스」, 기업 자문, 교육, 국제협력을 한 흐름으로 운영합니다.",
        "The China Securities Administration Institute (CSAI) is an independent macroeconomic think tank that reads China's policies and markets through original documents and data, helping companies and institutions in Korea make better decisions. Research and analysis, the monthly China Economy Focus, business advisory, education and international cooperation run as one flow.",
        "中国证券行政研究院（CSAI）是一家独立的宏观经济智库，以原始文件和数据解读中国的政策与市场，帮助韩国的企业和机构做出更好的决策。研究分析、月刊《中国经济聚焦》、企业咨询、教育与国际合作作为一个整体运行。")}</p>
    <p>{L("쌓인 기록으로 판단을 검증하고, 검증된 판단으로 한국 기업과 기관의 결정을 돕습니다.",
          "We test our judgments against the record we accumulate, and use the tested judgments to support the decisions of Korean companies and institutions.",
          "我们用积累的记录检验判断，再以经过检验的判断支持韩国企业和机构的决策。")}</p>
    {hist}</div>
  <div>{kv([
        (L("대외 표기", "Name", "对外名称"), "CSAI"),
        (L("하는 일", "What we do", "业务范围"), L("중국 거시·정책·산업 연구, 콘텐츠 발행, 기업 자문, 교육, 국제협력", "China macro, policy and industry research; publishing; business advisory; education; international cooperation", "中国宏观、政策与产业研究，内容发行，企业咨询，教育，国际合作")),
        (L("콘텐츠 채널", "Content channel", "内容频道"), L("거시경제연구소 · 월간 「중국경제포커스」", "China Economy Focus (Macroeconomic Institute) · monthly issue", "宏观经济研究所 · 月刊《中国经济聚焦》")),
        (L("언어", "Languages", "语言"), L("한국어 · 영어 · 중국어", "Korean · English · Chinese", "韩语 · 英语 · 中文")),
        (L("슬로건", "Slogan", "口号"), "Insight without Borders"),
    ])}</div>
</div>''')

    do = [L("거시경제·산업·정책·공급망 분석과 기업의 전략적 의사결정 지원", "Macro, industry, policy and supply-chain analysis, and support for companies' strategic decisions", "宏观、产业、政策与供应链分析，以及对企业战略决策的支持"),
          L("공개 자료와 적법한 조사 범위 안에서의 연구", "Research within public sources and lawful inquiry", "在公开资料与合法调研范围内开展研究"),
          L("숫자는 출처와 함께, 추정은 추정이라고 밝히기", "Numbers with their sources; estimates labelled as estimates", "数字注明出处，估算明确标示"),
          L("구독과 자문을 핵심 수입으로 하는 독립 운영", "Independent operation, with subscriptions and advisory as core income", "以订阅与咨询为核心收入的独立运营")]
    dont = [L("유료 종목 추천, 목표가, 매매 전략 제시", "Paid stock picks, price targets or trading strategies", "付费荐股、目标价或交易策略"),
            L("고객 자산 운용, 투자일임, 투자중개·주선", "Managing client assets, discretionary investment, or investment brokerage", "客户资产管理、全权委托投资或投资中介"),
            L("비공개 정보 접근을 내세운 홍보", "Promoting access to non-public information", "以获取非公开信息作为宣传"),
            L("실사·전문가 네트워크형 조사, 비공개 데이터 수집", "Due-diligence or expert-network style investigation, or collecting non-public data", "尽职调查或专家网络式调查，以及收集非公开数据"),
            L("정책 모니터링만 하는 상품 — 판단·데이터·접근이 없는 상품은 내지 않습니다", "Products that only monitor policy — nothing without judgment, data or access", "只做政策监测的产品——没有判断、数据或渠道的产品不推出"),
            L("단독 후원이나 정부 과제에만 기대는 운영", "Relying on a single sponsor or on government projects alone", "仅依赖单一赞助方或政府课题的运营")]
    b += sec("position", "POSITION", boundary_title(), "", boundary_block(), "alt")
    b += sec("vision", "VISION & MISSION", L("비전·미션", "Vision & Mission", "愿景与使命"), "", f'''<div class="vision-box">
  <p class="yr">VISION 2036</p>
  <p class="big">{L("중국의 정책을 한국의 결정으로 번역한다.", "Translating China into Korean decisions.", "把中国的政策，翻译成韩国的决策。")}</p>
  <p class="en">{L("Translating China into Korean decisions · 중국과 세계를 잇는 아시아의 독립 거시경제 싱크탱크", "An independent Asian macroeconomic think tank connecting China and the world", "Translating China into Korean decisions · 连接中国与世界的亚洲独立宏观经济智库")}</p></div>
<div class="g2" style="margin-top:36px">
  <div class="card"><div class="num">MISSION</div><h3>{L("미션", "Mission", "使命")}</h3><p>{L("중국을 가장 깊이 읽는 거시경제 통찰로, 한국과 세계의 기업·기관이 더 나은 결정을 내리도록 돕는다.", "With the deepest macroeconomic reading of China, we help companies and institutions in Korea and the world make better decisions.", "以对中国最深入的宏观经济洞察，帮助韩国与世界的企业和机构做出更好的决策。")}</p></div>
  <div class="card"><div class="num">SLOGAN</div><h3>Insight without Borders</h3><p>{L("국경을 넘어 통하는 통찰을 지향합니다.", "Insight that travels across borders.", "追求跨越国界的洞察。")}</p></div>
</div>
<h3 style="margin:44px 0 18px;font-size:24px">{L("핵심가치", "Core values", "核心价值")}</h3>{core_values_cards()}
<h3 style="margin:44px 0 8px;font-size:24px">{L("차별화 자산: 판단 · 데이터 · 접근", "What sets us apart: judgment, data, access", "差异化资产：判断 · 数据 · 渠道")}</h3><p class="sub-p">{assets_lede()}</p>{asset_cards(detail=True)}
<h3 style="margin:44px 0 18px;font-size:24px">{L("운영 원칙", "How we work", "运营原则")}</h3>
<div class="g2"><div class="card"><h3>{L("하는 일", "What we do", "我们做什么")}</h3>{ticks(do)}</div>
<div class="card"><h3>{L("하지 않는 일", "What we do not do", "我们不做什么")}</h3>{ticks(dont, "ticks xs")}</div></div>''')
    b += sec("strategy", "STRATEGY", L("4대 전략 방향", "Four strategic directions", "四大战略方向"), strategy_lede(), strategy_cards(), "alt")

    bio = "".join(f"<p>{p}</p>" for p in bio_paragraphs())
    b += sec("leadership", "LEADERSHIP", L("리더십", "Leadership", "领导层"), "", f'''<div class="leader">
  <figure class="portrait"><img src="{A("profile.jpg")}" alt="{L("안유화 원장 프로필 사진", "Portrait of Professor An Yuhua", "安玉花院长照片")}" width="720" height="900"></figure>
  <div class="bio"><h3>{message()["name"]}</h3><p class="role">{L("중국증권행정연구원(CSAI) 원장 · 중국 경제·금융 전문가 · 경영학 박사", "President, CSAI · China economy & finance · Ph.D. in Business", "CSAI院长 · 中国经济与金融专家 · 管理学博士")}</p>
    <div class="greeting" id="greeting">
      <div class="g-label">{L("원장 인사말", "FROM THE PRESIDENT", "院长致辞")}</div>
      <p class="g-title">{L("중국을 묻는 것은 결국 한국을 묻는 일입니다", "To ask about China is, in the end, to ask about Korea.", "问中国，归根结底是问韩国。")}</p>
      <p>{L("“중국은 어떻게 됩니까?”라는 질문 뒤에는 늘 “그러면 우리는 어떻게 해야 합니까?”가 있습니다. 저희 연구는 그 두 번째 질문에 답하려고 있습니다.", "Behind the question “What will happen to China?” there is always another: “Then what should we do?” Our research exists to answer that second question.", "“中国会怎样？”这个问题背后，总有另一个问题：“那么我们该怎么办？”我们的研究，正是为了回答这第二个问题。")}</p>
      <p>{L("중국을 정확히 읽는 것이 세계 경제를 읽는 일이고, 그 끝은 언제나 한국의 결정이어야 합니다.", "Reading China accurately is reading the world economy, and where it ends must always be a decision for Korea.", "准确读懂中国，就是读懂世界经济；而它的终点，始终应当是韩国的决策。")}</p>
      <p class="g-sign">{L("중국증권행정연구원 원장 <strong>안유화</strong>", "<strong>An Yuhua</strong>, President, China Securities Administration Institute", "中国证券行政研究院 院长 <strong>安玉花</strong>")}</p>
    </div>
    {bio}{channels()}
    <h3 style="font-size:20px;margin:36px 0 14px">{L("약력", "Career", "履历")}</h3>{timeline()}</div>
</div>''')

    fn = [("chart", L("연구·분석", "Research", "研究分析"), P("research")), ("news", L("거시경제연구소", "China Economy Focus", "宏观经济研究所"), P("focus")),
          ("users", L("기업 자문", "Business Advisory", "企业咨询"), P("advisory")), ("cap", L("교육·아카데미", "Academy", "教育学院"), P("academy")),
          ("globe", L("글로벌 협력", "Global Network", "全球合作"), P("global"))]
    fcards = "".join(f'<a class="type" href="{h}"><h3>{icon(ic, 20)}{t}</h3></a>' for ic, t, h in fn)
    HEAD = ("본부장", "Head", "本部长")
    org = [
        (L("교육본부", "Education Division", "教育本部"), L("본부장", "Heads", "本部长"), [("김장호",) + HEAD, ("문정진",) + HEAD], [("문지은", "과장", "Manager", "科长")],
         [L("최고위과정", "Executive programme", "高层课程"), L("강좌·독서모임", "Courses and reading group", "讲座·读书会"), L("중국 탐방", "China study tours", "中国考察")]),
        (L("산업전략본부", "Industry Strategy Division", "产业战略本部"), L("본부장", "Head", "本部长"), [("김장호",) + HEAD], [("홍명기", "PD", "PD", "PD")],
         [L("한·중 기업 투자, 상장·M&amp;A", "Korea–China corporate investment, listings and M&amp;A", "韩中企业投资、上市与并购"), L("유튜브 영상 제작", "YouTube video production", "YouTube视频制作"), L("방송·인터뷰", "Broadcast and interviews", "广播与采访")]),
        (L("리서치&amp;컨설팅본부", "Research &amp; Consulting Division", "研究与咨询本部"), L("본부장", "Head", "本部长"), [("문정진",) + HEAD], [],
         [L("뉴스레터 구독 상품", "Newsletter subscriptions", "订阅通讯产品"), L("기업 회원·컨설팅", "Corporate membership and consulting", "企业会员·咨询"), L("국제협력, 외부 강연", "International cooperation and outside lectures", "国际合作、对外演讲"),
          L("기획·운영관리", "Planning and operations", "企划·运营管理"), L("홈페이지·홍보", "Website and communications", "网站·宣传")]),
        (L("세무&amp;재무본부", "Tax &amp; Finance Division", "税务与财务本部"), L("담당", "Lead", "负责人"), [("문지은", "과장", "Manager", "科长")], [("김광용", "대표", "CEO", "代表")],
         [L("세금계산서 발행·수취", "Tax invoices issued and received", "税务发票开具与收取"), L("비용 처리와 증빙", "Expenses and supporting records", "费用处理与凭证")]),
    ]
    ppl = lambda ps, tag: "<br>".join(f"<{tag}>{n}</{tag}> {L(ko, en, zh)}" for n, ko, en, zh in ps)
    ocols = "".join(
        f'<div class="org-col"><div class="org-card"><h3>{t}</h3><div class="org-in"><div class="org-k">{hl}</div><div class="org-v">{ppl(hs, "b")}</div>'
        + (f'<div class="org-k">{L("구성원", "Members", "成员")}</div><div class="org-v">{ppl(ms, "span")}</div>' if ms else "")
        + f'<div class="org-k">{L("하는 일", "Work", "职能")}</div><div class="org-w">{"<br>".join(ws)}</div></div></div></div>'
        for t, hl, hs, ms, ws in org)
    orgchart = (f'<div class="org"><div class="org-top"><small>{L("원장", "President", "院长")}</small><b>{L("안유화", "An Yuhua", "安玉花")}</b></div>'
                f'<div class="org-stem"></div><div class="org-cols">{ocols}</div></div>')
    b += sec("organization", "ORGANIZATION", L("조직", "Organization", "组织架构"), "",
             orgchart + '<div style="margin-top:22px">' + soon(L("전문가 프로필은 확정되는 대로 올립니다.", "Expert profiles will be posted once confirmed.", "专家简介将在确认后发布。")) + "</div>"
             + f'<h3 style="font-size:20px;margin:36px 0 16px">{L("주요 기능", "Main functions", "主要职能")}</h3><div class="g3">{fcards}</div>', "alt")

    b += sec("contact", "CONTACT", L("연락처", "Contact", "联系方式"), "", kv([
        (L("이메일", "Email", "邮箱"), f'<a class="mailto" href="mailto:{MAIL}">{MAIL}</a>'),
        (L("문의 접수", "Inquiries", "咨询受理"), L("기업 자문 · 교육 · 국제협력 · 일반 문의를 목적별로 받습니다.", "Business advisory, education, international cooperation and general inquiries, each with its own form.", "企业咨询、教育、国际合作与一般咨询，按类别受理。")),
        (L("대표 전화", "Phone", "电话"), '<a href="tel:+8225170866">02-517-0866</a>'),
    ]) + f'<div class="sec-foot">{btn(L("문의하기", "Contact CSAI", "联系我们"), P("contact"), "navy")}</div>')
    return page("about", title, lede, b, "about")


# ── 연구·분석 ──────────────────────────────────────────────────




def research():
    C.slug = "research"
    title = L("연구·분석", "Research", "研究分析")
    lede = L("중국의 거시경제·정책·산업을 데이터와 원칙으로 읽고, 한국 기업·기관의 결정에 필요한 시사점으로 정리합니다.",
             "We read China's macro economy, policy and industry through data and principles, and distil what Korean companies and institutions need for their decisions.",
             "以数据和原则解读中国的宏观经济、政策与产业，并提炼出韩国企业和机构决策所需的启示。")
    b = page_hero("research", "RESEARCH", title, lede)
    b += sec("framework", "FRAMEWORK", L("중국 경제는 어떻게 작동하는가", "How China's economy works", "中国经济如何运行"), machine_lede(), machine_block())

    cards = "".join(
        f'<div class="card" id="{a}"><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3><p>{d}</p><div class="tags">{"".join(f"<span>{x}</span>" for x in tg)}</div></div>'
        for a, ic, t, d, tg in research_areas())
    for a, ic, t, d, tg in research_areas():
        reg(t, d, P("research", a), "Research")
    b += sec("areas", "RESEARCH AREAS", L("연구 분야", "Research areas", "研究领域"),
             L("세 분야를 따로 보지 않고 서로의 원인과 결과로 함께 읽습니다.", "We read the three areas together, as each other's causes and effects.", "三个领域不分开看，而是作为彼此的因果一并解读。"),
             f'<div class="g3">{cards}</div>{future_finance()}', "alt")

    rep_card = ('<div class="card" id="report-supply-chain-01"><div class="num">CSAI GLOBAL SUPPLY CHAIN FOCUS · No. 01 · 2026.11</div><h3>'
                + L("반도체 공급망 대전환 2026", "The Great Semiconductor Supply-chain Shift 2026", "半导体供应链大转变 2026") + "</h3><p><b>"
                + L("미중 갈등이 다시 그리는 반도체 지도와 한국의 선택", "The chip map redrawn by US–China rivalry, and Korea's choices", "美中博弈重绘的半导体版图与韩国的选择") + "</b></p><p>"
                + L("반도체 공급망은 하나의 세계 사슬에서 관리된 두 개의 사슬로 갈라지고 있습니다. 한국은 가장 대체하기 어려운 메모리를 쥐고 있지만 설계 소프트웨어, 장비, 소재는 남에게 기대고 있습니다. 누가 병목을 쥐고 누가 밀려나는지, 한국은 무엇을 해야 하는지를 공개 자료 16건으로 정리했습니다.",
                    "The semiconductor supply chain is splitting from one global chain into two managed chains. Korea holds memory, the hardest link to replace, but relies on others for design software, equipment and materials. Drawing on 16 public sources, the report sets out who holds the chokepoints, who is pushed aside, and what Korea should do.",
                    "半导体供应链正从一条全球链条分裂为两条受管理的链条。韩国握有最难替代的存储芯片，但在设计软件、设备和材料上依赖他人。报告依据16份公开资料，梳理谁掌握瓶颈、谁被挤出，以及韩国该怎么做。") + '</p><p style="font-size:14px;color:var(--ink-2)">'
                + L("차례: 공급망 지도 · 병목과 집중도 · 단계별 경쟁력 · 미중 갈등이 바꾸는 사슬 · 승자와 패자 · 2027~2030 시나리오 · 한국의 위기와 기회 · 지켜볼 신호",
                    "Contents: supply-chain map · chokepoints and concentration · competitiveness by stage · how US–China rivalry changes the chain · winners and losers · 2027–2030 scenarios · risks and opportunities for Korea · signals to watch",
                    "目录：供应链地图 · 瓶颈与集中度 · 各环节竞争力 · 美中博弈如何改变链条 · 赢家与输家 · 2027~2030情景 · 韩国的危机与机遇 · 值得关注的信号") + '</p><p style="font-size:13.500px;color:var(--muted)">'
                + L("작성 기준일 2026년 11월 3일 · 15쪽", "As of 3 November 2026 · 15 pages", "编写基准日：2026年11月3日 · 15页") + ' · <a href="' + P("contact") + '" style="font-weight:700;color:var(--navy-700)">'
                + L("전문 문의", "Request the full report", "索取全文") + " →</a></p></div>")
    IND = [
        (L("정책 문장 강도 지수", "Policy Language Index", "政策措辞强度指数"),
         L("정치국 회의, 중앙경제공작회의, 인민은행 통화정책 보고서의 수식어 변화를 회의마다 비교해 완화와 긴축의 방향과 세기를 점수로 매깁니다.", "Compares the modifiers in Politburo, Central Economic Work Conference and PBOC policy texts from one meeting to the next, and scores the direction and strength of easing or tightening.", "逐次比较政治局会议、中央经济工作会议和央行货币政策报告中的措辞变化，为宽松或收紧的方向与力度打分。"),
         L("자료: 회의 발표문·보고서 원문 · 주기: 회의마다", "Source: original meeting statements and reports · Each meeting", "资料：会议公报与报告原文 · 周期：每次会议")),
        (L("부채 위치 지도", "Debt Location Map", "债务位置图"),
         L("중국 부채를 중앙정부, 지방정부, 기업, 가계로 나눠 어디에서 늘고 줄었는지를 봅니다. 총량보다 위치를 봅니다.", "Splits China's debt among central government, local governments, companies and households to see where it rises and falls. Location before totals.", "把中国债务分为中央政府、地方政府、企业和家庭，观察增减发生在哪里。看位置，而不只看总量。"),
         L("자료: 인민은행, 재정부, 국제결제은행(BIS) · 주기: 분기", "Source: PBOC, Ministry of Finance, BIS · Quarterly", "资料：中国人民银行、财政部、国际清算银行 · 周期：季度")),
        (L("한국 수출로 읽는 중국", "China through Korean Exports", "从韩国出口看中国"),
         L("한국의 대중 수출을 품목별로 가격 효과와 물량 효과로 나눠, 중국 수요의 실제 변화를 읽습니다.", "Breaks Korea's exports to China into price and volume effects by product, to read the real change in Chinese demand.", "按品类把韩国对华出口分解为价格效应与数量效应，读出中国需求的实际变化。"),
         L("자료: 관세청·산업부 통계 · 주기: 월", "Source: Korea Customs Service and trade ministry statistics · Monthly", "资料：韩国关税厅与产业部统计 · 周期：月")),
        (L("성(省)별 체력 지표", "Provincial Strength Indicators", "省级实力指标"),
         L("31개 성의 재정 자립도, 토지 수입 의존도, 부채 부담을 묶어 지역 사이의 격차를 봅니다.", "Combines fiscal self-sufficiency, reliance on land revenue and debt burden across 31 provinces to see the gaps between regions.", "综合31个省份的财政自给率、土地收入依赖度与债务负担，观察地区之间的差距。"),
         L("자료: 각 성 재정청, 국가통계국 · 주기: 반기", "Source: provincial finance departments, NBS · Half-yearly", "资料：各省财政厅、国家统计局 · 周期：半年")),
        (L("순풍·역풍 지수", "Tailwind–Headwind Index", "顺风·逆风指数"),
         L("매주 쌓는 정책 신호를 한국 산업별(반도체, 배터리, 자동차, 해운 등)로 순풍과 역풍으로 나눠 세고 그 차이를 봅니다.", "Counts each week's policy signals as tailwinds or headwinds for Korean industries such as semiconductors, batteries, autos and shipping, and tracks the difference.", "把每周积累的政策信号按韩国产业（半导体、电池、汽车、航运等）分为顺风与逆风并统计其差值。"),
         L("자료: CSAI 정책 신호 기록 · 주기: 주", "Source: CSAI policy signal log · Weekly", "资料：CSAI政策信号记录 · 周期：周")),
        (L("CSAI 판단 기록", "CSAI Judgment Record", "CSAI判断记录"),
         L("기준일과 무효화 조건을 붙여 공개한 판단이 맞았는지 빗나갔는지를 기록하고 공개합니다.", "Records and publishes whether each judgment we issued, with its as-of date and invalidation condition, proved right or wrong.", "记录并公布每一项附有基准日与失效条件的判断是否应验。"),
         L("자료: CSAI 판단 기록 · 주기: 판단의 점검일마다", "Source: CSAI judgment log · At each review date", "资料：CSAI判断记录 · 周期：每个检验日")),
        (L("공급망 의존 지도", "Supply-chain Dependence Map", "供应链依存图"),
         L("한국이 중국에서 들여오는 핵심 품목(희토류, 흑연, 요소, 배터리 소재 등)의 대중 수입 의존도와 중국의 수출통제 조치를 품목별로 함께 봅니다.", "Tracks, item by item, Korea's import dependence on China for key inputs such as rare earths, graphite, urea and battery materials, alongside China's export controls.", "逐项观察韩国对中国关键品类（稀土、石墨、尿素、电池材料等）的进口依存度以及中国的出口管制措施。"),
         L("자료: 관세청 수출입 통계, 중국 상무부·해관총서 공고 · 주기: 월", "Source: Korea Customs Service trade data, MOFCOM and GACC notices · Monthly", "资料：韩国关税厅进出口统计、中国商务部与海关总署公告 · 周期：月")),
        (L("첨단산업 선두 지표", "Frontier Industry Leadership", "尖端产业领先指标"),
         L("전기차, 배터리, 태양광, 조선, AI, 로봇처럼 중국이 세계 선두권에 있는 산업의 세계 점유율과 한국과의 격차를 봅니다.", "Tracks global shares in industries where China is among the world leaders, such as EVs, batteries, solar, shipbuilding, AI and robots, and the gap with Korea.", "观察电动车、电池、光伏、造船、AI、机器人等中国处于世界前列的产业的全球份额及其与韩国的差距。"),
         L("자료: 해관총서, 산업별 협회, 국제기구 통계 · 주기: 분기", "Source: GACC, industry associations, international agencies · Quarterly", "资料：海关总署、各行业协会、国际机构统计 · 周期：季度")),
    ]
    ind_lede = L("CSAI는 ‘중국을 읽는 원칙’에서 나온 여덟 가지 고유 지표를 쌓아 갑니다. 아래에 지표마다 무엇을 보는지, 자료와 주기를 적었습니다. 수치는 쌓이는 대로 이곳에 공개합니다.",
                 "CSAI builds eight indicators of its own, each derived from our principles for reading China. Below is what each one looks at, with its sources and frequency. Figures will be published here as they accumulate.",
                 "CSAI持续积累源自“读懂中国的原则”的八项自有指标。下面列出每项指标观察什么、资料来源与周期。数据将随积累在此公布。")
    ind_cards = ('<h3 style="font-size:20px;margin:40px 0 16px">' + L("CSAI 고유 지표", "CSAI indicators", "CSAI自有指标") + '</h3><div class="g2">'
                 + "".join('<div class="card"><div class="num">' + ("%02d" % (k + 1)) + "</div><h3>" + t + "</h3><p>" + d + '</p><p style="font-size:13.500px;color:var(--muted)">' + m + "</p></div>" for k, (t, d, m) in enumerate(IND)) + "</div>")
    b += sec("data", "RESEARCH DATA", L("고유 데이터", "Our data", "自有数据"),
             L("공개 통계를 바탕으로 직접 가공한 지표를 시계열로 쌓아 갑니다.", "Indicators we build from public statistics, accumulated as time series.", "基于公开统计自行加工的指标，以时间序列持续积累。"),
             f'<div class="split"><div>{signal_box()}</div><div class="bio"><p>{ind_lede}</p></div></div>' + data_items() + ind_cards)

    b += sec("reports", "RESEARCH REPORTS", L("연구보고서·기고", "Research reports & commentary", "研究报告与评论"),
             L("원장의 자본시장연구원 시절 보고서부터 언론 기고까지, 중국 금융을 기록해 온 글입니다. CSAI의 새 보고서는 발간되는 대로 이곳에 올립니다.",
               "From the President's reports at the Korea Capital Market Institute to her newspaper columns: a record of writing on Chinese finance. New CSAI reports will be posted here as they are published.",
               "从院长在韩国资本市场研究院时期的报告到媒体专栏，这里汇集了记录中国金融的文字。CSAI的新报告将在发布后陆续上线。"),
             articles() + f'<div style="margin-top:24px">{rep_card}</div>'
             + columns_note(), "alt")
    return page("research", title, lede, b, "research")


# ── 거시경제연구소 ─────────────────────────────────────────────
def focus():
    C.slug = "focus"
    title = L("거시경제연구소", "China Economy Focus", "宏观经济研究所")
    lede = L("거시경제연구소는 CSAI의 콘텐츠 채널입니다. 월간 「중국경제포커스」와 영상으로 중국 경제의 흐름을 전하고, Flash와 심층보고를 준비하고 있습니다.",
             "China Economy Focus is the content channel of CSAI's Macroeconomic Institute (거시경제연구소). It covers China's economy through a monthly issue and video, with Flash notes and deep dives in preparation.",
             "宏观经济研究所是CSAI的内容频道，通过月刊《中国经济聚焦》与视频传递中国经济动向，快讯与深度报告正在筹备中。")
    b = page_hero("focus", "CHINA ECONOMY FOCUS", title, lede)
    pillars = [(L("거시", "Macro", "宏观"), L("성장률, 물가, 사회융자총량, 통화·재정 정책", "Growth, prices, total social financing, monetary and fiscal policy", "增长、物价、社会融资规模、货币与财政政策")),
               (L("산업분석", "Industry", "产业分析"), L("신에너지, 반도체, 플랫폼, 부동산", "New energy, semiconductors, platforms, property", "新能源、半导体、平台经济、房地产")),
               (L("공급망", "Supply chains", "供应链"), L("한중 교역, 핵심 소재, 수출통제", "Korea–China trade, critical materials, export controls", "韩中贸易、关键材料、出口管制"))]
    pc = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in pillars)
    b += sec("latest", "LATEST", L("최신", "Latest", "最新"), "",
             f'<div class="split"><div>{issue_card()}</div><div>{content_types()}<p class="note" style="margin-top:16px">{L("모든 콘텐츠는 ‘한국 시사점’으로 끝맺습니다. 중국의 변화가 한국 기업·기관의 가격·조달·투자·고용 결정에 주는 영향을 정리합니다.", "Every piece closes with “implications for Korea”: what the change in China means for pricing, sourcing, investment and hiring decisions.", "所有内容都以“对韩国的启示”收尾：中国的变化对韩国企业和机构在定价、采购、投资与用工决策上的影响。")}</p></div></div>')
    fh = lambda t: '<h4 style="font-size:15px;margin:14px 0 2px;color:var(--gold-600);letter-spacing:.04em">' + t + "</h4>"
    f_pts = L(["11월 1~10일 대중 수출은 91.6억 달러로 1년 전보다 148% 늘었습니다.",
               "같은 기간 반도체 수출이 331.2% 늘어 전체 수출의 49.7%를 차지했습니다. 대중 수출 급증도 반도체가 끌었을 가능성이 큽니다.",
               "그래서 이 숫자를 ‘중국 내수가 살아났다’는 신호로 읽기는 이릅니다. 가격이 오른 것인지 물량이 늘어난 것인지를 갈라 봐야 합니다."],
              ["Korea's exports to China in 1–10 November were $9.16bn, up 148% from a year earlier.",
               "Chip exports rose 331.2% in the same period and made up 49.7% of all exports, so chips probably drove the jump in shipments to China as well.",
               "It is too early to read this as a recovery in Chinese domestic demand. Price and volume have to be separated first."],
              ["11月1日至10日，韩国对华出口为91.6亿美元，同比增长148%。",
               "同期半导体出口增长331.2%，占全部出口的49.7%，对华出口的激增很可能同样由半导体带动。",
               "因此，把这一数字解读为“中国内需回暖”为时尚早，必须先区分价格与数量。"])
    f_nums = L(["전체 수출 335억 달러(+111.9%). 11월 1~10일 기준 역대 최대",
                "반도체 166억 달러(+331.2%). 비중 49.7%, 1년 전보다 25.3%포인트 상승",
                "대중 수출 91.6억 달러(+148%), 대미 수출 67.9억 달러(+163.6%)",
                "수입 247억 달러, 무역수지 88억 달러 흑자. 올해 누계 수출 9,636억 달러",
                "CSAI 계산: 대중 비중 약 27%, 대미 약 20%. 반도체를 뺀 수출은 약 169억 달러로 1년 전보다 40% 남짓 증가(반올림된 공표치로 계산한 어림값)"],
               ["Total exports $33.5bn (+111.9%), a record for 1–10 November",
                "Chips $16.6bn (+331.2%), 49.7% of exports, up 25.3 points from a year earlier",
                "To China $9.16bn (+148%); to the US $6.79bn (+163.6%)",
                "Imports $24.7bn, trade surplus $8.8bn; exports for the year to date $963.6bn",
                "CSAI arithmetic: China about 27% of exports, the US about 20%; exports excluding chips about $16.9bn, up a little over 40% (an approximation from rounded published figures)"],
               ["出口总额335亿美元（+111.9%），创11月1至10日历史新高",
                "半导体166亿美元（+331.2%），占比49.7%，同比上升25.3个百分点",
                "对华出口91.6亿美元（+148%），对美出口67.9亿美元（+163.6%）",
                "进口247亿美元，贸易顺差88亿美元；今年累计出口9,636亿美元",
                "CSAI测算：对华占比约27%，对美约20%；剔除半导体的出口约169亿美元，同比增长40%出头（依据四舍五入后的公布数据估算）"])
    f_read = L(["대중 수출 증가율(148%)은 전체(111.9%)보다 높지만 반도체(331.2%)보다는 한참 낮습니다. 반도체를 빼면 전체 수출 증가율은 40% 안팎으로 내려옵니다. 대중 수출도 같은 구조일 가능성이 큽니다.",
                "메모리 가격이 오르면 같은 물량을 팔아도 수출액은 늘어납니다. 금액이 늘었다고 중국이 더 많이 사 갔다고 읽을 수는 없습니다.",
                "10일 통계에는 나라별 품목 내역과 물량이 없습니다. 조업일수 차이도 걸러지지 않았습니다. 가격 효과와 물량 효과는 월간 확정치에서 갈라 보겠습니다."],
               ["Growth to China (148%) is above the total (111.9%) but far below chips (331.2%). Excluding chips, total export growth falls to around 40%, and shipments to China probably have the same structure.",
                "When memory prices rise, export value rises even on the same volume. A higher value does not mean China bought more.",
                "The ten-day release has no product breakdown by country, no volumes and no working-day adjustment. We will separate price and volume effects in the monthly data."],
               ["对华出口增速（148%）高于整体（111.9%），但远低于半导体（331.2%）。剔除半导体后，整体出口增速降至40%左右，对华出口很可能是同样的结构。",
                "存储芯片价格上涨时，即使数量不变，出口额也会增加。金额增加不等于中国买得更多。",
                "十日统计没有分国别的品类明细和数量，也未剔除工作日差异。价格效应与数量效应将在月度确定值中拆分。"])
    f_kor = L(["대중 수출이 좋아 보이는 것은 ‘반도체가 좋다’는 뜻에 가깝습니다. 석유화학, 철강, 일반기계처럼 중국 수요에 기대는 업종은 이 숫자를 회복의 근거로 삼기 어렵습니다.",
               "수출의 절반이 한 품목에서 나옵니다. 메모리 가격이 꺾이면 대중 수출과 무역수지가 함께 흔들립니다. 가격·조달·투자 계획에서 반도체 경기와 중국 수요를 따로 놓고 봐야 합니다."],
              ["Strong exports to China mostly mean strong chips. Sectors that depend on Chinese demand, such as petrochemicals, steel and general machinery, cannot take this figure as evidence of recovery.",
               "Half of all exports now come from one product. If memory prices turn, exports to China and the trade balance move together. Plans for pricing, sourcing and investment should treat the chip cycle and Chinese demand separately."],
              ["对华出口看起来强劲，更接近“半导体强劲”的意思。石化、钢铁、一般机械等依赖中国需求的行业，难以把这一数字当作回暖的依据。",
               "一半的出口来自单一品类。存储价格一旦回落，对华出口与贸易收支将同时波动。在定价、采购和投资计划中，应把半导体景气与中国需求分开看。"])
    f_next = L(["11월 1~20일 통계에서 대중 수출 증가율이 이어지는지",
                "12월 1일 월간 수출입 동향에서 반도체를 뺀 대중 수출이 얼마나 늘었는지. 이 숫자가 반도체를 뺀 전체 수출보다 빠르게 늘면 ‘중국 수요 회복’ 해석에 힘이 실립니다.",
                "연간 수출 1조 달러를 넘는 시점과 그때의 반도체 비중"],
               ["Whether growth to China holds in the 1–20 November release",
                "How much exports to China excluding chips grew in the monthly data due on 1 December. If they grow faster than total exports excluding chips, the case for a recovery in Chinese demand strengthens.",
                "When annual exports pass $1 trillion, and the chip share at that point"],
               ["11月1至20日统计中对华出口增速能否延续",
                "12月1日月度进出口动向中，剔除半导体的对华出口增长多少。若其增速快于剔除半导体的整体出口，“中国需求回暖”的解读将更有说服力。",
                "年度出口突破1万亿美元的时点及届时的半导体占比"])
    flash_card = ('<article class="card" id="flash-2026-11"><div class="num">FLASH · ' + L("한국 수출로 읽는 중국", "China through Korean Exports", "从韩国出口看中国") + " · " + L("2026년 11월 중순호", "Mid-November 2026", "2026年11月中旬")
                  + "</div><h3>" + L("반도체가 끌어올린 대중 수출, 중국 수요로 읽으면 안 되는 이유", "Chips lifted exports to China. Why that is not Chinese demand", "半导体拉高了对华出口：为什么不能把它读成中国需求") + "</h3>"
                  + '<p style="font-size:13.500px;color:var(--muted)">' + L("기준일 2026년 11월 15일 · 관세청 11월 1~10일 수출입 현황(11월 11일 발표)", "As of 15 November 2026 · Korea Customs Service release for 1–10 November (published 11 November)", "基准日：2026年11月15日 · 韩国关税厅11月1至10日进出口现况（11月11日发布）") + "</p>"
                  + fh(L("핵심 요지", "Key points", "核心要点")) + ticks(f_pts) + fh(L("숫자", "The numbers", "数字")) + ticks(f_nums) + fh(L("읽는 법", "How to read it", "如何解读")) + ticks(f_read)
                  + fh(L("한국 시사점", "Implications for Korea", "对韩国的启示")) + ticks(f_kor) + fh(L("다음에 확인할 것", "What we will check next", "接下来要验证的")) + ticks(f_next)
                  + '<p style="font-size:13px;color:var(--muted);margin-top:12px">' + L("출처: 관세청 발표를 전한 ", "Sources: Korea Customs Service figures as reported by ", "来源：转引韩国关税厅数据的")
                  + '<a href="https://www.koreatimes.co.kr/economy/others/20261111/exports-more-than-double-in-1st-10-days-of-november" target="_blank" rel="noopener">The Korea Times</a>, '
                  + '<a href="https://www.koreajoongangdaily.com/business/exports-more-than-double-in-1st-10-days-of-november/12966595" target="_blank" rel="noopener">Korea JoongAng Daily</a>'
                  + L(" 보도(2026.11.11). 비중과 반도체 제외 수치는 CSAI 계산입니다. 이 글은 투자 권유가 아닙니다.", " (11 Nov 2026). Shares and ex-chip figures are CSAI arithmetic. This note is not investment advice.", "报道（2026.11.11）。占比与剔除半导体的数值为CSAI测算。本文不构成投资建议。") + "</p></article>")
    b += sec("flash", "FLASH", "Flash", L("정책·통계·산업 변화에 대한 짧은 시의성 분석입니다. 무료 공개를 원칙으로 합니다.", "Short, timely notes on policy, data and industry shifts, open to all.", "针对政策、数据与产业变化的简短时评，以免费公开为原则。"),
             flash_card, "alt")
    b += sec("monthly", "MONTHLY", L("월간 「중국경제포커스」", "Monthly China Economy Focus", "月刊《中国经济聚焦》"),
             L("매월 둘째 주 화요일 아침, 중국 거시·산업·공급망의 한 달을 한 권으로 정리해 보내드립니다. 기사마다 한국 시사점을 붙입니다.",
               "Every second Tuesday morning: a month of China's macro economy, industries and supply chains in one issue, each article ending with what it means for Korea.",
               "每月第二个星期二早晨，将中国宏观、产业与供应链的一个月整理成一期发送，每篇文章都附上对韩国的启示。"),
             f'<div class="g3">{pc}</div><div class="split" style="margin-top:28px"><div>' + kv([
                 (L("발행", "Schedule", "发行"), L("매월 둘째 주 화요일 아침", "Second Tuesday of each month, morning", "每月第二个星期二早晨")),
                 (L("구성", "Sections", "栏目"), "OPINION · HOT ISSUE · MACRO · INDUSTRY · SUPPLY · Q&amp;A"),
                 (L("받아 보기", "How to get it", "获取方式"), f'<a href="{SUBSCRIBE}" target="_blank" rel="noopener">{L("이메일 무료 구독", "Free email subscription", "邮件免费订阅")}</a>'),
                 (L("지난 호", "Past issues", "往期"), f'<a href="{ARCHIVE}" target="_blank" rel="noopener">chinamacro.kr</a>'),
                 (L("발행 주체", "Publisher", "发行方"), L("거시경제연구소", "Macroeconomic Institute (거시경제연구소), CSAI", "宏观经济研究所")),
             ]) + f'</div><div>{signal_box()}</div></div><div class="sec-foot">{btn(L("무료 구독하기", "Subscribe free", "免费订阅"), SUBSCRIBE, "navy", ext=True)}{btn(L("지난 호 보기", "Past issues", "往期回顾"), ARCHIVE, "ghost", ext=True)}</div>')
    reg(L("심층보고 No.1 — 반도체·DRAM 공급망", "Deep Dive No. 1 — semiconductor and DRAM supply chain", "深度报告第1号——半导体与DRAM供应链"), "", P("focus", "deepdive"), "Deep Dive")
    b += sec("deepdive", "DEEP DIVE", L("심층보고", "Deep Dive", "深度报告"), L("특정 산업·정책·공급망을 깊이 다루는 보고서입니다. 분기마다 냅니다.", "In-depth reports on a single industry, policy or supply chain, published quarterly.", "针对单一产业、政策或供应链的深度报告，每季度发布。"),
             f'''<ul class="articles"><li><time>No. 1</time><div><h3>{L("반도체·DRAM 공급망", "Semiconductor and DRAM supply chain", "半导体与DRAM供应链")}</h3><p>{L("전문은 문의로 제공합니다.", "Full report available on inquiry.", "全文可通过咨询获取。")} <a href="{P("contact", "general")}">{L("문의하기", "Inquire", "咨询")}</a></p></div><span class="kind">{L("심층보고", "Deep Dive", "深度报告")}</span></li></ul>
<div style="margin-top:20px">{soon(L("다음 심층보고는 2026년 12월 첫 주에 발행합니다. 미래 금융(디지털 위안화·토큰증권·탄소시장)도 심층보고 주제로 다룹니다.", "The next in-depth report will be published in the first week of December 2026. Future finance (the digital yuan, tokenised securities and carbon markets) is also among our in-depth topics.", "下一期深度报告将于2026年12月第一周发布。未来金融（数字人民币、代币化证券、碳市场）也是深度报告的主题。"))}</div>''', "alt")
    b += sec("video", "VIDEO & NEWSLETTER", L("영상·뉴스레터", "Video & Newsletter", "视频与通讯"),
             L("유튜브 채널 「안유화의 경제투자론」의 최신 영상을 바로 볼 수 있습니다. 매주 화요일 새 영상이 올라옵니다.", "Watch the latest from the YouTube channel right here. A new video goes up every Tuesday.", "可在此直接观看YouTube频道的最新视频，每周二更新。"),
             f'''<div class="player"><a href="{YOUTUBE}/videos" target="_blank" rel="noopener">{L("안유화의 경제투자론 최신 영상", "Latest videos on YouTube", "YouTube 最新视频")}<span>YOUTUBE</span></a>
<iframe src="https://www.youtube-nocookie.com/embed/videoseries?list=UUThwDMeuhkjOONCAIUiu4xg" title="{L("안유화의 경제투자론 최신 영상", "Latest videos", "最新视频")}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>{media_cards()}'''
             + f'<div class="sec-foot">{btn(L("영상 해설 읽기", "Read the video notes", "阅读视频解读"), P("videos"), "navy")}</div>'
             + cta_band(L("뉴스레터로 받아 보기", "Get it by email", "通过邮件接收"), L("월간 「중국경제포커스」를 이메일로 보내드립니다. 무료입니다.", "The monthly China Economy Focus, delivered free by email.", "月刊《中国经济聚焦》通过邮件免费发送。"), L("무료 구독하기", "Subscribe free", "免费订阅"), SUBSCRIBE, ext=True))
    b += f'<section class="sec tight"><div class="wrap"><p class="note">{L("본 채널의 자료는 정보 제공을 위한 것이며, 특정 종목·상품의 매수·매도 권유가 아닙니다.", "Material on this channel is for information only and is not a recommendation to buy or sell any security or product.", "本频道资料仅供参考，不构成任何证券或产品的买卖建议。")}</p></div></section>'
    return page("focus", title, lede, b, "focus")


# ── 기업 자문 ──────────────────────────────────────────────────
def advisory():
    C.slug = "advisory"
    title = L("기업 자문·컨설팅", "Business Advisory & Consulting", "企业咨询与顾问")
    lede = L("중국의 정책·시장·공급망 변화 앞에서 기업이 내려야 하는 전략적 결정을, 거시·산업·정책 분석으로 뒷받침합니다.",
             "We back the strategic decisions companies face amid shifts in China's policy, markets and supply chains with macro, industry and policy analysis.",
             "面对中国政策、市场与供应链的变化，以宏观、产业与政策分析支持企业的战略决策。")
    b = page_hero("advisory", "BUSINESS ADVISORY", title, lede)
    sv = "".join(f'<div class="card"><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in services())
    for ic, t, d in services():
        reg(t, d, P("advisory", "services"), "Advisory")
    do = [L("거시경제·산업·정책·공급망 분석", "Macro, industry, policy and supply-chain analysis", "宏观、产业、政策与供应链分析"),
          L("기업의 전략적 의사결정 지원", "Support for companies' strategic decisions", "支持企业的战略决策"),
          L("공개 자료와 적법한 조사에 기반한 자문", "Advice based on public sources and lawful research", "基于公开资料与合法调研的咨询")]
    dont = [L("종목 추천, 목표가, 매매 전략", "Stock picks, price targets, trading strategies", "荐股、目标价、交易策略"),
            L("자산 운용, 투자일임, 투자중개·주선", "Asset management, discretionary investment, brokerage", "资产管理、全权委托投资、投资中介"),
            L("M&A 중개·주선", "Brokering or arranging M&A transactions", "并购中介或撮合"),
            L("실사·전문가 네트워크형 조사, 비공개 데이터 수집", "Due-diligence or expert-network style investigation, or collecting non-public data", "尽职调查或专家网络式调查，以及收集非公开数据")]
    b += sec("services", "SERVICE AREAS", L("서비스 분야", "Service areas", "服务领域"), scope_note(),
             f'<div class="g3">{sv}</div><div class="g2" style="margin-top:24px"><div class="card"><h3>{L("자문 범위", "In scope", "服务范围")}</h3>{ticks(do)}</div>'
             f'<div class="card"><h3>{L("하지 않는 일", "Out of scope", "不提供的服务")}</h3>{ticks(dont, "ticks xs")}</div></div>')
    b += sec("process", "PROCESS", L("수행 프로세스", "Process", "工作流程"), process_lede(), process_steps(), "alt")
    themes = [L("중국의 정책 변화가 우리 산업에 주는 영향", "What a change in China's policy means for our industry", "中国政策变化对本行业的影响"),
              L("공급망에서 중국 의존이 큰 품목과 대안", "Items in our supply chain that depend heavily on China, and the alternatives", "供应链中高度依赖中国的品类及替代方案"),
              L("중국 시장의 리스크와 기회", "Risks and opportunities in the China market", "中国市场的风险与机遇")]
    adv_cases = ('<div class="card"><h3>' + L("수행한 자문", "Advisory work we have done", "已开展的咨询") + "</h3>"
                 + ticks(L(["한국 최대 식품그룹의 중국 투자 자문", "중국 1등 기업의 한국 투자와 자금조달 자문", "한국 해운회사의 글로벌 시장 분석", "한국 대기업의 중국 법인 정리 컨설팅"],
                           ["Advising Korea's largest food group on its investment in China", "Advising an industry-leading Chinese company on investing and raising capital in Korea", "Global market analysis for a Korean shipping company", "Consulting for a major Korean conglomerate on winding down its China subsidiary"],
                           ["为韩国最大的食品集团提供对华投资咨询", "为中国行业龙头企业提供在韩投资与融资咨询", "为韩国航运公司提供全球市场分析", "为韩国大企业提供在华法人清理咨询"]))
                 + '<p style="font-size:13.500px;color:var(--muted)">' + L("고객사 이름은 공개하지 않습니다.", "Client names are not disclosed.", "不公开客户名称。") + "</p></div>")
    b += sec("themes", "CASE THEMES", L("자문 주제", "Case themes", "咨询主题"),
             L("기업이 자주 마주하는 질문과 실제로 수행한 자문을 정리했습니다.", "The questions companies most often face, and advisory work we have carried out.", "这里整理了企业最常面对的问题以及我们实际开展的咨询。"),
             f'<div class="g2"><div class="card"><h3>{L("자주 받는 질문의 유형", "Typical questions", "常见问题类型")}</h3>{ticks(themes)}</div><div>{adv_cases}</div></div>')
    b += f'<section class="sec alt" id="inquiry"><div class="wrap"><div class="sec-head"><div class="eyebrow">INQUIRY</div><h2>{L("기업 문의", "Business inquiry", "企业咨询联系")}</h2><p>{L("회사명, 담당자, 관심 분야와 문의 내용을 알려 주세요.", "Tell us your company, contact person, area of interest and what you need.", "请告知公司名称、联系人、关注领域与咨询内容。")}</p></div>{cta_band(L("중국 관련 의사결정, 함께 검토합니다", "Let's review your China-related decision together", "涉华决策，我们一同研判"), L("기업 자문 문의 양식으로 연결됩니다.", "Opens the business advisory inquiry form.", "将进入企业咨询表单。"), L("기업 문의하기", "Business Inquiry", "提交企业咨询"), P("contact", "advisory"), flush=True)}</div></section>'
    return page("advisory", title, lede, b, "advisory")


# ── 교육·아카데미 ──────────────────────────────────────────────
def academy():
    C.slug = "academy"
    title = L("교육·아카데미", "Academy", "教育学院")
    lede = L("중국 경제와 정책, 디지털 금융을 주제로 한 교육 프로그램을 운영합니다.", "We run education programmes on China's economy and policy and on digital finance.", "我们开设以中国经济与政策、数字金融为主题的教育课程。")
    b = page_hero("academy", "ACADEMY", title, lede)
    progs = [("users", L("임원 과정", "Executive education", "高管课程"), L("경영진을 위한 중국 경제·정책 이해 과정", "Understanding China's economy and policy, for executives", "面向企业高管的中国经济与政策课程"), "executive"),
             ("factory", L("기업 맞춤 교육", "Corporate training", "企业定制培训"), L("기업의 산업과 과제에 맞춰 구성하는 교육", "Training tailored to a company's industry and agenda", "根据企业所在行业与课题定制的培训"), "corporate"),
             ("scale", L("금융기관 중국 리스크 과정", "China-risk programme for financial institutions", "金融机构中国风险课程"), L("금융기관을 위한 중국 리스크 이해 과정", "Understanding China risk, for financial institutions", "面向金融机构的中国风险课程"), "programs"),
             ("layers", L("디지털 금융 교육", "Digital finance training", "数字金融培训"), L("AI·디지털 금융 전문 교육", "Specialist training in AI and digital finance", "AI与数字金融专业培训"), "programs")]
    run_progs = [
        ("cap", L("디지털자산·AI 융합 최고위과정", "Digital Assets and AI Executive Programme", "数字资产·AI融合高层课程"),
         "<p>" + L("매일경제와 공동 주관합니다. 1·2기를 운영했고, 3기는 2027년 3월에 개강합니다.", "Co-organised with Maeil Business Newspaper. The 1st and 2nd classes have run; the 3rd opens in March 2027.", "与《每日经济》共同主办。已举办第1、2期，第3期将于2027年3月开课。") + "</p>", ""),
        ("users", L("강좌", "Courses", "讲座"),
         ticks(L(["알트코인 미래 설계반", "비트코인 30일 완전정복반", "안유화 LEP 100일 챌린지 모임반", "부의 곡선 AI에이전트 스쿨"],
                 ["Altcoin Future Design class", "Bitcoin 30-Day Mastery class", "An Yuhua LEP 100-Day Challenge group", "Wealth Curve AI Agent School"],
                 ["山寨币未来设计班", "比特币30天完全掌握班", "安玉花LEP 100天挑战班", "《财富曲线》AI智能体学院"]))
         + '<p style="font-size:13px;color:var(--muted)">' + L("강좌는 교육을 위한 것이며 투자 권유가 아닙니다.", "Courses are for education and are not investment advice.", "课程以教育为目的，不构成投资建议。") + "</p>", ""),
        ("globe", L("중국 탐방", "China study tours", "中国考察"),
         "<p>" + L("상해·항주, 심천·베이징, 북경 등 지역의 1등 기업을 탐방합니다.", "Visits to leading companies in Shanghai and Hangzhou, Shenzhen and Beijing, and other regions.", "走访上海·杭州、深圳·北京等地区的龙头企业。") + "</p>", ""),
    ]
    pc_run = "".join(f'<div class="card"><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3>{d}</div>' for ic, t, d, a in run_progs)
    pc = "".join(f'<div class="card"><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d, a in progs)
    for ic, t, d, a in progs:
        reg(t, d, P("academy", a), "Academy")
    wait = (L("신청과 문의는 ", "To apply or ask a question, use the ", "报名与咨询请通过") + '<a href="' + P("contact") + '">' + L("문의 페이지", "contact page", "咨询页面") + "</a>"
            + L(" 또는 대표 전화 ", " or call ", "或致电") + '<a href="tel:+8225170866">02-517-0866</a>'
            + L("으로 받습니다. 대상과 인원, 희망 주제와 시기를 알려 주시면 과정 구성을 상담해 드립니다.", ". Tell us the audience, headcount, topics and timing you have in mind and we will discuss the format.", "。请告知对象、人数、希望的主题与时间，我们将就课程方案进行沟通。"))
    wait_box = '<p class="note" style="font-size:15px">' + wait + "</p>"
    b += sec("programs", "PROGRAMS", L("프로그램", "Programs", "课程项目"), "", f'<h3 style="font-size:20px;margin:0 0 16px">{L("운영 중인 과정", "Programmes now running", "正在开设的课程")}</h3><div class="g3">{pc_run}</div><h3 style="font-size:20px;margin:40px 0 16px">{L("기업·기관 맞춤 과정", "Tailored programmes for companies and institutions", "面向企业与机构的定制课程")}</h3><div class="g4">{pc}</div><div style="margin-top:24px">{wait_box}</div>'
             f'<p class="note" style="margin-top:14px">{L("안유화독서투자클럽, 유튜브 채널과 연결해 운영합니다.", "Run in connection with the An Yuhua Reading & Investment Club and the YouTube channel.", "与安玉花读书投资俱乐部及YouTube频道联动运营。")}</p>')
    b += sec("executive", "EXECUTIVE EDUCATION", L("임원 과정", "Executive education", "高管课程"),
             L("경영진이 중국의 정책과 시장을 읽는 기준을 갖추도록 돕는 과정입니다.", "A programme that gives executives a framework for reading China's policy and markets.", "帮助企业高管建立解读中国政策与市场的框架。"), wait_box, "alt")
    b += sec("corporate", "CORPORATE TRAINING", L("기업 맞춤 교육", "Corporate training", "企业定制培训"),
             L("교육 대상과 인원, 희망 주제와 시기를 알려 주시면 맞춤 구성을 상담합니다.", "Tell us the audience and headcount, the topics and the timing you have in mind, and we will discuss a tailored format.", "请告知培训对象与人数、希望的主题与时间，我们将就定制方案进行沟通。"), wait_box)
    b += f'<section class="sec alt" id="inquiry"><div class="wrap"><div class="sec-head"><div class="eyebrow">INQUIRY</div><h2>{L("교육 문의", "Training inquiry", "培训咨询")}</h2></div>{cta_band(L("교육 상담을 신청하세요", "Ask about training", "预约培训咨询"), L("교육 문의 양식으로 연결됩니다.", "Opens the training inquiry form.", "将进入培训咨询表单。"), L("교육 문의하기", "Training Inquiry", "提交培训咨询"), P("contact", "academy"), flush=True)}</div></section>'
    return page("academy", title, lede, b, "academy")


# ── 글로벌 협력 ────────────────────────────────────────────────
def global_():
    C.slug = "global"
    title = L("글로벌 협력", "Global Network", "全球合作")
    lede = L("해외 연구기관·전문가와의 공동연구, 포럼, 특별기고 등 협력의 창구를 엽니다.", "A window for cooperation with overseas institutes and experts: joint research, forums and contributed articles.", "面向海外研究机构与专家，开放联合研究、论坛与特约撰稿等合作渠道。")
    b = page_hero("global", "GLOBAL NETWORK", title, lede)
    kinds = [("doc", L("공동연구", "Joint research", "联合研究"), L("연구 주제를 함께 정하고 결과를 공동으로 발간합니다.", "Agreeing a research topic together and publishing the results jointly.", "共同确定研究课题并联合发布成果。")),
             ("users", L("전문가 교류·기고", "Expert exchange & contributions", "专家交流与撰稿"), L("중국 학자 특별기고 등 전문가의 글과 대담을 싣습니다.", "Contributed articles and conversations with experts, including special contributions from Chinese scholars.", "刊载中国学者特约撰稿等专家文章与对谈。")),
             ("cal", L("포럼·세미나", "Forums & seminars", "论坛与研讨会"), L("공동 포럼과 세미나를 기획합니다.", "Planning joint forums and seminars.", "策划联合论坛与研讨会。"))]
    kc = "".join(f'<div class="card"><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in kinds)
    coop_types = ('<div class="card"><h3>' + L("협력의 유형", "Types of cooperation", "合作类型") + "</h3>"
                  + ticks(L(["언론사와 교육과정 공동 주관", "중국 1등 기업 현지 탐방", "지방자치단체·언론사가 여는 포럼과 아카데미 강연", "한국과 중국 기업의 상호 투자 자문"],
                            ["Co-organising education programmes with media companies", "On-site visits to leading Chinese companies", "Lectures at forums and academies hosted by local governments and media", "Advisory on cross-border investment between Korean and Chinese companies"],
                            ["与媒体共同主办教育课程", "实地走访中国龙头企业", "在地方政府与媒体主办的论坛和学院演讲", "为韩中企业的相互投资提供咨询"]))
                  + '<p style="font-size:13.500px;color:var(--muted)">' + L("협력기관의 이름은 해당 기관의 동의를 받은 경우에만 공개합니다.", "Partner names are published only with the partner's consent.", "合作机构名称仅在获得对方同意后公开。") + "</p></div>")
    b += sec("partners", "PARTNERS", L("협력기관", "Partners", "合作机构"), "",
             coop_types
             + f'<h3 style="font-size:20px;margin:36px 0 16px">{L("협력 유형", "Ways to cooperate", "合作形式")}</h3><div class="g3">{kc}</div>'
             + f'<div class="card" style="margin-top:24px"><div class="type-h"><h3>{L("영문 분기 노트 「Korea Sensor」", "Korea Sensor — English quarterly note", "英文季度简报 Korea Sensor")}</h3>{tag_date("2026년 12월 15일 첫 호", "First issue 15 Dec 2026", "2026年12月15日首期")}</div><p>{L("중국 정책의 신호가 한국의 숫자에 먼저 나타나는 지점을, 해외 독자를 위해 영문으로 정리하는 분기 노트입니다. 해외 리서치 기관과의 파트너 유통을 준비합니다.", "A quarterly note in English, for overseas readers, on where the signal of China policy shows up first in Korean numbers. Distribution through overseas research partners is in preparation.", "面向海外读者的英文季度简报，梳理中国政策信号最先体现在韩国数字上的环节。正在筹备通过海外研究机构合作发行。")}</p></div>')
    b += sec("experts", "EXPERTS", L("전문가", "Experts", "专家"), "", ('<p class="note" style="font-size:15px">' + L("중국 학자 특별기고를 2027년 1분기부터 분기에 1편씩 싣습니다(공개 분석만).", "From the first quarter of 2027 we will carry one special contribution a quarter from Chinese scholars (public analysis only).", "自2027年第一季度起，每季度刊登一篇中国学者特约稿（仅限公开分析）。") + "</p>"), "alt")
    b += sec("events", "EVENTS & FORUMS", L("포럼·행사", "Events & forums", "论坛与活动"), "", f'''<div class="types"><div class="type"><div class="type-h"><h3>{icon("cal", 20)}{L("연례 중국 전망 포럼", "Annual China outlook forum", "年度中国展望论坛")}</h3>{tag_date("2026년 12월 24일", "24 Dec 2026", "2026年12月24日")}</div><p>{L("한 해의 중국 전망을 나누는 연례 포럼", "An annual forum on the year's outlook for China", "分享年度中国展望的年度论坛")}</p></div>
<div class="type"><div class="type-h"><h3>{icon("users", 20)}{L("분기 경영진 브리핑", "Quarterly executive briefing", "季度管理层简报")}</h3>{tag_date("2027년 1월 15일", "15 Jan 2027", "2027年1月15日")}</div><p>{L("경영진을 위한 비공개 분기 브리핑", "A closed-door quarterly briefing for management", "面向管理层的季度闭门简报")}</p></div></div>
<div style="margin-top:14px">''' + events_list() + "</div>")
    b += f'<section class="sec alt" id="inquiry"><div class="wrap"><div class="sec-head"><div class="eyebrow">COOPERATION</div><h2>{L("협력 문의", "Cooperation inquiry", "合作咨询")}</h2><p>{L("영어·중국어 문의도 받습니다.", "Inquiries in English and Chinese are welcome.", "欢迎以英文或中文联系。")}</p></div>{cta_band(L("협력을 제안해 주세요", "Propose a partnership", "欢迎提出合作意向"), L("국제협력 문의 양식으로 연결됩니다.", "Opens the cooperation inquiry form.", "将进入合作咨询表单。"), L("협력 제안하기", "Partnership", "提交合作意向"), P("contact", "global"), flush=True)}</div></section>'
    return page("global", title, lede, b, "global")


# ── 뉴스·자료 ──────────────────────────────────────────────────


def news():
    C.slug = "news"
    title = L("뉴스·자료", "News & Insights", "新闻与资料")
    lede = L("기관 소식, 언론·영상, 연구소장의 판단과 자료를 한곳에 모읍니다.", "Institute news, media, the Director's judgments and publications in one place.", "机构动态、媒体与视频、所长观点及资料汇集于此。")
    b = page_hero("news", "NEWS & INSIGHTS", title, lede)
    b += sec("news", "NEWS", L("기관 소식", "News", "机构动态"), "", notices())
    b += sec("media", "MEDIA", L("언론·미디어", "Media", "媒体"), L("방송과 영상, 팟캐스트로 중국과 세계 경제를 설명합니다.", "Explaining China and the world economy on air, on video and in podcast.", "通过电视节目、视频与播客解读中国与世界经济。"), media_cards() + channels()
             + f'<p class="note" style="margin-top:18px">{L("칼럼은 내일신문 「금요진단」에 연재하고 있습니다.", "Her current newspaper column runs in Naeil Shinmun on Fridays.", "目前在《明日新闻》周五专栏连载。")} <a href="{NAEIL_SEARCH}" target="_blank" rel="noopener">{L("최근 글 보기", "Latest pieces", "查看最新文章")}</a> · <a href="{P("research", "reports")}">{L("연구·칼럼 목록", "Research & commentary", "研究与评论")}</a></p>', "alt")
    reg(L("연구소장's Insight", "Director's Insight", "所长观点"), L("중국을 읽는 원칙과 판단 기록", "Principles for reading China and the judgment record", "解读中国的原则与判断记录"), P("insight"), "Insight")
    b += f'''<section class="sec dark" id="insight"><div class="wrap"><div class="sec-head"><div class="eyebrow">{L("연구소장's Insight", "Director's Insight", "所长观点")}</div>
<h2>{L("판단의 기준과 기록", "Standards and record of judgment", "判断的标准与记录")}</h2><p>{L("중국을 읽는 원칙, 판단 기록, 대표저서를 모았습니다.", "Principles for reading China, the judgment record, and selected books.", "汇集解读中国的原则、判断记录与代表著作。")}</p></div>
{record_box()}<div class="sec-foot">{btn(L("Insight 읽기", "Read Insight", "阅读观点"), P("insight"))}</div></div></section>'''
    pubs = [("doc", L("연구보고서·기고", "Research reports & commentary", "研究报告与评论"), L("보고서와 언론 기고 목록", "Reports and newspaper columns", "报告与媒体专栏"), P("research", "reports"), False),
            ("cal", L("월간 「중국경제포커스」 지난 호", "China Economy Focus — past issues", "月刊《中国经济聚焦》往期"), "chinamacro.kr", ARCHIVE, True),
            ("layers", L("대표저서", "Selected books", "代表著作"), L("『부의 곡선』, 『더 플로』", "Two books in Korean", "两部韩文著作"), P("insight", "books"), False)]
    pc = "".join(f'<a class="card" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if x else ""}><div class="badge-ico">{icon(ic, 26)}</div><h3>{t}</h3><p>{d}</p></a>' for ic, t, d, h, x in pubs)
    b += sec("publications", "PUBLICATIONS", L("자료실", "Publications", "资料室"), "", f'<div class="g3">{pc}</div>')
    return page("news", title, lede, b, "news")


# ── 연구소장's Insight ─────────────────────────────────────────
def insight():
    C.slug = "insight"
    title = L("연구소장's Insight", "Director's Insight", "所长观点")
    lede = L("안유화 원장이 중국을 읽는 기준과 판단을 기록하는 공간입니다.", "Where Professor An Yuhua records the standards and judgments she uses to read China.", "安玉花院长记录其解读中国的标准与判断的栏目。")
    subs = [("insight", L("메시지", "Message", "寄语")), ("principles", L("중국을 읽는 원칙", "Principles", "解读中国的原则")), ("record", L("판단 기록", "Judgment record", "判断记录")), ("books", L("대표저서", "Selected books", "代表著作"))]
    b = page_hero("insight", "DIRECTOR'S INSIGHT", title, lede, subs)
    b += message_section("#principles", SUBSCRIBE, focus_ext=True)
    b += sec("principles", "PRINCIPLES", L("중국을 읽는 원칙", "Principles for reading China", "解读中国的原则"), principles_lede(),
             principles_grid() + f'<div class="sec-foot">{more(L("분석 프레임: 중국 경제는 어떻게 작동하는가", "Framework: how China\'s economy works", "分析框架：中国经济如何运行"), P("research", "framework"))}</div>', "alt")
    b += sec("record", "JUDGMENT", L("판단·한마디", "Judgments", "判断与短评"),
             L("판단은 기록될 때 검증할 수 있습니다. 기준일과 근거, 무효화 조건을 함께 남기고 결과를 공개 성적표로 쌓아 갑니다.", "A judgment can be tested only if it is recorded. Each is logged with its date, evidence and invalidation conditions, and the results build into a public scorecard.", "判断只有被记录下来才能被检验。每一次判断都记录基准日、依据与失效条件，并将结果累积为公开成绩单。"),
             record_box(light=True))
    b += sec("books", "BOOKS", L("대표저서", "Selected books", "代表著作"), books_lede(), books_html(), "alt")
    return page("insight", title, lede, b, "news")


# ── 영상 해설(요약 무료 · 전문 유료) ────────────────────────────
def paid_box():
    return f'''<div class="lock"><div><h4>{icon("shield", 18)}{L("대본 전문 · 근거 자료 묶음", "Full script and evidence pack", "完整文稿与资料包")} <span class="tag-soon">{L("유료", "Paid", "付费")}</span></h4>
<p>{L("요약은 누구나 볼 수 있습니다. 대본 전문과 원문 근거·숫자 출처를 묶은 자료는 유료로 제공합니다.", "The summary is open to all. The full script, with the source documents and data behind it, is a paid service.", "摘要面向所有人开放；完整文稿及其背后的原文依据与数据来源为付费内容。")}</p></div>
{btn(L("유료 구독 문의", "Ask about paid access", "咨询付费订阅"), P("contact", "general"), "navy")}</div>'''


def episode_html(ep):
    import re as _re
    m = _re.search(r"(?:v=|youtu\.be/|embed/)([\w-]{6,})", ep.get("youtube", ""))
    vid = m.group(1) if m else ""
    thumb = (f'<a class="ep-thumb" href="{e(ep["youtube"])}" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()">'
             f'<span>{icon("play", 30)}{L("영상 보기", "Watch", "观看视频")}</span></a>') if ep.get("youtube") else ""
    pts = "".join(f"<li>{e(x)}</li>" for x in ep.get("points", []))
    paras = "".join(f"<p>{e(x.strip())}</p>" for x in ep.get("summary", "").split("\n\n") if x.strip())
    imp = f'<div class="ep-box"><b>{L("한국 시사점", "Implications for Korea", "对韩国的启示")}</b><p>{e(ep["implication"])}</p></div>' if ep.get("implication") else ""
    j = ep.get("judgment")
    jud = (f'<div class="ep-box gold"><b>{L("판단", "Judgment", "判断")} · {L("기준일", "as of", "基准日")} {e(j["asof"])}</b><p>{e(j["text"])}</p>'
           f'<p class="note">{L("무효화 조건", "Invalidation conditions", "失效条件")}: {e(j["invalid"])}</p></div>') if j else ""
    src = ""
    if ep.get("sources"):
        src = f'<p class="note">{L("출처", "Sources", "来源")}: ' + " · ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a>' if u else e(t) for t, u in ep["sources"]) + "</p>"
    reg(ep["title"], " ".join(ep.get("points", [])), P("videos", "ep-" + ep["date"]), L("영상 해설", "Video notes", "视频解读"))
    return f'''<article class="ep card" id="ep-{e(ep["date"])}" lang="ko"><div class="ep-head"><div><time>{e(ep["date"])}</time><h3>{e(ep["title"])}</h3></div>{thumb}</div>
<ul class="ticks">{pts}</ul><div class="ep-sum">{paras}</div>{imp}{jud}{src}{paid_box()}</article>'''


def videos():
    from episodes import EPISODES
    C.slug = "videos"
    title = L("영상 해설", "Video notes", "视频解读")
    lede = L("유튜브 「안유화경제투자론」의 매주 영상을 글로 정리합니다. 핵심 요지와 요약, 한국 시사점, 판단을 무료로 싣습니다.",
             "Each week's video from the YouTube channel, written up: key points, a summary, implications for Korea and the judgment — free to read.",
             "将YouTube频道每周的视频整理成文：核心要点、摘要、对韩国的启示与判断，均可免费阅读。")
    b = page_hero("videos", "VIDEO NOTES", title, lede, [])
    how = [(L("핵심 요지 3줄", "Three key points", "三条核心要点"), L("영상을 보지 않아도 결론을 알 수 있게", "The conclusion, even without watching", "不看视频也能了解结论")),
           (L("대본 요약", "Script summary", "文稿摘要"), L("주장과 근거의 흐름을 글로", "The line of argument and evidence, in writing", "以文字呈现论点与依据的脉络")),
           (L("한국 시사점", "Implications for Korea", "对韩国的启示"), L("한국 기업·기관의 결정에 주는 뜻", "What it means for decisions in Korea", "对韩国企业与机构决策的意义")),
           (L("판단과 무효화 조건", "Judgment and invalidation", "判断与失效条件"), L("기준일과 함께 남기고 나중에 채점", "Logged with a date and graded later", "连同基准日记录，日后评分"))]
    how_html = '<ol class="steps">' + "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in how) + "</ol>"
    if EPISODES:
        note = "" if C.lang == "ko" else f'<p class="note" style="margin-bottom:18px">{L("", "Episode notes are in Korean.", "各期内容为韩文。")}</p>'
        body = note + '<div class="eps">' + "".join(episode_html(x) for x in EPISODES) + "</div>"
    else:
        body = soon(L("첫 영상 해설을 준비하고 있습니다. 매주 영상이 공개되면 이곳에 한 편씩 쌓입니다.", "The first video note is in preparation. One will be added here each week as the video is published.", "首期视频解读正在准备中，此后每周随视频发布在此更新一篇。")) + f'<div style="margin-top:20px">{paid_box()}</div>'
    b += sec("list", "EPISODES", L("회차별 해설", "Notes by episode", "各期解读"), "", body)
    b += sec("how", "FORMAT", L("한 편에 담는 것", "What each note contains", "每期包含的内容"), "", how_html
             + f'<div class="sec-foot">{btn(L("유튜브 채널 보기", "YouTube channel", "YouTube 频道"), YOUTUBE, "ghost", ext=True)}{more(L("판단 기록 보기", "Judgment record", "查看判断记录"), P("insight", "record"))}</div>', "alt")
    b += f'<section class="sec tight"><div class="wrap"><p class="note">{L("영상과 해설은 정보 제공을 위한 것이며, 특정 종목·상품의 매수·매도 권유가 아닙니다.", "Videos and notes are for information only and are not a recommendation to buy or sell any security or product.", "视频与解读仅供参考，不构成任何证券或产品的买卖建议。")}</p></div></section>'
    return page("videos", title, lede, b, "focus")


# ── 문의 ───────────────────────────────────────────────────────
def field(name, label, kind="text", req=False, opt=False, full=False, options=None, ph=""):
    r = " required" if req else ""
    tail = f'<i>({L("선택", "optional", "选填")})</i>' if opt else ("<i>*</i>" if req else "")
    idn = f"f-{C.form}-{name}"
    common = f'id="{idn}" name="{name}" data-label="{e(label)}"{r}'
    if kind == "select":
        ctl = f'<select {common}>' + "".join(f"<option>{o}</option>" for o in options) + "</select>"
    elif kind == "textarea":
        ctl = f'<textarea {common} placeholder="{e(ph)}"></textarea>'
    else:
        ac = {"email": ' autocomplete="email"', "tel": ' autocomplete="tel"'}.get(kind, "")
        ctl = f'<input type="{kind}" {common}{ac} placeholder="{e(ph)}">'
    return f'<div class="field{" full" if full else ""}"><label for="{idn}">{label}{tail}</label>{ctl}</div>'


def form(fid, subject, fields, hidden=True):
    C.form = fid
    consent = L("문의 응대를 위한 개인정보(이름·이메일 등) 수집·이용에 동의합니다.", "I agree to the collection and use of my personal information (name, email, etc.) for the purpose of responding to this inquiry.", "我同意为回复本次咨询而收集和使用我的个人信息（姓名、邮箱等）。")
    return f'''<form class="form" data-form="{fid}" data-subject="{e(subject)}" data-to="{MAIL}"{" hidden" if hidden else ""} novalidate>
  {"".join(field(*f[0], **f[1]) for f in fields)}
  <label class="consent"><input type="checkbox" required><span>{consent} <a href="{P("policy", "privacy")}">{L("개인정보 안내", "Privacy notice", "隐私说明")}</a></span></label>
  <div class="form-act"><button class="btn btn-navy" type="submit">{L("문의 내용 정리하기", "Prepare my inquiry", "整理咨询内容")} {icon("arrow", 16)}</button>
    <span class="note">{L("이 사이트는 문의 내용을 저장하지 않습니다. 정리된 내용을 메일로 보내 주세요.", "This site does not store your inquiry. Please send the prepared text by email.", "本网站不保存咨询内容，请将整理后的内容通过邮件发送。")}</span></div>
  <div class="form-out" hidden><strong>{L("아직 전송되지 않았습니다.", "Not sent yet.", "尚未发送。")}</strong> {L("아래 버튼으로 메일 앱을 열어 보내시거나, 내용을 복사해", "Open your mail app with the button below, or copy the text and send it to", "请点击下方按钮打开邮件应用发送，或复制内容发送至")} <span class="mailto">{MAIL}</span>{L("로 보내 주세요.", ".", "。")}
    <pre id="out-{fid}"></pre>
    <div class="row-btns"><a class="btn btn-gold mail-open" href="mailto:{MAIL}">{L("메일 앱으로 보내기", "Open in mail app", "用邮件应用发送")} {icon("mail", 16)}</a>
    <button type="button" class="copy dk" data-copy="#out-{fid}" data-done="{L("복사됨", "Copied", "已复制")}">{L("내용 복사", "Copy text", "复制内容")}</button></div></div>
</form>'''


def contact():
    C.slug = "contact"
    title = L("문의", "Contact", "联系我们")
    lede = L("기업 자문, 교육, 국제협력, 일반 문의를 목적별로 받습니다. 필요한 최소한의 정보만 여쭙니다.", "Business advisory, training, international cooperation and general inquiries, each with its own form. We ask only for the minimum we need.", "企业咨询、培训、国际合作与一般咨询，按类别受理。我们只收集必要的最少信息。")
    b = page_hero("contact", "CONTACT", title, lede)
    F = lambda *a, **k: (a, k)
    msg = L("문의 내용", "Your inquiry", "咨询内容")
    email = L("이메일", "Email", "邮箱")
    person = L("담당자", "Contact person", "联系人")
    forms = {
        "advisory": (L("기업 자문", "Business advisory", "企业咨询"), L("CSAI 기업 자문 문의", "CSAI business advisory inquiry", "CSAI 企业咨询"), [
            F("org", L("회사명", "Company", "公司名称"), req=True), F("dept", L("부서·직책", "Department / title", "部门·职务")),
            F("name", person, req=True), F("email", email, "email", req=True), F("tel", L("연락처", "Phone", "电话"), "tel", opt=True),
            F("area", L("관심 분야", "Area of interest", "关注领域"), "select", options=[s[1] for s in services()] + [L("기타", "Other", "其他")]),
            F("msg", msg, "textarea", req=True, full=True)]),
        "academy": (L("교육", "Training", "培训"), L("CSAI 교육 문의", "CSAI training inquiry", "CSAI 培训咨询"), [
            F("org", L("기관·회사명", "Organisation", "机构·公司名称"), req=True), F("name", person, req=True), F("email", email, "email", req=True),
            F("who", L("교육 대상·인원", "Audience / headcount", "培训对象·人数"), opt=True), F("topic", L("희망 주제", "Preferred topic", "希望的主题")),
            F("when", L("희망 시기", "Preferred timing", "希望的时间")), F("msg", msg, "textarea", req=True, full=True)]),
        "global": (L("국제협력", "Cooperation", "国际合作"), L("CSAI 국제협력 문의", "CSAI cooperation inquiry", "CSAI 国际合作咨询"), [
            F("org", L("기관명", "Institution", "机构名称"), req=True), F("country", L("국가·지역", "Country / region", "国家·地区")),
            F("name", person, req=True), F("email", email, "email", req=True), F("area", L("협력 희망 분야", "Field of cooperation", "希望合作的领域")),
            F("msg", L("제안 내용", "Your proposal", "合作提案"), "textarea", req=True, full=True)]),
        "general": (L("일반 문의", "General", "一般咨询"), L("CSAI 일반 문의", "CSAI general inquiry", "CSAI 一般咨询"), [
            F("kind", L("문의 유형", "Type of inquiry", "咨询类型"), "select", options=[L("강연·인터뷰 요청", "Speaking / interview request", "演讲·采访邀请"), L("영상 해설 유료 구독", "Paid access to video notes", "视频解读付费订阅"), L("콘텐츠·구독", "Content / subscription", "内容·订阅"), L("사이트 이용", "Using this site", "网站使用"), L("기타", "Other", "其他")]),
            F("name", L("이름 또는 담당자", "Name", "姓名或联系人"), req=True), F("email", email, "email", req=True),
            F("subject", L("제목", "Subject", "标题"), req=True), F("msg", L("내용", "Message", "内容"), "textarea", req=True, full=True)]),
    }
    tabs = "".join(f'<button type="button" role="tab" data-tab="{k}" id="{k}" aria-selected="{str(i == 0).lower()}">{v[0]}</button>' for i, (k, v) in enumerate(forms.items()))
    fhtml = "".join(form(k, v[1], v[2], hidden=(i > 0)) for i, (k, v) in enumerate(forms.items()))
    side = f'''<div class="contact-side">
  <div class="card"><h3>{icon("mail", 20)}{L("이메일", "Email", "邮箱")}</h3><p><a class="mailto" href="mailto:{MAIL}">{MAIL}</a></p><p>{L("양식 없이 직접 메일을 보내셔도 됩니다.", "You can also email us directly without the form.", "也可不填表单，直接发送邮件。")}</p></div>
  <div class="card"><h3>{icon("shield", 20)}{L("개인정보 원칙", "Privacy", "隐私原则")}</h3><p>{L("문의 단계에서는 필요한 최소 정보만 받습니다. 입력한 내용은 이 사이트에 저장되지 않고, 보내시는 메일로만 전달됩니다.", "At the inquiry stage we ask only for the minimum. What you type is not stored on this site; it travels only in the email you send.", "咨询阶段仅收集必要的最少信息。您填写的内容不会保存在本网站，只会通过您发送的邮件传达。")}</p>{more(L("자세히", "Details", "详情"), P("policy", "privacy"))}</div>
  <div class="card"><h3>{icon("pin", 20)}{L("대표 전화", "Phone", "电话")}</h3><p><a href="tel:+8225170866">02-517-0866</a></p></div>
</div>'''
    b += sec("form", "INQUIRY", L("문의 양식", "Inquiry form", "咨询表单"), L("문의 유형을 고른 뒤 내용을 적어 주세요.", "Choose the type of inquiry, then fill in the details.", "请先选择咨询类型，再填写内容。"),
             f'<div class="contact-grid"><div><div class="tabs" role="tablist">{tabs}</div>{fhtml}</div>{side}</div>')
    return page("contact", title, lede, b, "")


# ── 정책 ───────────────────────────────────────────────────────
def policy():
    C.slug = "policy"
    title = L("개인정보·이용 안내", "Privacy & Terms", "隐私与使用说明")
    lede = L("개인정보 처리방침과 이용약관은 법률 검토를 거쳐 정식 게시합니다. 아래는 현재 적용되는 원칙입니다.", "The formal privacy policy and terms of use will be posted after legal review. The principles below apply for now.", "正式的隐私政策与使用条款将在法律审核后发布。以下为目前适用的原则。")
    subs = [("privacy", L("개인정보", "Privacy", "隐私")), ("terms", L("이용약관", "Terms", "使用条款")), ("disclaimer", L("면책·저작권", "Disclaimer & copyright", "免责与版权"))]
    b = page_hero("policy", "POLICY", title, lede, subs)
    li = lambda xs: "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
    b += sec("privacy", "PRIVACY", L("개인정보 안내", "Privacy notice", "隐私说明"), "", '<div class="prose">' + soon(L("정식 개인정보 처리방침(보유기간·파기 절차·위탁 처리 여부 포함)은 검토 후 게시합니다.", "The formal privacy policy — including retention period, destruction procedure and any outsourcing — will be posted after review.", "正式的隐私政策（包括保存期限、销毁程序及是否委托处理）将在审核后发布。")) + f'<h3>{L("현재 적용되는 원칙", "Principles that apply now", "目前适用的原则")}</h3>' + li([
        L("문의 단계에서는 응대에 필요한 최소한의 정보만 받습니다.", "At the inquiry stage we collect only the minimum needed to respond.", "咨询阶段仅收集回复所需的最少信息。"),
        L("문의 양식에 입력한 내용은 이 사이트에 저장되지 않습니다. 방문자가 직접 보내는 이메일로만 전달됩니다.", "What you type in the inquiry form is not stored on this site. It is delivered only in the email you send yourself.", "咨询表单中填写的内容不会保存在本网站，只会通过您亲自发送的邮件传达。"),
        L("뉴스레터 구독은 외부 구독 페이지(스티비)에서 이루어집니다.", "Newsletter subscription takes place on an external subscription page (Stibee).", "通讯订阅在外部订阅页面（Stibee）进行。"),
        f'{L("개인정보 관련 문의:", "Privacy questions:", "隐私相关咨询：")} <span class="mailto">{MAIL}</span>']) + "</div>")
    b += sec("terms", "TERMS", L("이용약관", "Terms of use", "使用条款"), "", '<div class="prose">' + soon(L("이용약관은 검토 후 게시합니다.", "Terms of use will be posted after review.", "使用条款将在审核后发布。")) + "</div>", "alt")
    b += sec("disclaimer", "DISCLAIMER", L("면책·저작권", "Disclaimer & copyright", "免责与版权"), "", '<div class="prose">' + li([
        L("본 사이트의 내용은 정보 제공을 위한 것이며, 특정 종목·상품의 매수·매도 권유나 투자 자문이 아닙니다.", "Content on this site is for information only. It is not investment advice or a recommendation to buy or sell any security or product.", "本网站内容仅供参考，不构成任何证券或产品的买卖建议或投资咨询。"),
        L("CSAI는 거시경제·산업·정책·공급망 분석과 기업의 전략적 의사결정 지원을 하며, 자산 운용·투자일임·투자중개를 하지 않습니다.", "CSAI provides macro, industry, policy and supply-chain analysis and supports companies' strategic decisions. It does not manage assets, exercise investment discretion or broker investments.", "CSAI提供宏观、产业、政策与供应链分析，并支持企业的战略决策；不从事资产管理、全权委托投资或投资中介。"),
        L("사이트에 실린 글·도표·영상의 저작권은 CSAI 또는 원저작자에게 있습니다. 인용할 때는 출처를 밝혀 주세요.", "Copyright in the text, charts and video on this site belongs to CSAI or the original authors. Please cite the source when quoting.", "本网站所载文字、图表与视频的版权归CSAI或原作者所有。引用时请注明出处。")]) + "</div>")
    return page("policy", title, lede, b, "")
