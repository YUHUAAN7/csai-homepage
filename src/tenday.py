# -*- coding: utf-8 -*-
"""「열흘 노트」 목록. 한국 무역 통계가 나오는 날(매월 1일·11일·21일 무렵)마다 한 편.

- 새 호를 TENDAY 맨 위에 추가하고, NEXT_ISSUE(안내 상자의 '다음 호' 문구)를 고친 뒤
  `python3 src/build.py` 를 실행한다. 최신 호는 펼쳐서, 지난 호는 접어서 보인다.
- 열흘 노트는 무료 공개물이라 전문을 넣는다. 원장이 "올려 주세요"라고 승인한 원고만 넣는다.
- 글은 한국어(ko)·영어(en)·중국어(zh) 세 가지를 함께 넣는다. en·zh 를 비우면 그 언어 화면에 한국어가 나온다.
- 글자는 그대로 적는다(HTML 태그를 쓰지 않는다). 빌드할 때 자동으로 안전하게 바뀐다.
- 투자 권유로 읽힐 표현(종목·코인 매수·매도, 목표가)은 쓰지 않는다.

항목 형식 (ko/en/zh 가 있는 칸은 {"ko": …, "en": …, "zh": …}):
    {
        "id": "2026-11-20",        # 통계 대상 기간의 마지막 날. 1~10일 → -10, 1~20일 → -20, 월간 → 그달 말일.
                                   # 글 주소는 focus.html#note-2026-11-20
        "anchor": "…",             # 예전 주소를 지켜야 할 때만 쓴다. 보통은 넣지 않는다.
        "asof": "2026-11-23",      # 기준일(글을 쓴 날)
        "period": {…},             # "2026년 11월 1~20일 통계"
        "title": {…},              # 제목 한 줄
        "basis": {…},              # "기준일 2026년 11월 23일 · 관세청 11월 1~20일 수출입 현황(11월 23일 발표)"
        "points": {"ko": [..], …}, # 핵심 요지 (3개 안팎)
        "numbers": {…},            # 숫자 (4~5개. 직접 계산한 값은 "CSAI 계산"이라고 밝힌다)
        "reading": {…},            # 읽는 법 (2~3개)
        "korea": {…},              # 한국 시사점 (2개 안팎)
        "judgment": {"text": {…}, "invalid": {…}},   # 판단 한 문장과 무효화 조건. 원장이 확인한 것만. 없으면 생략
        "substack": "https://…",  # 영어판을 Substack에 올렸으면 그 글 주소 (없으면 넣지 않음)
        "example": {               # 연구원 소개·첫 화면 「우리가 서는 자리」 사례 상자. 최신 호의 것이 자동으로 쓰인다.
            "stats": [["+148%", {…}], ["49.7%", {…}]],   # 핵심 숫자 2개와 짧은 설명
            "verdict": {…},        # 판단을 한 구절로 (judgment 와 같은 뜻)
        },
        "exec_q": {…},             # 경영진 점검 질문 (2개 안팎). 한국 기업 경영진이 자기 회사에 던져 볼 질문. 아래에 '함께 점검하기' 문의 링크가 붙는다
        "next": {…},               # 다음에 확인할 것 (2~3개)
        "sources": [["출처 이름", "https://…"], …],
        "source_pre": {…},         # 출처 이름 앞에 붙일 말 (없으면 생략)
        "source_post": {…},        # 출처 이름 뒤에 붙일 말 (없으면 생략)
    }
"""

NEXT_ISSUE = {
    "ko": "2026년 11월 월간 통계가 발표되는 날(12월 1일)",
    "en": "The day the figures for November 2026 are released (1 December)",
    "zh": "2026年11月月度统计发布之日（12月1日）"
}

TENDAY = [
    {
        "id": "2026-11-20",
        "asof": "2026-11-23",
        "period": {
            "ko": "2026년 11월 1~20일 통계",
            "en": "1–20 November 2026",
            "zh": "2026年11月1至20日"
        },
        "title": {
            "ko": "대중 수출 급증은 20일까지 이어졌다. 늘어난 수출의 약 4분의 3은 반도체다",
            "en": "The surge in exports to China held through day 20. About three-quarters of the export gain is chips",
            "zh": "对华出口激增延续至20日，出口增量约四分之三来自半导体"
        },
        "basis": {
            "ko": "기준일 2026년 11월 23일 · 관세청 11월 1~20일 수출입 현황(11월 23일 발표)",
            "en": "As of 23 November 2026 · Korea Customs Service release for 1–20 November (published 23 November)",
            "zh": "基准日：2026年11月23日 · 韩国关税厅11月1至20日进出口现况（11月23日发布）"
        },
        "points": {
            "ko": [
                "11월 1~20일 대중 수출은 200억 달러로 1년 전보다 145.6% 늘었습니다. 1~10일의 증가율(148%)이 거의 그대로 이어졌습니다.",
                "같은 기간 전체 수출은 약 390억 달러 늘었고, 그 가운데 약 287억 달러(약 74%)가 반도체입니다(CSAI 계산). 반도체 비중은 49.7%로 1~10일과 같습니다.",
                "반도체를 뺀 수출도 약 36% 늘었지만(CSAI 계산), 그중 얼마가 중국으로 갔는지는 20일 통계로 알 수 없습니다. 대중 수출 급증을 중국 내수 회복으로 읽을 근거는 이번에도 없습니다."
            ],
            "en": [
                "Korea's exports to China in 1–20 November were $20.0bn, up 145.6% from a year earlier. Growth was almost the same as in 1–10 November (148%).",
                "Total exports rose by about $39.0bn in the period, and about $28.7bn of that (about 74%) was chips (CSAI arithmetic). Chips made up 49.7% of exports, the same share as in 1–10 November.",
                "Exports excluding chips also rose about 36% (CSAI arithmetic), but the 20-day release does not show how much of that went to China. It again gives no evidence that the jump in exports to China is a recovery in Chinese domestic demand."
            ],
            "zh": [
                "11月1日至20日，韩国对华出口为200亿美元，同比增长145.6%，与1日至10日的增速（148%）几乎持平。",
                "同期出口总额增加约390亿美元，其中约287亿美元（约74%）来自半导体（CSAI测算）。半导体占比为49.7%，与1日至10日相同。",
                "剔除半导体的出口也增长约36%（CSAI测算）。但其中有多少流向中国，二十日统计无从得知。这一次同样没有出现可以把对华出口激增解读为中国内需回暖的依据。"
            ]
        },
        "numbers": {
            "ko": [
                "전체 수출 774억 달러(+101.5%). 1~20일 기준 역대 최대. 일평균 48.4억 달러(+95.2%)",
                "반도체 385억 달러(+294.4%). 비중 49.7%, 1년 전보다 24.3%포인트 상승",
                "대중 수출 200억 달러(+145.6%), 대미 수출 164억 달러(+142.7%). 대만 +149.7%, 베트남 +85.8%, 유럽연합 +25.7%",
                "수입 503억 달러(+39.4%), 무역수지 271억 달러 흑자. 올해 누계 수출 1조 76억 달러(+63.2%). 11월 19일 처음 1조 달러를 넘음",
                "CSAI 계산: 반도체를 뺀 수출 약 389억 달러, 약 36% 증가(일평균 약 32%). 대중 비중 약 26%, 대미 약 21%(반올림된 공표치로 계산한 어림값)"
            ],
            "en": [
                "Total exports $77.4bn (+101.5%), a record for the first 20 days of a month. Daily average $4.84bn (+95.2%)",
                "Chips $38.5bn (+294.4%), 49.7% of exports, up 24.3 points from a year earlier",
                "To China $20.0bn (+145.6%); to the US $16.4bn (+142.7%). Taiwan +149.7%, Vietnam +85.8%, the EU +25.7%",
                "Imports $50.3bn (+39.4%), trade surplus $27.1bn. Exports for the year to date $1,007.6bn (+63.2%); they passed $1 trillion for the first time on 19 November",
                "CSAI arithmetic: exports excluding chips about $38.9bn, up about 36% (about 32% on a daily-average basis). China about 26% of exports, the US about 21% (approximations from rounded published figures)"
            ],
            "zh": [
                "出口总额774亿美元（+101.5%），创月度前20日历史新高；日均48.4亿美元（+95.2%）",
                "半导体385亿美元（+294.4%），占比49.7%，同比上升24.3个百分点",
                "对华出口200亿美元（+145.6%），对美出口164亿美元（+142.7%）；对台湾地区+149.7%，对越南+85.8%，对欧盟+25.7%",
                "进口503亿美元（+39.4%），贸易顺差271亿美元；今年累计出口10,076亿美元（+63.2%），于11月19日首次突破1万亿美元",
                "CSAI测算：剔除半导体的出口约389亿美元，同比增长约36%（按日均计算约32%）；对华占比约26%，对美约21%（依据四舍五入后的公布数据估算）"
            ]
        },
        "reading": {
            "ko": [
                "관세청 통계는 금액입니다. 한국은행 10월 수출물가지수에서 D램은 1년 전보다 199.4% 올랐습니다. 같은 물량을 팔아도 금액이 약 세 배가 됩니다. 다만 10월 수출물량지수도 43.9% 올라 역대 가장 큰 폭이었습니다. 금액 증가가 모두 가격은 아닙니다.",
                "증가율이 높은 곳은 대만, 중국, 미국, 베트남이고 유럽연합은 25.7%에 그쳤습니다. 반도체가 많이 가는 시장과 그렇지 않은 시장의 차이로 보입니다. 다만 20일 통계에는 나라별 품목 내역이 없어 ‘반도체를 뺀 대중 수출’과 ‘반도체를 뺀 전체 수출’을 견주지 못했습니다. 12월 1일 월간 통계에서 합니다.",
                "조업일수가 작년보다 0.5일 많았지만 일평균으로도 95.2% 늘었습니다. 작년 같은 기간 수출도 8.2% 늘었으니 기저효과도 아닙니다. 반도체에 더해 컴퓨터 주변기기(+330.6%)와 석유제품(+91.9%)까지 빼면 증가율은 약 21%입니다(CSAI 계산). 컴퓨터 주변기기에는 SSD처럼 메모리가 들어간 제품이 많고, 석유제품은 유가를 따라 움직입니다."
            ],
            "en": [
                "Customs figures are values. In the Bank of Korea's export price index for October, DRAM prices were up 199.4% from a year earlier. The same volume now brings in about three times the value. But the export volume index also rose 43.9% in October, its largest rise on record. Not all of the gain in value is price.",
                "Growth was highest to Taiwan, China, the US and Vietnam. To the EU it was only 25.7%. This looks like the gap between markets that take many chips and markets that do not. But the 20-day release has no product breakdown by country, so we could not compare exports to China excluding chips with total exports excluding chips. We will do so with the monthly data on 1 December.",
                "There was half a working day more than last year, but the daily average still rose 95.2%. Exports in the same period last year rose 8.2%, so this is not a low base either. Take out computer peripherals (+330.6%) and petroleum products (+91.9%) as well as chips, and growth is about 21% (CSAI arithmetic). Many computer peripherals, such as SSDs, contain memory, and petroleum products follow oil prices."
            ],
            "zh": [
                "关税厅的统计是金额。韩国银行10月出口物价指数显示，DRAM价格同比上涨199.4%，也就是说，即使出口数量不变，金额也会变成约三倍。不过，10月出口数量指数也上升43.9%，升幅为历史最高。金额的增加不能全部归因于价格。",
                "增速高的是台湾地区、中国、美国和越南，对欧盟只增长25.7%。这看起来是半导体流向多的市场与流向少的市场之间的差别。不过，二十日统计没有分国别的品类明细，因此这次无法比较“剔除半导体的对华出口”与“剔除半导体的整体出口”，将在12月1日的月度统计中进行。",
                "工作日比去年多0.5天，但日均出口仍增长95.2%。去年同期出口也增长8.2%，因此也不是低基数效应。除半导体外，再剔除计算机周边设备（+330.6%）和石油制品（+91.9%），增速约为21%（CSAI测算）。计算机周边设备中有不少像固态硬盘（SSD）这样含有存储芯片的产品，石油制品则随油价波动。"
            ]
        },
        "korea": {
            "ko": [
                "수출 1조 달러, 일평균 48억 달러 같은 기록을 끌어올린 것은 반도체입니다. 반도체 밖 기업이 수출 총액이나 대중 수출 총액을 근거로 투자와 채용을 늘리면 실제 주문보다 앞서 갈 수 있습니다. 자기 품목의 주문 물량과 단가를 따로 봐야 합니다.",
                "수입도 39.4% 늘었고, 원유(+83.4%)와 가스(+93.9%)의 증가가 큽니다. 수출 호황과 원가 부담이 함께 커지고 있습니다. 에너지와 원재료 비중이 큰 기업은 원가 상승분을 판매가에 얼마나 옮길 수 있는지, 조달 계약의 가격 조건은 어떤지 점검할 때입니다."
            ],
            "en": [
                "Chips are what lifted records such as $1 trillion in exports and a $4.8bn daily average. A company outside chips that expands investment and hiring on the strength of total exports, or of total exports to China, may run ahead of its real orders. It should look at order volumes and prices for its own products.",
                "Imports also rose 39.4%, with large increases in crude oil (+83.4%) and gas (+93.9%). The export boom and cost pressure are growing together. Companies with large energy and raw-material costs should check how much of the cost increase they can pass on to selling prices, and what the price terms in their supply contracts are."
            ],
            "zh": [
                "把出口推上1万亿美元、日均48亿美元这些纪录的是半导体。半导体以外的企业如果以出口总额或对华出口总额为依据扩大投资和招聘，可能会走在实际订单前面，应当单独看本企业产品的订单数量和单价。",
                "进口也增长39.4%，其中原油（+83.4%）和天然气（+93.9%）增幅较大。出口繁荣与成本压力同时加大。能源和原材料占比高的企业，现在应当检查成本上涨能在多大程度上转嫁到售价，以及采购合同的价格条款。"
            ]
        },
        # 이번 호에는 새 판단이 없어 "judgment" 를 넣지 않았다.
        # "example" 도 넣지 않았다: 첫 화면 사례 상자의 마지막 칸에는 '판단' 표지가 자동으로 붙는데,
        # 판단이 없는 호를 어떻게 보일지 원장 확인 전이라 첫 화면은 지난 호(11월 1~10일) 상자를 그대로 쓴다.
        "exec_q": {
            "ko": [
                "중국 거래처로 가는 우리 제품은 중국 안에서 쓰이는가, 조립돼 다른 나라로 다시 나가는가?",
                "오른 에너지·원재료 값을 판매가에 얼마나 옮기고 있는가? 옮기지 못한 몫은 누가 지고 있는가?"
            ],
            "en": [
                "Are your products shipped to Chinese customers used inside China, or assembled and exported again to other countries?",
                "How much of the higher energy and raw-material cost are you passing on to selling prices? Who is bearing the part you cannot pass on?"
            ],
            "zh": [
                "发往中国客户的本公司产品，是在中国境内使用，还是经组装后再出口到其他国家？",
                "上涨的能源和原材料成本，有多少转嫁到了售价？无法转嫁的部分由谁承担？"
            ]
        },
        "next": {
            "ko": [
                "12월 1일 산업통상부 11월 수출입 동향에서 반도체를 뺀 대중 수출이 반도체를 뺀 전체 수출보다 빠르게 늘었는지. 지난 호 판단의 무효화 조건입니다.",
                "12월 중순 무렵 한국은행 11월 수출물가·무역지수에서 D램 가격과 수출물량이 함께 오르는지",
                "11월 월간 반도체 비중이 50%를 넘는지. 1조 달러를 넘은 시점의 누계 반도체 비중은 보도마다 달라 관세청 자료로 확인하겠습니다."
            ],
            "en": [
                "Whether exports to China excluding chips grew faster than total exports excluding chips in the trade ministry's November figures on 1 December. This is the invalidation condition of our previous judgment.",
                "Whether DRAM prices and export volumes rise together again in the Bank of Korea's November export price and trade indexes, due around mid-December",
                "Whether chips pass 50% of exports for November as a whole. Reports differ on the chip share of year-to-date exports when the $1 trillion mark was passed; we will confirm it from customs data."
            ],
            "zh": [
                "12月1日产业通商部11月进出口动向中，剔除半导体的对华出口增速是否快于剔除半导体的整体出口。这是上一期判断的失效条件。",
                "12月中旬前后韩国银行11月出口物价与贸易指数中，DRAM价格与出口数量是否继续同步上升",
                "11月全月半导体占比是否超过50%。突破1万亿美元时的累计半导体占比，各家报道不一，将以关税厅资料核实。"
            ]
        },
        "sources": [
            [
                "아주경제",
                "https://www.ajunews.com/view/20261123092143955"
            ],
            [
                "포인트경제",
                "https://www.pointe.co.kr/news/articleView.html?idxno=88212"
            ],
            [
                "The Korea Times",
                "https://www.koreatimes.co.kr/economy/others/20261123/exports-more-than-double-in-1st-20-days-of-november-with-chip-shipments-surging-to-new-high"
            ],
            [
                "메트로신문",
                "https://www.metroseoul.co.kr/article/20261112500417"
            ],
            [
                "EBN",
                "https://www.ebn.co.kr/news/articleView.html?idxno=1731501"
            ],
            [
                "KDI 경제교육·정보센터",
                "https://eiec.kdi.re.kr/policy/materialView.do?num=273703"
            ]
        ],
        "source_pre": {
            "ko": "관세청 발표(2026.11.23)와 한국은행 10월 수출물가·무역지수(2026.11.13)를 전한 보도, 그리고 지난해 같은 기간 통계: ",
            "en": "Reports of the Korea Customs Service release (23 Nov 2026) and the Bank of Korea's October price and trade indexes (13 Nov 2026), and last year's release for the same period: ",
            "zh": "转引韩国关税厅数据（2026.11.23）与韩国银行10月出口物价、贸易指数（2026.11.13）的报道及去年同期统计："
        },
        "source_post": {
            "ko": ". 비중, 반도체 제외 수치, 증가분에서 반도체가 차지하는 몫은 CSAI 계산입니다.",
            "en": ". Shares, ex-chip figures and the chip share of the gain are CSAI arithmetic.",
            "zh": "。占比、剔除半导体的数值及半导体在增量中的比重为CSAI测算。"
        }
    },
    {
        "id": "2026-11-10",
        "anchor": "flash-2026-11",
        "asof": "2026-11-15",
        "period": {
            "ko": "2026년 11월 1~10일 통계",
            "en": "1–10 November 2026",
            "zh": "2026年11月1至10日"
        },
        "title": {
            "ko": "반도체가 끌어올린 대중 수출, 중국 수요로 읽으면 안 되는 이유",
            "en": "Chips lifted exports to China. Why that is not Chinese demand",
            "zh": "半导体拉高了对华出口：为什么不能把它读成中国需求"
        },
        "basis": {
            "ko": "기준일 2026년 11월 15일 · 관세청 11월 1~10일 수출입 현황(11월 11일 발표)",
            "en": "As of 15 November 2026 · Korea Customs Service release for 1–10 November (published 11 November)",
            "zh": "基准日：2026年11月15日 · 韩国关税厅11月1至10日进出口现况（11月11日发布）"
        },
        "points": {
            "ko": [
                "11월 1~10일 대중 수출은 91.6억 달러로 1년 전보다 148% 늘었습니다.",
                "같은 기간 반도체 수출이 331.2% 늘어 전체 수출의 49.7%를 차지했습니다. 대중 수출 급증도 반도체가 끌었을 가능성이 큽니다.",
                "그래서 이 숫자를 ‘중국 내수가 살아났다’는 신호로 읽기는 이릅니다. 가격이 오른 것인지 물량이 늘어난 것인지를 갈라 봐야 합니다."
            ],
            "en": [
                "Korea's exports to China in 1–10 November were $9.16bn, up 148% from a year earlier.",
                "Chip exports rose 331.2% in the same period and made up 49.7% of all exports, so chips probably drove the jump in shipments to China as well.",
                "It is too early to read this as a recovery in Chinese domestic demand. Price and volume have to be separated first."
            ],
            "zh": [
                "11月1日至10日，韩国对华出口为91.6亿美元，同比增长148%。",
                "同期半导体出口增长331.2%，占全部出口的49.7%，对华出口的激增很可能同样由半导体带动。",
                "因此，把这一数字解读为“中国内需回暖”为时尚早，必须先区分价格与数量。"
            ]
        },
        "numbers": {
            "ko": [
                "전체 수출 335억 달러(+111.9%). 11월 1~10일 기준 역대 최대",
                "반도체 166억 달러(+331.2%). 비중 49.7%, 1년 전보다 25.3%포인트 상승",
                "대중 수출 91.6억 달러(+148%), 대미 수출 67.9억 달러(+163.6%)",
                "수입 247억 달러, 무역수지 88억 달러 흑자. 올해 누계 수출 9,636억 달러",
                "CSAI 계산: 대중 비중 약 27%, 대미 약 20%. 반도체를 뺀 수출은 약 169억 달러로 1년 전보다 40% 남짓 증가(반올림된 공표치로 계산한 어림값)"
            ],
            "en": [
                "Total exports $33.5bn (+111.9%), a record for 1–10 November",
                "Chips $16.6bn (+331.2%), 49.7% of exports, up 25.3 points from a year earlier",
                "To China $9.16bn (+148%); to the US $6.79bn (+163.6%)",
                "Imports $24.7bn, trade surplus $8.8bn; exports for the year to date $963.6bn",
                "CSAI arithmetic: China about 27% of exports, the US about 20%; exports excluding chips about $16.9bn, up a little over 40% (an approximation from rounded published figures)"
            ],
            "zh": [
                "出口总额335亿美元（+111.9%），创11月1至10日历史新高",
                "半导体166亿美元（+331.2%），占比49.7%，同比上升25.3个百分点",
                "对华出口91.6亿美元（+148%），对美出口67.9亿美元（+163.6%）",
                "进口247亿美元，贸易顺差88亿美元；今年累计出口9,636亿美元",
                "CSAI测算：对华占比约27%，对美约20%；剔除半导体的出口约169亿美元，同比增长40%出头（依据四舍五入后的公布数据估算）"
            ]
        },
        "reading": {
            "ko": [
                "대중 수출 증가율(148%)은 전체(111.9%)보다 높지만 반도체(331.2%)보다는 한참 낮습니다. 반도체를 빼면 전체 수출 증가율은 40% 안팎으로 내려옵니다. 대중 수출도 같은 구조일 가능성이 큽니다.",
                "메모리 가격이 오르면 같은 물량을 팔아도 수출액은 늘어납니다. 금액이 늘었다고 중국이 더 많이 사 갔다고 읽을 수는 없습니다.",
                "10일 통계에는 나라별 품목 내역과 물량이 없습니다. 조업일수 차이도 걸러지지 않았습니다. 가격 효과와 물량 효과는 월간 확정치에서 갈라 보겠습니다."
            ],
            "en": [
                "Growth to China (148%) is above the total (111.9%) but far below chips (331.2%). Excluding chips, total export growth falls to around 40%, and shipments to China probably have the same structure.",
                "When memory prices rise, export value rises even on the same volume. A higher value does not mean China bought more.",
                "The ten-day release has no product breakdown by country, no volumes and no working-day adjustment. We will separate price and volume effects in the monthly data."
            ],
            "zh": [
                "对华出口增速（148%）高于整体（111.9%），但远低于半导体（331.2%）。剔除半导体后，整体出口增速降至40%左右，对华出口很可能是同样的结构。",
                "存储芯片价格上涨时，即使数量不变，出口额也会增加。金额增加不等于中国买得更多。",
                "十日统计没有分国别的品类明细和数量，也未剔除工作日差异。价格效应与数量效应将在月度确定值中拆分。"
            ]
        },
        "korea": {
            "ko": [
                "대중 수출이 좋아 보이는 것은 ‘반도체가 좋다’는 뜻에 가깝습니다. 석유화학, 철강, 일반기계처럼 중국 수요에 기대는 업종은 이 숫자를 회복의 근거로 삼기 어렵습니다.",
                "수출의 절반이 한 품목에서 나옵니다. 메모리 가격이 꺾이면 대중 수출과 무역수지가 함께 흔들립니다. 가격·조달·투자 계획에서 반도체 경기와 중국 수요를 따로 놓고 봐야 합니다."
            ],
            "en": [
                "Strong exports to China mostly mean strong chips. Sectors that depend on Chinese demand, such as petrochemicals, steel and general machinery, cannot take this figure as evidence of recovery.",
                "Half of all exports now come from one product. If memory prices turn, exports to China and the trade balance move together. Plans for pricing, sourcing and investment should treat the chip cycle and Chinese demand separately."
            ],
            "zh": [
                "对华出口看起来强劲，更接近“半导体强劲”的意思。石化、钢铁、一般机械等依赖中国需求的行业，难以把这一数字当作回暖的依据。",
                "一半的出口来自单一品类。存储价格一旦回落，对华出口与贸易收支将同时波动。在定价、采购和投资计划中，应把半导体景气与中国需求分开看。"
            ]
        },
        "judgment": {
            "text": {
                "ko": "11월 초 대중 수출 급증은 중국 내수 회복이 아니라 반도체 가격 효과가 이끈 것이다.",
                "en": "The surge in Korea's exports to China in early November was driven by chip prices, not by a recovery in Chinese domestic demand.",
                "zh": "11月初韩国对华出口激增，是半导体价格效应带动的，而不是中国内需回暖。"
            },
            "invalid": {
                "ko": "12월 1일 월간 통계에서 반도체를 뺀 대중 수출이 반도체를 뺀 전체 수출보다 빠르게 늘면 이 판단을 거둔다.",
                "en": "We withdraw this judgment if the monthly data on 1 December show exports to China excluding chips growing faster than total exports excluding chips.",
                "zh": "若12月1日的月度统计显示剔除半导体的对华出口增速快于剔除半导体的整体出口，则撤回这一判断。"
            }
        },
        "substack": "https://csai2026.substack.com/p/chips-lifted-exports-to-china-why",
        "example": {
            "stats": [
                ["+148%", {"ko": "대중 수출 증가", "en": "exports to China", "zh": "对华出口增长"}],
                ["49.7%", {"ko": "전체 수출 중 반도체 비중", "en": "chips' share of all exports", "zh": "半导体占出口比重"}]
            ],
            "verdict": {"ko": "중국 수요 회복이 아니라 반도체 가격 효과", "en": "chip prices, not a recovery in Chinese demand", "zh": "是半导体价格效应，而非中国需求回暖"}
        },
        "exec_q": {
            "ko": [
                "우리 회사의 대중 매출 증가는 단가 상승 때문인가, 주문 물량 증가 때문인가?",
                "중국 고객의 주문이 반도체 밖 품목에서도 늘고 있는가?"
            ],
            "en": [
                "Is your company's growth in sales to China coming from higher prices or from larger order volumes?",
                "Are Chinese customers ordering more of products other than chips?"
            ],
            "zh": [
                "贵公司对华销售增长来自单价上涨，还是订单数量增加？",
                "中国客户在半导体以外的品类上是否也在增加订单？"
            ]
        },
        "next": {
            "ko": [
                "11월 1~20일 통계에서 대중 수출 증가율이 이어지는지",
                "12월 1일 월간 수출입 동향에서 반도체를 뺀 대중 수출이 얼마나 늘었는지. 이 숫자가 반도체를 뺀 전체 수출보다 빠르게 늘면 ‘중국 수요 회복’ 해석에 힘이 실립니다.",
                "연간 수출 1조 달러를 넘는 시점과 그때의 반도체 비중"
            ],
            "en": [
                "Whether growth to China holds in the 1–20 November release",
                "How much exports to China excluding chips grew in the monthly data due on 1 December. If they grow faster than total exports excluding chips, the case for a recovery in Chinese demand strengthens.",
                "When annual exports pass $1 trillion, and the chip share at that point"
            ],
            "zh": [
                "11月1至20日统计中对华出口增速能否延续",
                "12月1日月度进出口动向中，剔除半导体的对华出口增长多少。若其增速快于剔除半导体的整体出口，“中国需求回暖”的解读将更有说服力。",
                "年度出口突破1万亿美元的时点及届时的半导体占比"
            ]
        },
        "sources": [
            [
                "The Korea Times",
                "https://www.koreatimes.co.kr/economy/others/20261111/exports-more-than-double-in-1st-10-days-of-november"
            ],
            [
                "Korea JoongAng Daily",
                "https://www.koreajoongangdaily.com/business/exports-more-than-double-in-1st-10-days-of-november/12966595"
            ]
        ],
        "source_pre": {
            "ko": "관세청 발표를 전한 ",
            "en": "Korea Customs Service figures as reported by ",
            "zh": "转引韩国关税厅数据的"
        },
        "source_post": {
            "ko": " 보도(2026.11.11). 비중과 반도체 제외 수치는 CSAI 계산입니다.",
            "en": " (11 Nov 2026). Shares and ex-chip figures are CSAI arithmetic.",
            "zh": "报道（2026.11.11）。占比与剔除半导体的数值为CSAI测算。"
        }
    }
]
