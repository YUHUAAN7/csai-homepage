# -*- coding: utf-8 -*-
"""메뉴별 누적 자료(아카이브). 새 항목은 목록에 **추가만** 하고, 지난 항목은 지우거나 덮어쓰지 않는다.

- 목록 안의 순서는 상관없다. 빌드할 때 날짜(date)가 늦은 것부터 자동으로 정렬된다.
- 날짜는 "2026-11-15"(일까지) 또는 "2026-11"(월까지)로 적는다. 화면에는 2026.11.15 / 2026.11 로 나온다.
  기간처럼 날짜로 적기 어려우면 date 에 정렬용 날짜를 넣고 label 에 보일 글자를 넣는다.
- 글은 {"ko": …, "en": …, "zh": …} 로 적는다. en·zh 를 비우면 한국어가 그대로 나온다.
- 글자는 그대로 적는다(HTML 태그를 쓰지 않는다). 빌드할 때 자동으로 안전하게 바뀐다.
- 링크 "link" 는 사이트 안이면 ["페이지", "앵커"] (예: ["focus", "flash-2026-11"]), 밖이면 "https://…".
- 모든 항목은 각 메뉴 화면과 뉴스·자료 > 전체 아카이브(archive.html)에 함께 쌓인다.
- 열흘 노트는 src/tenday.py, 영상 해설은 src/episodes.py 에 따로 있고, 아카이브에도 자동으로 들어간다.

    python3 src/build.py
"""

# ── 월간 「중국경제포커스」 (거시경제연구소) ─────────────────────────
# 매월 발행 후 한 항목 추가. pdf 를 비우면 고정 규칙 https://chinamacro.kr/issues/YYYY-MM.pdf 를 쓴다.
#   {"id": "2026-12", "no": 3, "date": "2026-12-08", "title": {…}, "points": {"ko": [..]}, "pdf": "", "web": ""}
#   title·points 는 없으면 생략(제목 대신 '2026년 12월호'로 나온다). 가장 최근 호가 '최신호' 카드에 나온다.
MONTHLY = [
    {"id": "2026-11", "no": 2, "date": "2026-11"},
    {"id": "2026-10", "no": 1, "date": "2026-10", "label_note": {"ko": "창간호", "en": "First issue", "zh": "创刊号"}},
]

# ── 심층보고 (거시경제연구소, 분기) ──────────────────────────────────
DEEPDIVE = [
    {
        "id": "deepdive-01", "no": 1, "date": "2026-11",
        "title": {"ko": "반도체·DRAM 공급망", "en": "Semiconductor and DRAM supply chain", "zh": "半导体与DRAM供应链"},
        "note": {"ko": "전문은 문의로 제공합니다.", "en": "Full report available on inquiry.", "zh": "全文可通过咨询获取。"},
        "inquiry": True,
    },
]

# 다음 심층보고 안내(발행되면 DEEPDIVE 에 항목을 추가하고 이 문구를 다음 호로 바꾼다. 비우면 안내 상자를 숨긴다)
DEEPDIVE_NEXT = {
    "ko": "다음 심층보고는 2026년 12월 첫 주에 발행합니다. 주제는 ‘반도체 호황을 걷어낸 한국 수출의 진짜 모습’입니다. 미래 금융(디지털 위안화·토큰증권·탄소시장)도 심층보고 주제로 다룹니다.",
    "en": "The next in-depth report will be published in the first week of December 2026, on what Korea's exports look like once the chip boom is stripped out. Future finance (the digital yuan, tokenised securities and carbon markets) is also among our in-depth topics.",
    "zh": "下一期深度报告将于2026年12月第一周发布，主题是“剔除半导体热潮后韩国出口的真实面貌”。未来金融（数字人民币、代币化证券、碳市场）也是深度报告的主题。",
}

# ── CSAI 연구보고서 (연구·분석 > 연구보고서) ─────────────────────────
REPORTS = [
    {
        "id": "report-supply-chain-01", "date": "2026-11-03",
        "series": "CSAI GLOBAL SUPPLY CHAIN FOCUS · No. 01",
        "title": {"ko": "반도체 공급망 대전환 2026", "en": "The Great Semiconductor Supply-chain Shift 2026", "zh": "半导体供应链大转变 2026"},
        "subtitle": {"ko": "미중 갈등이 다시 그리는 반도체 지도와 한국의 선택", "en": "The chip map redrawn by US–China rivalry, and Korea's choices", "zh": "美中博弈重绘的半导体版图与韩国的选择"},
        "summary": {
            "ko": "반도체 공급망은 하나의 세계 사슬에서 관리된 두 개의 사슬로 갈라지고 있습니다. 한국은 가장 대체하기 어려운 메모리를 쥐고 있지만 설계 소프트웨어, 장비, 소재는 남에게 기대고 있습니다. 누가 병목을 쥐고 누가 밀려나는지, 한국은 무엇을 해야 하는지를 공개 자료 16건으로 정리했습니다.",
            "en": "The semiconductor supply chain is splitting from one global chain into two managed chains. Korea holds memory, the hardest link to replace, but relies on others for design software, equipment and materials. Drawing on 16 public sources, the report sets out who holds the chokepoints, who is pushed aside, and what Korea should do.",
            "zh": "半导体供应链正从一条全球链条分裂为两条受管理的链条。韩国握有最难替代的存储芯片，但在设计软件、设备和材料上依赖他人。报告依据16份公开资料，梳理谁掌握瓶颈、谁被挤出，以及韩国该怎么做。",
        },
        "toc": {
            "ko": "차례: 공급망 지도 · 병목과 집중도 · 단계별 경쟁력 · 미중 갈등이 바꾸는 사슬 · 승자와 패자 · 2027~2030 시나리오 · 한국의 위기와 기회 · 지켜볼 신호",
            "en": "Contents: supply-chain map · chokepoints and concentration · competitiveness by stage · how US–China rivalry changes the chain · winners and losers · 2027–2030 scenarios · risks and opportunities for Korea · signals to watch",
            "zh": "目录：供应链地图 · 瓶颈与集中度 · 各环节竞争力 · 美中博弈如何改变链条 · 赢家与输家 · 2027~2030情景 · 韩国的危机与机遇 · 值得关注的信号",
        },
        "meta": {"ko": "작성 기준일 2026년 11월 3일 · 15쪽", "en": "As of 3 November 2026 · 15 pages", "zh": "编写基准日：2026年11月3日 · 15页"},
        "inquiry": True,
    },
]

# ── 칼럼·기고·외부 보고서 (연구·분석 > 연구보고서·기고) ───────────────
# kind: "col"(칼럼) · "rep"(연구보고서) · "pub"(정기간행물). title 은 원문(한국어) 그대로.
WRITINGS_ONGOING = {  # 맨 위에 고정되는 '연재 중' 줄
    "kind": "col", "link": "NAEIL_SEARCH", "title": "내일신문 「금요진단」",
    "source": {"ko": "현재 연재하고 있는 칼럼입니다. 제목을 누르면 최근 글을 모아 볼 수 있습니다.", "en": "The column currently running. The title opens a search of the latest pieces.", "zh": "目前正在连载的专栏，点击标题可查看最新文章。"},
}
_NAEIL = {"ko": "내일신문 「금요진단」", "en": "Naeil Shinmun, Friday column", "zh": "《明日新闻》周五专栏"}
_AJU = {"ko": "아주경제 「안유화 칼럼」", "en": "Aju Business Daily", "zh": "亚洲经济"}
WRITINGS = [
    {"kind": "col", "date": "2024-09", "link": "https://m.naeil.com/news/read/522358", "title": "중국이 대만문제에 그토록 민감해하는 이유", "source": _NAEIL},
    {"kind": "col", "date": "2024-05", "link": "https://m.naeil.com/news/read/511341", "title": "미국이 금리를 내리지 않는 진짜 이유", "source": _NAEIL},
    {"kind": "col", "date": "2020-09", "link": "https://www.ajunews.com/view/20200923095335019", "title": "미·중 충돌 격화 속에 속도 내는 위안화 국제화", "source": _AJU},
    {"kind": "col", "date": "2020-02", "link": "https://www.ajunews.com/view/20200213143112344", "title": "코로나19 확산 사태가 세계경제에 미치는 영향", "source": _AJU},
    {"kind": "col", "date": "2019-12", "link": "https://www.ajunews.com/view/20191210100650279", "title": "中 인민은행이 금융안정보고서를 통해 시장에 경보를 울린 이유", "source": _AJU},
    {"kind": "col", "date": "2016-04", "link": "https://m.seoul.co.kr/news/2016/04/28/20160428030007", "title": "중국 부채위기를 어떻게 봐야 하나", "source": {"ko": "서울신문 「열린세상」", "en": "Seoul Shinmun", "zh": "首尔新闻"}},
    {"kind": "rep", "date": "2012-11", "link": "https://www.kcmi.re.kr/report/report_view?report_no=259", "title": "위안화의 역외 사용 확대와 한국의 대응",
     "source": {"ko": "자본시장연구원 이슈&정책 12-05", "en": "Korea Capital Market Institute, Issue & Policy 12-05", "zh": "韩国资本市场研究院 Issue & Policy 12-05"}},
    {"kind": "rep", "date": "2011-12", "link": "https://www.kcmi.re.kr/report/report_view?report_no=248", "title": "중국 주식시장 특성과 외국기업의 활용방안",
     "source": {"ko": "자본시장연구원 연구보고서", "en": "Korea Capital Market Institute research report", "zh": "韩国资本市场研究院研究报告"}},
    {"kind": "pub", "date": "2015-12", "label": "2008–2015", "link": "https://www.kcmi.re.kr/publications/pub_end2_view?syear=2013&zcd=002001006&zno=860&cno=2845", "title": "중국금융시장포커스",
     "source": {"ko": "자본시장연구원 정기간행물 · 창간 및 책임편집 · 예: 2013 여름호 「중국의 그림자금융에 따른 위기와 기회」",
                "en": "Korea Capital Market Institute periodical · founder and editor · e.g. Summer 2013, on the risks and opportunities of China's shadow banking",
                "zh": "韩国资本市场研究院期刊 · 创办并任责任编辑 · 例：2013年夏季号《中国影子银行带来的危机与机遇》"},
     "more": ["https://www.kcmi.re.kr/community/search_basic?topkey=%EC%95%88%EC%9C%A0%ED%99%94",
              {"ko": "자본시장연구원에서 안유화 발간물 전체 보기", "en": "All of An Yuhua's KCMI publications", "zh": "查看安玉花在该研究院的全部出版物"}]},
]

# ── 판단 기록 · 공개 성적표 (연구소장's Insight) ──────────────────────
# 판단을 낸 날 한 항목 추가. 점검일이 지나 결과가 나오면 그 항목의 status 와 result 만 채운다(판단 문장은 고치지 않는다).
# status: "open"(점검 대기) · "hit"(맞음) · "miss"(빗나감) · "withdrawn"(거둠) · "partial"(일부 맞음)
JUDGMENTS = [
    {
        "id": "j-2026-11-15", "date": "2026-11-15",
        "text": {"ko": "11월 초 대중 수출 급증은 중국 내수 회복이 아니라 반도체 가격 효과가 이끈 것이다.", "en": "The surge in Korea's exports to China in early November was driven by chip prices, not by a recovery in Chinese domestic demand.", "zh": "11月初韩国对华出口激增，是半导体价格效应带动的，而不是中国内需回暖。"},
        "evidence": {"ko": "11월 1~10일 반도체 수출 증가율(331.2%)이 대중 수출 증가율(148%)을 크게 웃돈다.", "en": "In 1–10 November, chip export growth (331.2%) far exceeded growth in exports to China (148%).", "zh": "11月1至10日，半导体出口增速（331.2%）远高于对华出口增速（148%）。"},
        "invalid": {"ko": "12월 1일 월간 통계에서 반도체를 뺀 대중 수출이 반도체를 뺀 전체 수출보다 빠르게 늘면 이 판단을 거둔다.", "en": "We withdraw this judgment if the monthly data on 1 December show exports to China excluding chips growing faster than total exports excluding chips.", "zh": "若12月1日的月度统计显示剔除半导体的对华出口增速快于剔除半导体的整体出口，则撤回这一判断。"},
        "review": {"ko": "2026년 12월 1일 통계 발표 뒤", "en": "After the data release on 1 December 2026", "zh": "2026年12月1日统计发布之后"},
        "link": ["focus", "flash-2026-11"],
        "status": "open",
        # "result": {"ko": "점검 결과 한두 문장", …}, "reviewed": "2026-12-02",
    },
]

# ── 기관 소식 (뉴스·자료) ───────────────────────────────────────────
NOTICES = [
    {"date": "2026-12-24", "title": {"ko": "연례 중국 전망 포럼 개최 예정", "en": "Annual China outlook forum to be held", "zh": "年度中国展望论坛即将举行"}, "link": ["global", "events"]},
    {"date": "2026-11-15", "title": {"ko": "홈페이지 개편, 원장 인사말과 조직도 공개", "en": "Website relaunched; President's greeting and organisation chart published", "zh": "网站改版，发布院长致辞与组织架构图"}, "link": ["about", "greeting"]},
    {"date": "2026-11-15", "title": {"ko": "「열흘 노트」 첫 호 발행 (한국 수출로 읽는 중국)", "en": "First Ten-Day Note published: China through Korean Exports", "zh": "《旬报》首期发布（从韩国出口看中国）"}, "link": ["focus", "flash-2026-11"]},
    {"date": "2026-11", "title": {"ko": "연구보고서 「반도체 공급망 대전환 2026」 발간", "en": "Research report published: The Great Semiconductor Supply-chain Shift 2026", "zh": "研究报告《半导体供应链大转变 2026》发布"}, "link": ["research", "report-supply-chain-01"]},
]

# ── 행사 일정 (글로벌 협력 > 포럼·행사) ─────────────────────────────
# 날짜가 지난 행사는 지우지 않아도 빌드할 때 자동으로 '지난 행사'로 옮겨진다.
# 끝난 뒤 후기·자료가 있으면 "result": {…}, "link": … 를 채운다. home=True 는 첫 화면에도 보일 행사.
EVENTS = [
    {"date": "2026-12-15", "title": {"ko": "영문 분기 노트 「Korea Sensor」 첫 호", "en": "First issue of the English quarterly note Korea Sensor", "zh": "英文季度简报 Korea Sensor 首期"}},
    {"date": "2026-12-24", "home": True, "title": {"ko": "연례 중국 전망 포럼: 2027년 중국 경제 전망, 정책 문장으로 읽는 방향", "en": "Annual China outlook forum: the 2027 outlook for China's economy, read through policy language", "zh": "年度中国展望论坛：2027年中国经济展望——从政策措辞读方向"}},
    {"date": "2027-01-15", "home": True, "title": {"ko": "CEO China Roundtable 첫 회 (분기 1회, 초청형)", "en": "CEO China Roundtable: first session (quarterly, by invitation)", "zh": "CEO China Roundtable 首期（每季度一次，邀请制）"}},
    {"date": "2027-03-31", "label": "2027 1Q", "title": {"ko": "중국 학자 특별기고 첫 편", "en": "First special contribution from a Chinese scholar", "zh": "中国学者特约稿首篇"}},
]
