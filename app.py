import streamlit as st

st.set_page_config(page_title="나와 어울리는 도시는?", page_icon="🏙️")

st.title("🏙️ 나와 어울리는 도시는?")
st.caption("3개의 질문에 답하면, 당신의 라이프스타일과 어울리는 도시를 찾아드려요!")

st.divider()

# 선택지 -> 도시 점수 매핑
# 도시 키: tokyo, newyork, paris, bali
Q1 = {
    "맛있는 음식": "paris",
    "새로운 문화 체험": "tokyo",
    "자연과 휴식": "bali",
    "쇼핑과 트렌드": "newyork",
}

Q2 = {
    "계획표대로 움직인다": "tokyo",
    "즉흥적으로 흘러간다": "newyork",
    "여유롭게 느리게": "bali",
    "바쁘고 에너지 넘치게": "newyork",
}

Q3 = {
    "조용한 카페": "paris",
    "사람 많은 거리": "newyork",
    "자연이 보이는 곳": "bali",
    "화려한 도심 한가운데": "tokyo",
}

RESULTS = {
    "tokyo": {
        "emoji": "🗼🇯🇵",
        "name": "도쿄",
        "desc": "섬세하고 계획적인 타입. 혼자서도 잘 즐기며 디테일을 중요시해요.",
    },
    "newyork": {
        "emoji": "🗽🇺🇸",
        "name": "뉴욕",
        "desc": "에너지 넘치고 도전적인 타입. 빠른 속도와 자극 속에서 살아나는 스타일이에요!",
    },
    "paris": {
        "emoji": "🥐🇫🇷",
        "name": "파리",
        "desc": "감성적이고 예술적인 타입. 분위기와 취향, 아름다운 디테일을 소중히 해요.",
    },
    "bali": {
        "emoji": "🌴🇮🇩",
        "name": "발리",
        "desc": "힐링과 균형을 추구하는 타입. 자연과 여유가 있을 때 가장 빛나요.",
    },
}


def pick_winner(scores: dict) -> str:
    """최고점 도시를 선택. 동점이면 우선순위로 결정."""
    priority = ["tokyo", "newyork", "paris", "bali"]  # 동점일 때 우선순위
    max_score = max(scores.values())
    tied = [k for k, v in scores.items() if v == max_score]
    for k in priority:
        if k in tied:
            return k
    return tied[0]


# 질문 UI (radio)
a1 = st.radio("Q1. 여행을 간다면 가장 중요한 것은?", list(Q1.keys()), index=0)
a2 = st.radio("Q2. 당신의 하루 리듬은?", list(Q2.keys()), index=0)
a3 = st.radio("Q3. 가장 끌리는 공간은?", list(Q3.keys()), index=0)

st.divider()

if st.button("결과 보기", type="primary"):
    scores = {"tokyo": 0, "newyork": 0, "paris": 0, "bali": 0}
    scores[Q1[a1]] += 1
    scores[Q2[a2]] += 1
    scores[Q3[a3]] += 1

    winner = pick_winner(scores)
    r = RESULTS[winner]

    st.subheader(f"{r['emoji']} 당신과 어울리는 도시는 **{r['name']}**!")
    st.write(r["desc"])

    st.info(f"공유 문구: 나는 {r['emoji']} {r['name']} 타입! 🏙️✨")

    with st.expander("내 선택 점수 보기"):
        st.write(scores)

st.caption("Tip: `streamlit run app.py` 로 실행할 수 있어요.")
