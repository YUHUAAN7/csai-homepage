# -*- coding: utf-8 -*-
"""「영상 해설」 회차 목록. 유튜브 「안유화경제투자론」 한 편마다 한 항목.

- 최신 회차를 EPISODES 맨 위에 추가하고 `python3 src/build.py` 를 실행한다.
- 여기에는 무료 공개분(요약)만 넣는다. 이 저장소는 공개이므로
  대본 전문과 근거 자료 묶음은 절대 넣지 않는다(유료 제공분, 별도 보관).

항목 형식:
    {
        "date": "2026-11-17",                      # 영상 공개일
        "title": "영상 제목",
        "youtube": "https://www.youtube.com/watch?v=영상ID",
        "points": ["핵심 요지 1", "핵심 요지 2", "핵심 요지 3"],
        "summary": "대본 요약 (500자 안팎, 문단 구분은 빈 줄)",
        "implication": "한국 시사점",
        "judgment": {"asof": "2026-11-17", "text": "판단 한 문장", "invalid": "무효화 조건"},   # 없으면 생략
        "sources": [("출처 이름", "https://...")],
    }
"""

EPISODES = []
