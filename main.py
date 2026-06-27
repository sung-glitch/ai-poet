#from dotenv import load_dotenv
#load_dotenv()
from langchain_openai import OpenAI, ChatOpenAI
import streamlit as st

chat_model = ChatOpenAI()

st.title("인공지능 시인")

content = st.text_input("시의 주제를 입력해주세요")


if st.button("시 생성"):

    with st.spinner("시를 생성하는 중입니다..."):

        result = chat_model.invoke(content + "에 대한 시를 생성해줘")
        st.write(result.content)
