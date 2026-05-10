import streamlit as st
import requests

st.set_page_config(page_title="AI Agent", layout="wide")

st.title("🤖 AI Agent (LangChain Advanced)")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.chat.append(("user", user_input))

    with st.spinner("Thinking..."):
        res = requests.post(
            "http://localhost:8000/chat",
            json={"question": user_input}
        )
        answer = res.json()["answer"]

    st.session_state.chat.append(("ai", answer))

for role, msg in st.session_state.chat:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)