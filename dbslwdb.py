import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 경쟁사 분석
# -----------------------------
elif menu == "경쟁 브랜드 분석":

    st.subheader("📈 경쟁 브랜드 분석")

    selected_brand = st.selectbox(
        "브랜드 선택",
        products["브랜드"].unique()
    )

    filtered = products[products["브랜드"] == selected_brand]

    st.dataframe(filtered, use_container_width=True)

    scatter = px.scatter(
        products,
        x="가격",
        y="평점",
        size="판매량",
        color="브랜드",
        hover_name="제품",
        title="경쟁 브랜드 포지셔닝"
    )

    st.plotly_chart(scatter, use_container_width=True)

# -----------------------------
# 퍼스널 컬러 추천
# -----------------------------
elif menu == "퍼스널 컬러 추천":

    st.subheader("🎨 퍼스널 컬러 추천")

    skin_tone = st.selectbox(
        "피부 톤 선택",
        ["봄 웜", "여름 쿨", "가을 웜", "겨울 쿨"]
    )

    color_map = {
        "봄 웜": ["코랄", "피치", "살몬 핑크"],
        "여름 쿨": ["로즈", "모브", "쿨 핑크"],
        "가을 웜": ["브릭", "테라코타", "브라운 레드"],
        "겨울 쿨": ["버건디", "체리 레드", "플럼"]
    }

    recommended = color_map[skin_tone]

    st.success(f"추천 컬러: {', '.join(recommended)}")

    color_df = pd.DataFrame({
        "추천 컬러": recommended,
        "트렌드 점수": [92, 88, 85]
    })

    color_chart = px.bar(
        color_df,
        x="추천 컬러",
        y="트렌드 점수",
        title="퍼스널 컬러 추천 점수"
    )

    st.plotly_chart(color_chart, use_container_width=True)
