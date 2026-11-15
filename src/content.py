# -*- coding: utf-8 -*-
"""여러 페이지가 함께 쓰는 콘텐츠: 원칙, 약력, 분석 프레임, 보고서 목록, 영상, 저서 등.
기존 안유화 교수 홈페이지의 내용은 모두 여기에 원문대로 들어 있다."""
from core import *

SOON = lambda: L("준비 중", "Coming soon", "筹备中")
NAEIL_SEARCH = "https://search.naver.com/search.naver?where=news&amp;query=%EC%95%88%EC%9C%A0%ED%99%94+%EA%B8%88%EC%9A%94%EC%A7%84%EB%8B%A8"


def ticks(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def kv(rows):
    return '<dl class="kv">' + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows) + "</dl>"


def principles():
    """중국을 읽는 원칙(초안, 원장 감수 후 확정)."""
    return [
        ("1.1", L("정책 문서를 시장 데이터보다 먼저 읽는다", "Read policy documents before market data", "先读政策文件，再看市场数据"),
         L("중국에서 정책은 가격의 선행지표다. 문장의 변화, 특히 수식어의 강도 변화를 추적한다.",
           "In China, policy leads prices. Track changes in wording, especially in the strength of modifiers.",
           "在中国，政策是价格的先行指标。跟踪措辞的变化，尤其是修饰语力度的变化。")),
        ("1.2", L("숫자는 반드시 출처와 함께 말한다", "Never quote a number without its source", "说数字，必带出处"),
         L("국가통계국, 인민은행, 해관총서의 원자료를 기준으로 하고, 추정은 추정이라고 밝힌다.",
           "Work from the primary data of the NBS, the PBoC and Customs, and label estimates as estimates.",
           "以国家统计局、人民银行、海关总署的原始数据为准；是估算，就说明是估算。")),
        ("1.3", L("부채는 총량보다 위치를 본다", "Look at where debt sits, not only how much", "看债务的位置，而不只是总量"),
         L("같은 부채라도 중앙·지방·기업·가계 중 어디에 있느냐에 따라 위험의 성격이 달라진다.",
           "The same debt carries a different risk depending on whether it sits with the central government, local governments, firms or households.",
           "同样的债务，落在中央、地方、企业还是居民部门，风险的性质各不相同。")),
        ("1.4", L("중국을 하나의 시장으로 보지 않는다", "Do not treat China as one market", "不把中国看作单一市场"),
         L("31개 성은 각기 다른 경제다. 지역별 재정 체력과 산업 구조를 따로 읽는다.",
           "Its 31 provinces are different economies. Read each region's fiscal strength and industrial structure separately.",
           "31个省份是各不相同的经济体，要分别解读各地的财政实力与产业结构。")),
        ("1.5", L("낙관과 비관 모두 검증 대상이다", "Optimism and pessimism are both to be tested", "乐观与悲观，都需要检验"),
         L("'중국 붕괴론'과 '중국 필승론'은 같은 오류다. 데이터가 말하는 만큼만 말한다.",
           "“China will collapse” and “China always wins” are the same error. Say only as much as the data says.",
           "“中国崩溃论”与“中国必胜论”是同一种错误。数据说多少，就说多少。")),
        ("1.6", L("모든 분석은 한국의 질문으로 돌아온다", "Every analysis returns to the Korean question", "所有分析都回到韩国的问题"),
         L("중국의 변화가 한국의 기업·투자자·정책에 무엇을 뜻하는지 답하지 못하면 분석은 끝나지 않은 것이다.",
           "If it cannot say what China's change means for Korean companies, investors and policy, the analysis is not finished.",
           "如果答不出中国的变化对韩国的企业、投资者和政策意味着什么，分析就还没有完成。")),
    ]


def values():
    return [
        ("target", L("판단", "Judgment", "判断"), "Judgment",
         L("정책 문서와 데이터를 근거로 판단을 내리고, 기준일과 근거를 남겨 나중에 검증합니다.",
           "We form judgments from policy documents and data, and log the date and evidence so they can be checked later.",
           "以政策文件和数据为依据作出判断，并记录基准日与依据，以便事后检验。")),
        ("chart", L("데이터", "Data", "数据"), "Data",
         L("공식 통계와 공개 자료를 원자료 기준으로 쌓아, 시계열로 봅니다.",
           "We accumulate official statistics and public sources at the primary-data level and read them as time series.",
           "以原始数据为基础积累官方统计与公开资料，并以时间序列来观察。")),
        ("compass", L("접근", "Access", "渠道"), "Access",
         L("중국 원문 자료와 현지 전문가 교류로 정책의 맥락을 읽습니다. 공개 자료와 적법한 조사 범위 안에서 일합니다.",
           "We read policy in context through Chinese-language sources and exchange with local experts — always within public sources and lawful research.",
           "通过中文原始资料和与当地专家的交流解读政策背景，始终在公开资料与合法调研的范围内开展工作。")),
    ]


def research_areas():
    return [
        ("macro", "chart", L("거시경제", "Macroeconomics", "宏观经济"),
         L("성장률, 물가, 사회융자총량, 통화·재정 정책의 흐름을 추적합니다.",
           "Growth, prices, total social financing, and the course of monetary and fiscal policy.",
           "跟踪经济增长、物价、社会融资规模以及货币与财政政策的走向。"),
         [L("성장률", "Growth", "增长"), L("물가", "Prices", "物价"), L("사회융자총량", "Total social financing", "社会融资规模"),
          L("통화·재정 정책", "Monetary & fiscal policy", "货币与财政政策")]),
        ("policy", "scale", L("정책·규제", "Policy & Regulation", "政策与监管"),
         L("중앙경제공작회의·양회 등 정책 문서의 문장 변화를 읽고, 규제 방향이 산업에 주는 영향을 분석합니다.",
           "We read the changing language of policy documents — the Central Economic Work Conference, the Two Sessions — and analyse what regulatory direction means for industry.",
           "解读中央经济工作会议、两会等政策文件的措辞变化，分析监管方向对产业的影响。"),
         [L("정책 문서", "Policy documents", "政策文件"), L("양회", "Two Sessions", "两会"),
          L("중앙경제공작회의", "Central Economic Work Conference", "中央经济工作会议"), L("수출통제", "Export controls", "出口管制")]),
        ("industry", "factory", L("산업·공급망", "Industry & Supply Chain", "产业与供应链"),
         L("신에너지, 반도체, 플랫폼, 부동산과 한중 교역, 핵심 소재, 수출통제를 다룹니다.",
           "New energy, semiconductors, platforms and property; Korea–China trade, critical materials and export controls.",
           "涵盖新能源、半导体、平台经济、房地产，以及韩中贸易、关键材料与出口管制。"),
         [L("신에너지", "New energy", "新能源"), L("반도체", "Semiconductors", "半导体"), L("플랫폼", "Platforms", "平台经济"),
          L("부동산", "Property", "房地产"), L("한중 교역", "Korea–China trade", "韩中贸易"), L("핵심 소재", "Critical materials", "关键材料")]),
    ]


def services():
    return [
        ("target", L("중국 노출 진단", "China exposure review", "涉华敞口诊断"),
         L("매출·조달·투자가 중국 변수에 얼마나 노출돼 있는지 점검하고, 진단 보고서로 정리합니다.",
           "How exposed revenue, sourcing and investment are to China factors, set out in a review report.",
           "梳理营收、采购与投资对中国因素的敞口，并形成诊断报告。")),
        ("users", L("경영진 자문 세션", "Executive advisory sessions", "管理层咨询会议"),
         L("경영진의 중국 판단을 결정 한 건 단위로 함께 검토합니다.",
           "Working through management's China call, one decision at a time.",
           "以单项决策为单位，与管理层共同研判对华判断。")),
        ("scale", L("정책·규제 영향 분석", "Policy & regulatory impact", "政策与监管影响分析"),
         L("중국의 정책·규제 변화가 사업에 주는 영향을 해석합니다.",
           "What changes in China's policy and regulation mean for the business.",
           "解读中国政策与监管变化对业务的影响。")),
        ("link", L("공급망 점검", "Supply-chain review", "供应链检视"),
         L("핵심 소재·부품의 조달 경로와 수출통제 변수를 살핍니다.",
           "Sourcing routes for key materials and parts, and export-control variables.",
           "审视关键材料与零部件的采购路径及出口管制变量。")),
        ("compass", L("시장 전략 검토", "Market strategy review", "市场战略评估"),
         L("중국 시장·산업의 흐름에 비춰 진출·철수를 포함한 사업 전략을 검토합니다.",
           "Testing business strategy, including entry and exit, against trends in China's markets and industries.",
           "结合中国市场与产业趋势，评估包括进入与退出在内的经营战略。")),
        ("layers", L("크로스보더 M&A 전략 자문", "Cross-border M&A strategy", "跨境并购战略咨询"),
         L("전략 자문 범위로 한정하며, 중개·주선은 하지 않습니다.",
           "Strategic advice only; we do not broker or arrange transactions.",
           "仅限战略咨询，不从事中介或撮合。")),
    ]


def scope_note():
    return L("세부 범위와 방식은 상담을 통해 정합니다. CSAI는 종목 추천·자산 운용·투자 중개를 하지 않습니다.",
             "Scope and format are agreed in consultation. CSAI does not recommend securities, manage assets or broker investments.",
             "具体范围与方式通过沟通确定。CSAI不提供个股推荐、资产管理或投资中介服务。")


def issue_card():
    toc = [
        ("OPINION", L("편집장 칼럼", "Editor's column", "主编专栏")),
        ("HOT ISSUE", L("이달의 핵심 이슈", "Issue of the month", "本月焦点")),
        ("MACRO", L("성장·물가·신용·정책", "Growth, prices, credit, policy", "增长·物价·信用·政策")),
        ("INDUSTRY", L("산업분석", "Industry analysis", "产业分析")),
        ("SUPPLY", L("공급망과 한국 수출", "Supply chains and Korean exports", "供应链与韩国出口")),
        ("Q&A", L("독자 질문에 답합니다", "Readers' questions answered", "读者问答")),
    ]
    rows = "".join(f"<li><span>{k}</span>{v}</li>" for k, v in toc)
    return f'''<div class="issue">
  <div class="issue-top"><b>{L("월간 「중국경제포커스」 최신호", "China Economy Focus — latest issue", "月刊《中国经济聚焦》最新一期")}</b><span>2026-11</span></div>
  <ol class="toc">{rows}</ol>
  <div class="row-btns">{btn(L("무료 구독하기", "Subscribe free", "免费订阅"), SUBSCRIBE, "navy", ext=True)}{btn(L("지난 호 보기", "Past issues", "往期回顾"), ARCHIVE, "ghost", ext=True)}</div>
  <p class="note">{L("발행: 거시경제연구소 · 본 자료는 정보 제공 목적이며 특정 종목·상품의 매수·매도 권유가 아닙니다.",
                    "Published by the Macroeconomic Institute (거시경제연구소). For information only; not a recommendation to buy or sell any security or product.",
                    "发行：宏观经济研究所。本资料仅供参考，不构成任何证券或产品的买卖建议。")}</p>
</div>'''


def signal_box():
    return f'''<div class="signal">
  <h3>{L("고유 지표 · 지방정부 부채 스트레스 지수", "Proprietary indicator · Local Government Debt Stress Index", "自有指标 · 地方政府债务压力指数")}</h3>
  <p>{L("성(省)별 신용스프레드·토지수입·그림자금융·차환 부담을 0~3점으로 평가해 매호 신호등으로 공개합니다.",
        "Each province is scored 0–3 on credit spreads, land revenue, shadow banking and refinancing burden, and shown as a traffic light in every issue.",
        "按省份对信用利差、土地收入、影子银行与再融资压力进行0–3分评估，每期以红绿灯形式公布。")}</p>
  <div class="sig-row">
    <span><i style="background:#B4483C"></i>{L("경고 · 2.2 이상", "Warning · 2.2 and above", "警告 · 2.2及以上")}</span>
    <span><i style="background:#D9A441"></i>{L("주의 · 1.6~2.2", "Caution · 1.6–2.2", "关注 · 1.6–2.2")}</span>
    <span><i style="background:#2E8B5E"></i>{L("안정 · 1.6 미만", "Stable · below 1.6", "稳定 · 低于1.6")}</span>
  </div>
</div>'''


def content_types(link=True):
    live1, live2 = L("발행 중", "Publishing", "发行中"), L("운영 중", "Live", "运营中")
    soon_t = L("준비 중", "Coming soon", "筹备中")
    data = [
        ("flash", "bolt", "Flash", L("정책·통계·산업 변화에 대한 짧은 시의성 분석", "Short, timely notes on policy, data and industry shifts", "针对政策、数据与产业变化的简短时评"), L("11월 중순호", "Mid-November issue", "11月中旬期"), True),
        ("monthly", "cal", L("월간 중국경제포커스", "Monthly", "月刊《中国经济聚焦》"), L("중국 거시·산업·공급망 월간 분석", "Monthly analysis of macro, industry and supply chains", "中国宏观、产业与供应链月度分析"), live1, True),
        ("deepdive", "layers", L("심층보고", "Deep Dive", "深度报告"), L("특정 산업·정책·공급망의 심층보고", "In-depth reports on one industry, policy or supply chain", "针对特定产业、政策或供应链的深度报告"), L("분기 발행", "Quarterly", "季度发行"), True),
        ("video", "play", L("영상", "Video", "视频"), L("유튜브·팟캐스트로 보는 해설", "Commentary on YouTube and podcast", "YouTube与播客解读"), live2, True),
    ]
    out = []
    for a, ic, t, d, tag, live in data:
        cls = "tag-live" if live else "tag-soon"
        out.append(f'<a class="type" href="{P("focus", a)}"><div class="type-h"><h3>{icon(ic, 20)}{t}</h3><span class="{cls}">{tag}</span></div><p>{d}</p></a>')
    return f'<div class="types">{"".join(out)}</div>'


def record_box(light=False):
    chips = [L("기준일", "As-of date", "基准日"), L("판단 내용", "Judgment", "判断内容"), L("근거", "Evidence", "依据"),
             L("무효화 조건", "Invalidation conditions", "失效条件"), L("후속 평가", "Follow-up review", "后续评估")]
    return f'''<div class="record{" light" if light else ""}">
  <h3>{L("판단 기록 · 공개 성적표", "Judgment record · public scorecard", "判断记录 · 公开成绩单")}</h3>
  <ol>{"".join(f"<li>{c}</li>" for c in chips)}</ol>
  <p>{L("판단을 내린 날짜와 근거, 틀렸다고 볼 조건을 함께 남기고 나중에 평가합니다.",
        "Each judgment is logged with its date, its evidence and the conditions that would prove it wrong, then reviewed later.",
        "每一次判断都记录日期、依据和失效条件，并在事后进行评估。")} {L("시나리오에는 확률을 함께 적을 예정입니다.", "Scenarios will carry probabilities.", "情景将附上概率。")}</p>
  <div class="rec-item">
    <p><b>{chips[0]}</b> {L("2026년 11월 15일", "15 November 2026", "2026年11月15日")}</p>
    <p><b>{chips[1]}</b> {L("11월 초 대중 수출 급증은 중국 내수 회복이 아니라 반도체 가격 효과가 이끈 것이다.", "The surge in Korea's exports to China in early November was driven by chip prices, not by a recovery in Chinese domestic demand.", "11月初韩国对华出口激增，是半导体价格效应带动的，而不是中国内需回暖。")}</p>
    <p><b>{chips[2]}</b> {L("11월 1~10일 반도체 수출 증가율(331.2%)이 대중 수출 증가율(148%)을 크게 웃돈다.", "In 1–10 November, chip export growth (331.2%) far exceeded growth in exports to China (148%).", "11月1至10日，半导体出口增速（331.2%）远高于对华出口增速（148%）。")}</p>
    <p><b>{chips[3]}</b> {L("12월 1일 월간 통계에서 반도체를 뺀 대중 수출이 반도체를 뺀 전체 수출보다 빠르게 늘면 이 판단을 거둔다.", "We withdraw this judgment if the monthly data on 1 December show exports to China excluding chips growing faster than total exports excluding chips.", "若12月1日的月度统计显示剔除半导体的对华出口增速快于剔除半导体的整体出口，则撤回这一判断。")}</p>
    <p><b>{chips[4]}</b> {L("2026년 12월 1일 통계 발표 뒤", "After the data release on 1 December 2026", "2026年12月1日统计发布之后")} · <a href="{P("focus", "flash-2026-11")}">{L("근거 글 보기", "Read the note", "查看依据")}</a></p>
  </div>
</div>'''


def media_cards():
    return f'''<div class="videos">
  <a class="vid" href="https://www.youtube.com/watch?v=V7p9mT0gU9w" target="_blank" rel="noopener"><div class="thumb"><img src="https://i.ytimg.com/vi/V7p9mT0gU9w/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"><b>안유화경제투자론</b><span class="len">YouTube</span></div><h3>{L("유튜브 채널", "YouTube channel", "YouTube 频道")}</h3><span>{L("중국·세계 경제와 투자 해설", "Commentary on China, the world economy and investing", "中国与世界经济及投资解读")}</span></a>
  <a class="vid" href="{PODCAST}" target="_blank" rel="noopener"><div class="thumb plain"><img src="{A("podcast.jpg")}" alt="{L("안유화의 경제투자론 팟캐스트 표지", "Podcast cover", "播客封面")}" loading="lazy"><b>안유화의 경제투자론 (안경투)</b><span class="len">Podcast</span></div><h3>{L("팟캐스트", "Podcast", "播客")}</h3><span>{L("팟빵에서 듣기", "Listen on Podbbang", "在 Podbbang 收听")}</span></a>
  <a class="vid" href="https://www.youtube.com/watch?v=rvKXDS1vyRA" target="_blank" rel="noopener"><div class="thumb"><img src="https://i.ytimg.com/vi/rvKXDS1vyRA/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"><b>안유화 쇼</b><span class="len">{L("연합인포맥스", "Yonhap Infomax", "韩联社 Infomax")}</span></div><h3>{L("경제 방송 진행", "Broadcast host", "财经节目主持")}</h3><span>{L("연합인포맥스 「안유화 쇼」", "“The An Yuhua Show”, Yonhap Infomax", "韩联社 Infomax《安玉花秀》")}</span></a>
</div>'''


def bio_paragraphs():
    return [
        L("안유화 교수는 중국 금융·자본시장을 연구하는 경제학자입니다. 중국 지린성 옌지에서 태어나 중국화공대학교에서 화학공정을 전공했고, 연변대학교에서 법학 석사, 고려대학교에서 경영학 박사 학위를 받았습니다. 연변대학교에서 10년간 학생을 가르쳤습니다.",
          "Professor An Yuhua is an economist specialising in Chinese finance and capital markets. Born in Yanji, Jilin Province, China, she studied chemical engineering as an undergraduate, earned a master's degree in law at Yanbian University and a Ph.D. in business administration at Korea University, and taught at Yanbian University for ten years.",
          "安玉花教授是研究中国金融与资本市场的经济学家。她出生于中国吉林省延吉市，本科主修化学工程，在延边大学获得法学硕士学位，在高丽大学获得管理学博士学位，并曾在延边大学任教十年。"),
        L("2008년부터 2015년까지 자본시장연구원 국제금융실에서 중국 담당 연구위원으로 일하며 「중국금융시장포커스」를 창간해 이끌었습니다. 이후 한국예탁결제원 객원연구원, 성균관대학교 중국대학원 금융학과 교수(2016~2023)를 지냈고, 외교부 정책자문위원과 국가지식재산위원회 전문위원으로 정책 자문을, 법무법인 율촌 중국팀 비상임고문으로 법률·투자 자문을 맡았습니다.",
          "From 2008 to 2015 she was the research fellow for China at the Korea Capital Market Institute (KCMI), where she founded and led the periodical “China Financial Market Focus”. She was later a visiting fellow at the Korea Securities Depository and a professor of finance at Sungkyunkwan University's Graduate School of China (2016–2023). She has advised on policy as a member of the Policy Advisory Committee of Korea's Ministry of Foreign Affairs and an expert member of the Presidential Council on Intellectual Property, and served as a non-standing advisor to the China team of the law firm Yulchon.",
          "2008年至2015年，她在韩国资本市场研究院（KCMI）国际金融室担任中国事务研究委员，创办并主持了《中国金融市场聚焦》。此后历任韩国预托结算院客座研究员、成均馆大学中国大学院金融系教授（2016–2023），并担任韩国外交部政策咨询委员、国家知识产权委员会专门委员，以及律村律师事务所中国组非常任顾问。"),
        L("현재 중국증권행정연구원 원장으로 한국 기업의 중국 투자 및 중국 기업의 한국과 미국투자 등 자문을 하고 있으며, 2024년부터 중국 하남성과학기술대학교 핀테크학과 석좌교수(学科带头人)로 재직 중입니다. 연세대학교 디지털금융·가상자산 최고위과정 교육원장(~2024)과 삼성글로벌경영포럼 자문위원(~2025)을 지냈습니다. 유튜브 「안유화경제투자론」과 연합인포맥스 「안유화 쇼」로 중국과 한국, 미국 및 세계 경제를 대중에게 알기 쉽게 설명하는 것으로 가장 큰 인기를 얻고 있습니다.",
          "She is now President of the China Securities Administration Institute (CSAI), advising Korean companies on investing in China and Chinese companies on investing in Korea and the United States, and since 2024 has also served as a chair professor (学科带头人) of fintech at a university of science and technology in Henan Province, China. She previously headed Yonsei University's executive programme in digital finance and virtual assets (to 2024) and advised the Samsung Global Management Forum (to 2025). She is best known for explaining the economies of China, Korea, the United States and the world in plain terms, through her YouTube channel and “The An Yuhua Show” on Yonhap Infomax.",
          "现任中国证券行政研究院（CSAI）院长，为韩国企业对华投资以及中国企业对韩国和美国的投资等提供咨询；自2024年起兼任中国河南省一所科技类大学金融科技学科带头人。曾任延世大学数字金融与虚拟资产高级课程教育院长（至2024年）、三星全球经营论坛咨询委员（至2025年）。她通过YouTube频道和韩联社 Infomax《安玉花秀》，以通俗易懂的方式向大众解读中国、韩国、美国及世界经济，并因此广受欢迎。"),
    ]


def timeline():
    rows = [
        (L("현재", "Present", "至今"), L("중국증권행정연구원 원장", "President, China Securities Administration Institute (CSAI)", "中国证券行政研究院（CSAI）院长")),
        (L("2024–현재", "2024–present", "2024–至今"), L("중국 하남성과학기술대학교 핀테크학과 석좌교수(学科带头人)", "Chair professor (学科带头人) of fintech, a university of science and technology in Henan, China", "中国河南省一所科技类大学金融科技学科带头人")),
        ("~2024.12", L("연세대 디지털금융·가상자산 최고위과정 교육원장", "Head, executive programme in digital finance & virtual assets, Yonsei University", "延世大学数字金融与虚拟资产高级课程教育院长")),
        ("~2025", L("삼성글로벌경영포럼 자문위원", "Advisor, Samsung Global Management Forum", "三星全球经营论坛咨询委员")),
        ("2026", L("월간 「중국경제포커스」 창간 · 편집장", "Founded the monthly China Economy Focus; editor-in-chief", "创办月刊《中国经济聚焦》并任主编")),
        ("2016–2023", L("성균관대학교 중국대학원 금융학과 교수", "Professor of finance, Graduate School of China, Sungkyunkwan University", "成均馆大学中国大学院金融系教授")),
        ("2016.01–2017.01", L("법무법인 율촌 중국팀 비상임고문", "Non-standing advisor, China team, Yulchon LLC", "律村律师事务所中国组非常任顾问")),
        ("2016–2020", L("국가지식재산위원회 전문위원", "Expert member, Presidential Council on Intellectual Property", "国家知识产权委员会专门委员")),
        ("2015–", L("외교부 정책자문위원 (경제·재외동포 분과)", "Policy Advisory Committee member, Ministry of Foreign Affairs", "韩国外交部政策咨询委员")),
        ("2015–2017", L("한국예탁결제원 객원연구원", "Visiting fellow, Korea Securities Depository", "韩国预托结算院客座研究员")),
        ("2008–2015", L("자본시장연구원 연구위원 · 「중국금융시장포커스」 책임편집", "Research fellow, Korea Capital Market Institute; editor of “China Financial Market Focus”", "韩国资本市场研究院研究委员 ·《中国金融市场聚焦》责任编辑")),
        ("2013", L("고려대학교 경영학 박사", "Ph.D. in business administration, Korea University", "高丽大学管理学博士")),
        ("1998–2001", L("연변대학교 경제학과 법학 석사", "Master of Laws, Department of Economics, Yanbian University", "延边大学经济系法学硕士")),
        ("1993–2003", L("연변대학교 교수", "Faculty, Yanbian University", "延边大学教师")),
        ("1989–1993", L("중국화공대학교 화학공정 공학사", "B.Eng. in chemical engineering", "化学工程工学学士")),
    ]
    return '<ol class="timeline">' + "".join(f"<li><time>{t}</time><b>{d}</b></li>" for t, d in rows) + "</ol>"


def channels():
    return (f'<div class="chan"><a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a>'
            f'<a href="{BLOG}" target="_blank" rel="noopener">{L("네이버 블로그", "Naver Blog", "Naver 博客")}</a>'
            f'<a href="{PODCAST}" target="_blank" rel="noopener">{L("팟캐스트", "Podcast", "播客")}</a>'
            f'<a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></div>')


def machine_svg():
    t = lambda *a: L(*a)
    return f'''<svg viewBox="0 0 560 360" role="img" aria-label="{t("중국 경제의 흐름: 정책, 금융, 지방재정, 산업·공급망, 가계·소비, 대외부문", "Flow of China's economy: policy, finance, local budgets, industry and supply chains, households, external sector", "中国经济的传导：政策、金融、地方财政、产业与供应链、居民与消费、对外部门")}">
  <defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#A9781F"/></marker></defs>
  <g fill="none" stroke="#A9781F" stroke-width="1.600" marker-end="url(#ar)"><path d="M200 62 L330 62"/><path d="M420 92 L420 150"/><path d="M380 196 L250 196"/><path d="M150 226 L150 272"/><path d="M240 302 L330 302"/></g>
  <path d="M100 272 C 40 220, 40 110, 92 90" fill="none" stroke="#63738E" stroke-width="1.200" stroke-dasharray="4 4" marker-end="url(#ar)"/>
  <g font-size="11" fill="#63738E">
    <text x="265" y="52" text-anchor="middle">{t("정책금리·대출 지도", "Rates · lending", "利率·信贷指导")}</text>
    <text x="430" y="126">{t("신용·채권", "Credit · bonds", "信用·债券")}</text>
    <text x="290" y="186" text-anchor="middle">{t("토지재정·LGFV", "Land finance", "土地财政")}</text>
    <text x="160" y="254">{t("투자·보조금", "Investment · subsidies", "投资·补贴")}</text>
    <text x="285" y="292" text-anchor="middle">{t("수출·위안화", "Exports · RMB", "出口·人民币")}</text>
    <text x="12" y="186" transform="rotate(-90 22 186)">{t("피드백", "Feedback", "反馈")}</text></g>
  <g>
    <rect x="60" y="32" width="140" height="60" rx="4" fill="#fff" stroke="#0B2452"/><text x="130" y="58" text-anchor="middle" font-size="15" font-weight="700" fill="#0E1E3C">{t("정책", "Policy", "政策")}</text><text x="130" y="78" text-anchor="middle" font-size="10.500" fill="#394966">{t("당중앙·국무원·발개위", "CPC · State Council · NDRC", "党中央·国务院·发改委")}</text>
    <rect x="340" y="32" width="170" height="60" rx="4" fill="#fff" stroke="#0B2452"/><text x="425" y="58" text-anchor="middle" font-size="15" font-weight="700" fill="#0E1E3C">{t("금융", "Finance", "金融")}</text><text x="425" y="78" text-anchor="middle" font-size="10.500" fill="#394966">{t("인민은행·국유은행·증권시장", "PBoC · state banks · securities", "人民银行·国有银行·证券市场")}</text>
    <rect x="340" y="160" width="170" height="60" rx="4" fill="#fff" stroke="#0B2452"/><text x="425" y="186" text-anchor="middle" font-size="15" font-weight="700" fill="#0E1E3C">{t("지방재정", "Local budgets", "地方财政")}</text><text x="425" y="206" text-anchor="middle" font-size="10.500" fill="#394966">{t("성·시 정부, 융자플랫폼", "Provinces, cities, LGFVs", "省市政府·融资平台")}</text>
    <rect x="60" y="166" width="180" height="60" rx="4" fill="#fff" stroke="#0B2452"/><text x="150" y="192" text-anchor="middle" font-size="15" font-weight="700" fill="#0E1E3C">{t("산업·공급망", "Industry", "产业·供应链")}</text><text x="150" y="212" text-anchor="middle" font-size="10.500" fill="#394966">{t("제조·신에너지·반도체", "Supply chains · new energy · chips", "制造·新能源·半导体")}</text>
    <rect x="60" y="276" width="180" height="56" rx="4" fill="#fff" stroke="#0B2452"/><text x="150" y="300" text-anchor="middle" font-size="15" font-weight="700" fill="#0E1E3C">{t("가계·소비", "Households", "居民·消费")}</text><text x="150" y="319" text-anchor="middle" font-size="10.500" fill="#394966">{t("고용·소득·부동산", "Jobs · income · property", "就业·收入·房地产")}</text>
    <rect x="340" y="276" width="170" height="56" rx="4" fill="#0B2452" stroke="#0B2452"/><text x="425" y="300" text-anchor="middle" font-size="15" font-weight="700" fill="#F6D896">{t("대외부문", "External sector", "对外部门")}</text><text x="425" y="319" text-anchor="middle" font-size="10.500" fill="#fff">{t("무역·자본흐름·위안화", "Trade · capital flows · RMB", "贸易·资本流动·人民币")}</text>
  </g></svg>'''


def articles():
    kc, kr, kp = L("칼럼", "Column", "专栏"), L("연구보고서", "Report", "研究报告"), L("정기간행물", "Periodical", "期刊")
    ko = "" if C.lang == "ko" else L("", " · in Korean", " · 韩文")
    naeil = L("내일신문 「금요진단」", "Naeil Shinmun, Friday column", "《明日新闻》周五专栏")
    rows = [
        ("col", L("연재 중", "Ongoing", "连载中"), NAEIL_SEARCH, "내일신문 「금요진단」", L("현재 연재하고 있는 칼럼입니다. 제목을 누르면 최근 글을 모아 볼 수 있습니다.", "The column currently running. The title opens a search of the latest pieces.", "目前正在连载的专栏，点击标题可查看最新文章。"), kc),
        ("col", "2024-09", "https://m.naeil.com/news/read/522358", "중국이 대만문제에 그토록 민감해하는 이유", naeil, kc),
        ("col", "2024-05", "https://m.naeil.com/news/read/511341", "미국이 금리를 내리지 않는 진짜 이유", naeil, kc),
        ("col", "2020-09", "https://www.ajunews.com/view/20200923095335019", "미·중 충돌 격화 속에 속도 내는 위안화 국제화", L("아주경제 「안유화 칼럼」", "Aju Business Daily", "亚洲经济"), kc),
        ("col", "2020-02", "https://www.ajunews.com/view/20200213143112344", "코로나19 확산 사태가 세계경제에 미치는 영향", L("아주경제 「안유화 칼럼」", "Aju Business Daily", "亚洲经济"), kc),
        ("col", "2019-12", "https://www.ajunews.com/view/20191210100650279", "中 인민은행이 금융안정보고서를 통해 시장에 경보를 울린 이유", L("아주경제 「안유화 칼럼」", "Aju Business Daily", "亚洲经济"), kc),
        ("col", "2016-04", "https://m.seoul.co.kr/news/2016/04/28/20160428030007", "중국 부채위기를 어떻게 봐야 하나", L("서울신문 「열린세상」", "Seoul Shinmun", "首尔新闻"), kc),
        ("rep", "2012-11", "https://www.kcmi.re.kr/report/report_view?report_no=259", "위안화의 역외 사용 확대와 한국의 대응", L("자본시장연구원 이슈&amp;정책 12-05", "Korea Capital Market Institute, Issue &amp; Policy 12-05", "韩国资本市场研究院 Issue &amp; Policy 12-05"), kr),
        ("rep", "2011-12", "https://www.kcmi.re.kr/report/report_view?report_no=248", "중국 주식시장 특성과 외국기업의 활용방안", L("자본시장연구원 연구보고서", "Korea Capital Market Institute research report", "韩国资本市场研究院研究报告"), kr),
        ("pub", "2008–2015", "https://www.kcmi.re.kr/publications/pub_end2_view?syear=2013&amp;zcd=002001006&amp;zno=860&amp;cno=2845", "중국금융시장포커스", L("자본시장연구원 정기간행물 · 창간 및 책임편집 · 예: 2013 여름호 「중국의 그림자금융에 따른 위기와 기회」", "Korea Capital Market Institute periodical · founder and editor · e.g. Summer 2013, on the risks and opportunities of China's shadow banking", "韩国资本市场研究院期刊 · 创办并任责任编辑 · 例：2013年夏季号《中国影子银行带来的危机与机遇》") + f' · <a href="https://www.kcmi.re.kr/community/search_basic?topkey=%EC%95%88%EC%9C%A0%ED%99%94" target="_blank" rel="noopener">{L("자본시장연구원에서 안유화 발간물 전체 보기", "All of An Yuhua's KCMI publications", "查看安玉花在该研究院的全部出版物")}</a>', kp),
    ]
    lis = []
    for t, d, u, title, src, kind in rows:
        reg(title, src, P("research", "reports"), kind)
        lis.append(f'<li data-t="{t}"><time>{d}</time><div><h3><a href="{u}" target="_blank" rel="noopener" lang="ko">{title}</a></h3><p>{src}{ko}</p></div><span class="kind">{kind}</span></li>')
    filt = (f'<div class="filters" role="group" aria-label="{L("유형", "Type", "类型")}">'
            f'<button type="button" aria-pressed="true" data-f="all">{L("전체", "All", "全部")}</button>'
            f'<button type="button" aria-pressed="false" data-f="col">{kc}</button><button type="button" aria-pressed="false" data-f="rep">{kr}</button>'
            f'<button type="button" aria-pressed="false" data-f="pub">{kp}</button></div>')
    return filt + f'<ul class="articles" id="articles">{"".join(lis)}</ul>'


def books_html():
    return f'''<div class="books">
  <div class="book"><a href="https://product.kyobobook.co.kr/detail/S000220567836" target="_blank" rel="noopener"><div class="cover c1"><img src="https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791124637166.jpg" alt="『부의 곡선』 표지" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()"><div><b>부의 곡선</b><em>인생의 손익분기점을 넘어야 돈이 나를 위해 일한다</em></div><small>안유화 지음</small></div></a><h3 lang="ko">부의 곡선</h3><span>{L("경이로움 · 2026 · 최신작", "Gyeongiroum · 2026 · latest", "Gyeongiroum 出版 · 2026 · 最新作品")}</span></div>
  <div class="book"><a href="https://product.kyobobook.co.kr/detail/S000202631370" target="_blank" rel="noopener"><div class="cover c3"><img src="https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9791192445403.jpg" alt="『더 플로』 표지" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()"><div><b>더 플로</b></div><small>안유화 지음</small></div></a><h3 lang="ko">더 플로</h3><span>{L("경이로움 · 2023 · 첫 단독 저서 · 베스트셀러", "Gyeongiroum · 2023 · first solo book · bestseller", "Gyeongiroum 出版 · 2023 · 首部个人专著 · 畅销书")}</span></div>
</div>'''


# ── 기존 홈페이지에서 옮겨 온 조각(원문 유지) ─────────────────────
def message():
    """원장의 대표 문구: 기존 홈페이지 표지 문안 그대로."""
    return {
        "eyebrow": L("경제학자 · 중국증권행정연구원 원장", "Economist · President, China Securities Administration Institute", "经济学家 · 中国证券行政研究院 院长"),
        "title": L("중국을 정확히 읽는 것이<br><em>세계 경제를 읽는 일</em>입니다.", "Reading China accurately<br>is <em>reading the world economy</em>.", "准确读懂中国，<br>就是<em>读懂世界经济</em>。"),
        "lede": L("중국 경제는 시장과 정책이 함께 움직이는 기계입니다. 그 작동 원리를 데이터와 원칙으로 풀어, 한국의 투자자·기업·정책 결정자가 더 나은 판단을 내리도록 돕습니다.",
                  "China's economy is a machine driven by markets and policy together. I explain how it works through data and principles, so investors, companies and policymakers can decide better.",
                  "中国经济是市场与政策共同驱动的机器。以数据和原则解读其运行机制，帮助投资者、企业与决策者做出更好的判断。"),
        "name": L("안유화 교수", "Prof. An Yuhua", "安玉花 教授"),
        "role": L("중국 경제·금융 전문가 · 경영학 박사", "China economy & finance · Ph.D. in Business", "中国经济与金融专家 · 管理学博士"),
        "cta1": L("원칙 읽기", "Read the principles", "阅读原则"),
        "cta2": L("중국경제포커스 구독", "Subscribe to China Focus", "订阅《中国经济聚焦》"),
    }


def socials():
    return (f'<div class="socials"><a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube · 안유화경제투자론</a>'
            f'<a href="{BLOG}" target="_blank" rel="noopener">{L("네이버 블로그", "Naver Blog", "Naver 博客")}</a>'
            f'<a href="{PODCAST}" target="_blank" rel="noopener">{L("팟캐스트 · 안경투", "Podcast", "播客")}</a>'
            f'<a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></div>')


def message_section(principles_href, focus_href, focus_ext=False, extra=""):
    m = message()
    return f'''<section class="sec dark" id="insight"><div class="wrap">
  <div class="insight">
    <figure class="portrait"><img src="{A("profile.jpg")}" alt="{L("안유화 교수 프로필 사진", "Portrait of Professor An Yuhua", "安玉花教授照片")}" width="720" height="900">
      <figcaption>{m["name"]}<span>{m["role"]}</span></figcaption></figure>
    <div>
      <div class="eyebrow">{L("연구소장's Insight", "Director's Insight", "所长观点")}</div>
      <p class="quote" style="margin-top:18px">{m["title"]}</p>
      <p class="say-lede">{m["lede"]}</p>
      <p class="cite">{m["name"]} · {m["eyebrow"]}</p>
      <div class="sec-foot">{btn(m["cta1"], principles_href)}{btn(m["cta2"], focus_href, "line", ext=focus_ext)}{extra}</div>
      {socials()}
    </div>
  </div>
</div></section>'''


def machine_lede():
    return L("정책 신호가 금융을 거쳐 지방정부와 산업으로 내려가고, 그 결과가 무역과 위안화를 통해 세계로 퍼집니다. 다섯 개의 톱니를 함께 봐야 중국이 보입니다.",
             "Policy signals travel through finance into local governments and industry, then out to the world through trade and the renminbi. Watch all five gears together.",
             "政策信号经由金融体系传导至地方政府与产业，再通过贸易和人民币影响世界。五个齿轮必须一起看。")


def machine_block():
    notes = [
        (L("정책이 먼저 움직입니다", "Policy moves first", "政策先行"), L("중국에서는 가격보다 정책 신호가 먼저 나옵니다. 중앙경제공작회의와 양회의 문장 하나가 1년의 신용 방향을 정합니다.", "In China the policy signal comes before the price. A single sentence from the Central Economic Work Conference or the Two Sessions sets the direction of credit for a year.", "在中国，政策信号先于价格出现。中央经济工作会议和两会的一句话，决定一年的信用方向。")),
        (L("돈은 은행과 지방정부를 거쳐 흐릅니다", "Money flows through banks and local governments", "资金经由银行与地方政府流动"), L("국유은행의 대출과 지방정부의 토지재정이 투자의 대부분을 만듭니다. 부채의 위치를 알면 위험의 위치가 보입니다.", "State-bank lending and local governments' land finance create most investment. Know where the debt sits and you see where the risk sits.", "国有银行贷款与地方政府的土地财政构成了大部分投资。知道债务在哪里，就能看到风险在哪里。")),
        (L("한국은 공급망으로 연결됩니다", "Korea is connected through supply chains", "韩国通过供应链相连"), L("중국의 산업정책 변화는 한국 수출 품목과 공급망에 곧바로 전달됩니다. 모든 분석은 '한국 시사점'으로 끝맺습니다.", "Shifts in China's industrial policy pass straight through to Korean export items and supply chains. Every analysis ends with “implications for Korea”.", "中国产业政策的变化会直接传导至韩国的出口品类与供应链。所有分析都以“对韩国的启示”收尾。")),
    ]
    strip = (f'<a class="video-strip" href="{YOUTUBE}" target="_blank" rel="noopener"><span class="play">{icon("play", 26)}</span>'
             f'<span><b>{L("30분 영상 강의: 중국 경제는 어떻게 작동하는가", "30-minute lecture: How China\'s economy works", "30分钟讲座：中国经济如何运行")}</b>'
             f'<small>{L("대표 강의 제작 예정 · 지금은 유튜브 「안유화경제투자론」에서 해설을 볼 수 있습니다", "Flagship lecture in production · watch commentary on YouTube now", "代表讲座制作中 · 现可在YouTube观看解读")}</small></span></a>')
    return (f'<div class="machine"><div class="diagram">{machine_svg()}</div><div class="flow-note">'
            + "".join(f"<div><h3>{h}</h3><p>{p}</p></div>" for h, p in notes) + f"</div></div>{strip}")


def pillars():
    data = [(L("거시", "Macro", "宏观"), L("성장률, 물가, 사회융자총량, 통화·재정 정책", "Growth, prices, total social financing, monetary and fiscal policy", "增长、物价、社会融资规模、货币与财政政策")),
            (L("산업분석", "Industry", "产业分析"), L("신에너지, 반도체, 플랫폼, 부동산", "New energy, semiconductors, platforms, property", "新能源、半导体、平台经济、房地产")),
            (L("공급망", "Supply chains", "供应链"), L("한중 교역, 핵심 소재, 수출통제", "Korea–China trade, critical materials, export controls", "韩中贸易、关键材料、出口管制"))]
    return '<div class="pillars">' + "".join(f"<div><b>{t}</b><span>{d}</span></div>" for t, d in data) + "</div>"


def principles_lede():
    return L("수십 년간 중국 시장을 관찰하며 정리한 판단의 기준입니다. 원칙은 결론이 아니라, 매번 같은 실수를 하지 않기 위한 체크리스트입니다.",
             "Rules of judgment distilled from decades of watching Chinese markets. A checklist to avoid repeating the same mistakes.",
             "多年观察中国市场所总结的判断标准，是避免重复同样错误的清单。")


def principles_grid():
    pr = "".join(f'<article class="pr"><span class="no">{n}</span><h3>{t}</h3><p>{d}</p></article>' for n, t, d in principles())
    for n, t, d in principles():
        reg(t, d, P("insight", "principles"), L("원칙", "Principle", "原则"))
    note = L("※ 위 원칙은 초안입니다. 교수님 감수 후 확정되며, 원칙마다 상세 해설 페이지로 확장합니다.", "※ Draft principles, pending the professor's review; each will be expanded into a detailed commentary page.", "※ 以上原则为草稿，待教授审定后确定，并将逐条扩展为详细解读页面。")
    return f'<div class="principles">{pr}</div><p class="note" style="margin-top:24px">{note}</p>'


def player():
    return (f'<div class="player"><a href="{YOUTUBE}/videos" target="_blank" rel="noopener">{L("안유화의 경제투자론 최신 영상", "Latest videos on YouTube", "YouTube 最新视频")}<span>YOUTUBE · {L("매주 화요일 업로드", "new every Tuesday", "每周二更新")}</span></a>'
            f'<iframe src="https://www.youtube-nocookie.com/embed/videoseries?list=UUThwDMeuhkjOONCAIUiu4xg" title="{L("안유화의 경제투자론 최신 영상", "Latest videos", "最新视频")}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>')


def videos_lede():
    return L("유튜브 채널 「안유화의 경제투자론」의 최신 영상을 바로 볼 수 있습니다. 매주 화요일 새 영상이 올라옵니다.", "Watch the latest from the YouTube channel right here. A new video goes up every Tuesday.", "可在此直接观看YouTube频道的最新视频，每周二更新。")


def books_lede():
    return L("돈과 부가 흐르는 원리를 개인의 언어로 풀어낸 책입니다. 표지를 누르면 교보문고 책 페이지로 이동합니다.", "Books that explain, in plain language, how money and wealth flow. Covers link to the Kyobo Book Centre pages (in Korean).", "以通俗的语言讲述金钱与财富流动原理的著作。点击封面可前往教保文库页面（韩文）。")


def columns_lede():
    return L("자본시장연구원 시절의 보고서부터 언론 기고까지, 중국 금융을 기록해 온 글을 모읍니다.", "From reports written at the Korea Capital Market Institute to newspaper columns: a record of writing on Chinese finance.", "从在韩国资本市场研究院时期的报告到媒体专栏，汇集记录中国金融的文字。")


def columns_note():
    return (f'<p class="note" style="margin-top:16px">{L("전체 칼럼 목록은", "The full list of columns is available via", "全部专栏可通过")} '
            f'<a href="https://search.naver.com/search.naver?where=news&amp;query=%EC%95%88%EC%9C%A0%ED%99%94+%EC%B9%BC%EB%9F%BC" target="_blank" rel="noopener">{L("언론 기고 검색", "a news search", "新闻搜索")}</a>'
            f'{L("에서 볼 수 있습니다. 연도별 아카이브로 정리해 갑니다.", ". A year-by-year archive is on the way.", "查看，并将按年份整理归档。")}</p>')


# ── 비전체계도 최종안(2026-11)에서 옮긴 내용. 표현이 다를 때는 홈페이지에 이미 쓴 표기를 따른다 ──
def core_values():
    return [
        ("compass", L("통찰", "Insight", "洞察"), "Insight",
         L("중국 1차 자료를 원문으로 읽고, 한국 기관의 언어로 씁니다.", "We read Chinese primary sources in the original and write in the language of Korean institutions.", "以原文阅读中国一手资料，用韩国机构的语言写作。"),
         L("양방향 전문성 · 「정책 언어 읽기」", "Two-way expertise · “Reading policy language”", "双向专业能力 ·“解读政策语言”")),
        ("shield", L("독립", "Independence", "独立"), "Independence",
         L("구독과 자문이 핵심 수입입니다. 후원·성과보수·매매 추천은 없습니다.", "Subscriptions and advisory are our core income. No sponsorship, no performance fees, no trading recommendations.", "订阅与咨询是核心收入。不接受赞助，不收取业绩报酬，不提供买卖建议。"),
         L("수입 구조 공개 · 이해상충 원칙", "Disclosed income structure · conflict-of-interest principles", "公开收入结构 · 利益冲突原则")),
        ("target", L("정확", "Accuracy", "准确"), "Accuracy",
         L("판단을 날짜와 함께 기록하고, 다음 호에 스스로 채점합니다.", "We record each judgment with its date and grade ourselves in the next issue.", "判断连同日期一并记录，并在下一期自行评分。"),
         L("판단 기록 · 공개 성적표", "Judgment record · public scorecard", "判断记录 · 公开成绩单")),
        ("bolt", L("실행", "Pragmatism", "务实"), "Pragmatism",
         L("모든 글은 한국 시사점으로 끝나고, 자문은 결정 한 건 단위로 합니다.", "Every piece ends with implications for Korea, and advisory is done one decision at a time.", "每篇文章都以对韩国的启示收尾，咨询以单项决策为单位进行。"),
         L("「한국 시사점」 상자 · 8주 유료 파일럿", "“Implications for Korea” box · eight-week paid pilot", "“对韩国的启示”专栏 · 8周付费试点")),
    ]


def core_values_cards(evidence=True):
    out = []
    for ic, t, en, d, ev in core_values():
        e_html = f'<div class="evi">{L("증거", "Evidence", "依据")} · {ev}</div>' if evidence else ""
        out.append(f'<div class="card"><div class="badge-ico">{icon(ic, 26)}</div><div class="num">{en.upper()}</div><h3>{t}</h3><p>{d}</p>{e_html}</div>')
        reg(t, d, P("about", "vision"), L("핵심가치", "Core values", "核心价值"))
    return f'<div class="g4">{"".join(out)}</div>'


def asset_lists():
    """판단·데이터·접근: 지금 하는 것 / 준비하는 것."""
    return [
        ([L("연구소장's Insight의 판단·한마디", "Judgments in Director's Insight", "“所长观点”中的判断与短评"),
          L("심층보고 No.1 (반도체·DRAM 공급망)", "Deep Dive No. 1 (semiconductor and DRAM supply chain)", "深度报告第1号（半导体与DRAM供应链）")],
         [L("공개 성적표 페이지", "Public scorecard page", "公开成绩单页面"), L("시나리오별 확률 표기", "Probabilities for each scenario", "各情景的概率标注")]),
        ([L("「연구실 데이터」 코너 — 예: 반도체 수입 증가의 88%는 가격 효과", "“Lab Data” column — e.g. 88% of the rise in semiconductor imports was a price effect", "“研究室数据”栏目——例：半导体进口增长的88%来自价格效应"),
          L("「한국 기업 중국 체감지수」 설문 시작", "Korea Corporate China Sentiment Index — survey under way", "“韩国企业对华景气指数”调查已启动")],
         [L("체감지수: 매월 · 5문항 · 업종별 · 결정 단위(가격·투자·고용)", "Sentiment index: monthly, five questions, by industry, at the level of decisions (pricing, investment, hiring)", "景气指数：每月、5个问题、分行业、以决策为单位（定价·投资·用工）"),
          L("지방정부 부채(LGFV) 성별 스트레스 지수", "Province-level local government debt (LGFV) stress index", "分省地方政府债务（融资平台）压力指数"),
          L("「한국 수출로 읽는 중국」 매월 1일 1쪽", "“Reading China through Korean exports”: one page on the 1st of each month", "“从韩国出口读中国”：每月1日一页")]),
        ([L("원장의 중국 학계·금융계 네트워크", "The President's network in Chinese academia and finance", "院长在中国学界与金融界的人脉"),
          L("연합인포맥스 「안유화 쇼」 · 유튜브 독자층", "“The An Yuhua Show” on Yonhap Infomax · YouTube audience", "韩联社 Infomax《安玉花秀》· YouTube 观众群")],
         [L("중국 학자 특별기고 분기 1편 (공개 분석만)", "One contribution a quarter from a Chinese scholar (public analysis only)", "每季度一篇中国学者特约文章（仅限公开分析）"),
          L("분기 경영진 브리핑(비공개) · 연례 중국 전망 포럼", "Quarterly closed-door executive briefing · annual China outlook forum", "季度管理层闭门简报 · 年度中国展望论坛")]),
    ]


def asset_cards(detail=False):
    out = []
    for (ic, t, en, d), (now, nxt) in zip(values(), asset_lists()):
        more_html = ""
        if detail:
            more_html = (f'<div class="mini"><h4>{L("지금 하는 것", "Now", "现有")}</h4><ul>{"".join(f"<li>{x}</li>" for x in now)}</ul>'
                         f'<h4>{L("준비하는 것", "In preparation", "筹备中")}</h4><ul>{"".join(f"<li>{x}</li>" for x in nxt)}</ul></div>')
        out.append(f'<div class="card"><div class="badge-ico">{icon(ic, 26)}</div><div class="num">{en.upper()}</div><h3>{t}</h3><p>{d}</p>{more_html}</div>')
    return f'<div class="g3">{"".join(out)}</div>'


def assets_lede():
    return L("정책 모니터링은 이제 AI가 대신합니다. 우리는 커버리지로 경쟁하지 않고, 판단·데이터·접근에서 복리로 쌓이는 자산을 만듭니다.",
             "Policy monitoring can now be done by AI. We do not compete on coverage; we build assets that compound in judgment, data and access.",
             "政策监测如今可由AI完成。我们不在覆盖面上竞争，而是在判断、数据与渠道上积累具有复利效应的资产。")


def boundary_title():
    return L("우리가 서는 자리: 중국과 한국 사이의 경계선", "Where we stand: the boundary between China and Korea", "我们的位置：中国与韩国之间的边界线")


def boundary_block(full=True):
    steps = [
        ("", L("중국의 정책", "China's policy", "中国的政策"), L("15차 5개년 계획 · 수출통제 · 보조금 · 규제 · 통화·재정", "15th Five-Year Plan · export controls · subsidies · regulation · monetary and fiscal policy", "“十五五”规划 · 出口管制 · 补贴 · 监管 · 货币与财政")),
        ("", L("한국 기업의 숫자", "Korean companies' numbers", "韩国企业的数字"), L("수출 · 조달 · 가격 · 투자 — 매월 1일, 가장 빠른 통계", "Exports · sourcing · prices · investment — the earliest statistics, on the 1st of each month", "出口 · 采购 · 价格 · 投资——每月1日，最快的统计")),
        (" end", L("한국의 결정", "Korean decisions", "韩国的决策"), L("조달 · 투자 · 가격 · 인력 — 경영진의 중국 판단", "Sourcing · investment · pricing · people — management's China call", "采购 · 投资 · 定价 · 人力——管理层的对华判断")),
    ]
    arrows = [L("경계선<br>1~2분기 먼저", "The boundary<br>1–2 quarters earlier", "边界线<br>提前1–2个季度"), L("번역", "Translation", "翻译")]
    parts = []
    for i, (cls, t, d) in enumerate(steps):
        parts.append(f'<div class="flow-step{cls}"><b>{t}</b><span>{d}</span></div>')
        if i < 2:
            parts.append(f'<div class="flow-arrow"><span>{arrows[i]}</span>{icon("arrow", 22)}</div>')
    ex = [L("수출통제 → 반도체", "Export controls → semiconductors", "出口管制 → 半导体"), L("배터리 보조금 → 배터리", "Battery subsidies → batteries", "电池补贴 → 电池"), L("해운 규제 → 해운", "Shipping regulation → shipping", "航运监管 → 航运")]
    hypo = L("<b>검증할 가설</b> — 중국 정책은 중국 통계보다 1~2분기 먼저 한국 숫자에 나타난다. 이 가설을 매호 검증합니다.",
             "<b>The hypothesis we test</b> — China's policy shows up in Korean numbers one to two quarters before it shows up in Chinese statistics. We test it in every issue.",
             "<b>待检验的假设</b>——中国的政策会比中国的统计数据提前一到两个季度体现在韩国的数字上。我们每期都对此进行检验。")
    pos = ""
    if full:
        pos = "<p class=\"sub-p\" style=\"margin:18px 0 0\">" + L("CSAI는 중국 정책이 한국 기업의 손익이 되는 경계선에 섭니다. 한국어로, 기업의 의사결정을 위해, 판단을 공개 채점하고, 중국 학자의 기고가 실리는 중립 플랫폼을 지향합니다.",
            "CSAI stands on the boundary where China's policy turns into Korean companies' profit and loss: a neutral platform, in Korean, built for corporate decisions, that grades its own judgments in public and carries contributions from Chinese scholars.",
            "CSAI站在中国政策转化为韩国企业损益的边界线上：以韩语、为企业决策服务、公开为自己的判断评分，并刊载中国学者文章的中立平台。") + "</p>"
    reg(boundary_title(), hypo, P("about", "position"), "About CSAI")
    return (f'<div class="flow">{"".join(parts)}</div><div class="chips">{"".join(f"<span>{x}</span>" for x in ex)}</div>'
            f'<p class="hypo">{hypo}</p>{pos}')


def strategy_cards():
    data = [
        ("chart", L("중국 거시·정책 리서치", "China macro and policy research", "中国宏观与政策研究"),
         L("월간 「중국경제포커스」(거시·산업·공급망), Flash, 분기 심층보고와 자체 데이터", "The monthly China Economy Focus (macro, industry, supply chains), Flash notes, quarterly deep dives and our own data", "月刊《中国经济聚焦》（宏观·产业·供应链）、快讯、季度深度报告与自有数据"), P("focus")),
        ("users", L("기업 자문 · 크로스보더 전략", "Business advisory and cross-border strategy", "企业咨询与跨境战略"),
         L("중국 노출 진단, 경영진 자문 세션, 공급망·진출·철수 전략", "China exposure review, executive sessions, supply-chain, entry and exit strategy", "涉华敞口诊断、管理层咨询会议、供应链及进入与退出战略"), P("advisory")),
        ("cap", L("교육 · 리더십과 인재 육성", "Education: leadership and talent", "教育：领导力与人才培养"),
         L("기업 임원 중국 과정, 금융기관 중국 리스크 과정, AI·디지털 금융 교육", "China programme for executives, China-risk programme for financial institutions, AI and digital-finance training", "企业高管中国课程、金融机构中国风险课程、AI与数字金融培训"), P("academy")),
        ("layers", L("미래 금융 연구 · 디지털과 기후", "Future-finance research: digital and climate", "未来金融研究：数字与气候"),
         L("디지털 위안화·스테이블코인·토큰증권(STO), 탄소배출권·녹색금융 — 분석·보고서로만", "Digital yuan, stablecoins, security tokens (STO), carbon markets and green finance — analysis and reports only", "数字人民币、稳定币、证券型代币（STO）、碳排放权与绿色金融——仅以分析与报告形式"), P("research", "future")),
    ]
    out = []
    for i, (ic, t, d, h) in enumerate(data):
        out.append(f'<a class="card" href="{h}"><div class="num">0{i + 1}</div><h3>{t}</h3><p>{d}</p></a>')
        reg(t, d, h, L("전략 방향", "Strategy", "战略方向"))
    return f'<div class="g4">{"".join(out)}</div>'


def strategy_lede():
    return L("네 방향을 동시에가 아니라 단계로 갑니다: 리서치 → 자문 → 교육 → 미래 금융 연구.", "Four directions, taken in stages rather than all at once: research → advisory → education → future-finance research.", "四个方向不是同时推进，而是分阶段：研究 → 咨询 → 教育 → 未来金融研究。")


def future_finance(compact=False):
    items = [L("디지털 위안화 · 스테이블코인 · 토큰증권(STO) 제도 분석", "Institutional analysis of the digital yuan, stablecoins and security tokens (STO)", "数字人民币、稳定币与证券型代币（STO）制度分析"),
             L("중국 탄소배출권 시장 · 녹색금융 분석", "China's carbon-emissions market and green finance", "中国碳排放权市场与绿色金融分析")]
    note = L("분석·보고서로만 다루며, 운용이나 알고리즘 제공은 하지 않습니다.", "Covered through analysis and reports only; we do not manage assets or provide algorithms.", "仅以分析与报告形式呈现，不从事资产管理或算法提供。")
    title = L("미래 금융 연구", "Future-finance research", "未来金融研究")
    tag = L("상시 연구 주제", "Standing research theme", "常设研究主题")
    reg(title, " · ".join(items), P("research", "future"), "Research")
    anchor = "" if compact else ' id="future"'
    return (f'<div class="card"{anchor} style="margin-top:24px"><div class="type-h"><h3>{title}</h3><span class="tag-live">{tag}</span></div>'
            f'<ul class="ticks">{"".join(f"<li>{x}</li>" for x in items)}</ul><p class="note">{note}</p></div>')


def data_items():
    data = [
        (L("한국 기업 중국 체감지수", "Korea Corporate China Sentiment Index", "韩国企业对华景气指数"),
         L("매월 · 5문항 · 업종별로, 가격·투자·고용 결정 단위로 묻습니다.", "Monthly, five questions, by industry, asked at the level of pricing, investment and hiring decisions.", "每月、5个问题、分行业，以定价、投资与用工决策为单位进行调查。"),
         L("설문 시작", "Survey under way", "调查已启动"), True),
        (L("한국 수출로 읽는 중국", "Reading China through Korean exports", "从韩国出口读中国"),
         L("관세청·산업부 통계로 매월 1일에 내는 1쪽 Flash", "A one-page Flash on the 1st of each month, from Korea Customs Service and trade-ministry statistics", "基于韩国关税厅与产业部统计、每月1日发布的一页快讯"),
         L("11월 중순호 발행", "Mid-November issue out", "11月中旬期已发布"), True),
        (L("「연구실 데이터」 코너", "“Lab Data” column", "“研究室数据”栏目"),
         L("월간지에 싣는 자체 분석. 예: 반도체 수입 증가의 88%는 가격 효과", "Our own analysis in the monthly. Example: 88% of the rise in semiconductor imports was a price effect.", "月刊中的自主分析。例：半导体进口增长的88%来自价格效应。"),
         L("발행 중", "Publishing", "发行中"), True),
    ]
    out = []
    for t, d, tag, live in data:
        reg(t, d, P("research", "data"), "Research Data")
        out.append(f'<div class="type"><div class="type-h"><h3>{t}</h3><span class="{"tag-live" if live else "tag-soon"}">{tag}</span></div><p>{d}</p></div>')
    return f'<div class="types" style="margin-top:14px">{"".join(out)}</div>'


def process_steps():
    steps = [(L("중국 노출 진단", "China exposure review", "涉华敞口诊断"), L("진단 보고서", "Review report", "诊断报告")),
             (L("경영진 자문 세션", "Executive advisory session", "管理层咨询会议"), L("결정 한 건 단위", "One decision at a time", "以单项决策为单位")),
             (L("8주 유료 파일럿", "Eight-week paid pilot", "8周付费试点"), L("범위와 방식을 맞춰 보는 기간", "A period to fit scope and format", "磨合范围与方式的阶段")),
             (L("연간 자문 계약", "Annual advisory contract", "年度咨询合同"), L("파일럿 뒤 이어 가는 연간 자문", "Advisory continued on an annual basis", "试点之后延续的年度咨询"))]
    return '<ol class="steps">' + "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in steps) + "</ol>"


def process_lede():
    return L("자문은 결정 한 건 단위로 합니다. 진단에서 시작해 8주 유료 파일럿을 거쳐 연간 계약으로 이어집니다.", "Advisory is done one decision at a time. It starts with a review, moves through an eight-week paid pilot, and continues as an annual contract.", "咨询以单项决策为单位进行：从诊断开始，经过8周付费试点，再延续为年度合同。")


def events_list(full=True):
    """확정된 일정 목록. full=False 이면 포럼·브리핑만."""
    rows = [("2026.12.15", L("영문 분기 노트 「Korea Sensor」 첫 호", "First issue of the English quarterly note Korea Sensor", "英文季度简报 Korea Sensor 首期")),
            ("2026.12.24", L("연례 중국 전망 포럼", "Annual China outlook forum", "年度中国展望论坛")),
            ("2027.01.15", L("분기 경영진 브리핑", "Quarterly executive briefing", "季度管理层简报")),
            ("2027 1Q", L("중국 학자 특별기고 첫 편", "First special contribution from a Chinese scholar", "中国学者特约稿首篇"))]
    if not full:
        rows = rows[1:3]
    return '<ul class="hist wide">' + "".join("<li><b>" + d + "</b><span>" + x + "</span></li>" for d, x in rows) + "</ul>"


def tag_date(ko, en, zh):
    return '<span class="tag-date">' + L(ko, en, zh) + "</span>"


def notices():
    """기관 소식: 날짜가 늦은 것부터."""
    rows = [("2026.12.24", L("연례 중국 전망 포럼 개최 예정", "Annual China outlook forum to be held", "年度中国展望论坛即将举行"), P("global", "events")),
            ("2026.11.15", L("홈페이지 개편, 원장 인사말과 조직도 공개", "Website relaunched; President's greeting and organisation chart published", "网站改版，发布院长致辞与组织架构图"), P("about", "greeting")),
            ("2026.11.15", L("Flash 「한국 수출로 읽는 중국」 첫 호 발행", "First Flash note published: China through Korean Exports", "Flash《从韩国出口看中国》首期发布"), P("focus", "flash-2026-11")),
            ("2026.11", L("연구보고서 「반도체 공급망 대전환 2026」 발간", "Research report published: The Great Semiconductor Supply-chain Shift 2026", "研究报告《半导体供应链大转变 2026》发布"), P("research", "report-supply-chain-01"))]
    return '<ul class="hist wide">' + "".join("<li><b>" + d + '</b><span><a href="' + u + '">' + x + "</a></span></li>" for d, x, u in rows) + "</ul>"
