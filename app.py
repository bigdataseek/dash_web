import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 로드
df = px.data.gapminder()

# 제목 표시
st.title("국가별 GDP 변화")

# 드롭다운 메뉴
country_list = df["country"].unique()
selected_country = st.selectbox("국가를 선택하세요:", country_list)

# 데이터 필터링
filtered_df = df[df["country"] == selected_country]

# 그래프 생성
fig = px.line(filtered_df, x="year", y="gdpPercap", title=f"{selected_country}의 GDP 변화")
st.plotly_chart(fig)
