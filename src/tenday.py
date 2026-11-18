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
    "ko": "2026년 11월 1~20일 통계가 발표되는 날",
    "en": "The day the figures for 1–20 November 2026 are released",
    "zh": "2026年11月1至20日统计发布之日"
}

TENDAY = [
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
