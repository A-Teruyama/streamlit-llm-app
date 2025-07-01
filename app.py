from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

import streamlit as st

st.title("Lesson21 Chapter6【提出課題】: 健康相談Webアプリ")

st.write("##### 心と体それぞれの健康について、専門家AIに相談できます。")


selected_item = st.radio(
    "心の健康については「メンタルヘルス専門家」、体の健康については「フィジカルヘルス専門家」を選択して、相談してください。",
    ["メンタルヘルス専門家", "フィジカルヘルス専門家"]
)

st.divider()
input_message = st.text_input("相談内容を入力して、「相談」ボタンを押してください。")

def health_advice(selected_item, input_message, llm):
    messages = [
        SystemMessage(content=f"あなたは相談者に寄り添う、優秀な{selected_item}です。相談に対して50字程度で答えてください。"),
        HumanMessage(content=input_message),
    ]
    result = llm.invoke(messages)
    return result.content

if st.button("相談"):
    st.divider()
    if input_message:  # 入力が空でない場合のみ処理を実行
        with st.spinner("AIが相談に応じています..."):
            response = health_advice(selected_item, input_message, llm)
        st.write(f"**{selected_item}の回答:** {response}")

    else:
        st.error("相談内容を入力してください。")
        st.stop()