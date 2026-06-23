import streamlit as st
import requests
from datetime import datetime

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:
    st.title("🤖 AI Agent")

    st.markdown(
        """
        Ask questions and get answers from your AI Agent.
        """
    )

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# -------------------------
# SESSION STATE
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# HEADER
# -------------------------
st.title("🤖 AI Agent")
st.caption("Powered by LangChain + FastAPI")

# -------------------------
# DISPLAY CHAT HISTORY
# -------------------------
for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar="👤" if message["role"] == "user" else "🤖"
    ):
        st.markdown(message["content"])

        if "timestamp" in message:
            st.caption(message["timestamp"])

# -------------------------
# USER INPUT
# -------------------------
prompt = st.chat_input("Ask me anything...")

if prompt:

    current_time = datetime.now().strftime("%I:%M %p")

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
            "timestamp": current_time
        }
    )

    # Show user message immediately
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        st.caption(current_time)

    # Assistant response
    with st.chat_message("assistant", avatar="🤖"):

        response_placeholder = st.empty()

        try:
            with st.spinner("Thinking..."):

                response = requests.post(
                    "https://ai-agent-latest-64mk.onrender.com/chat",
                    json={"question": prompt},
                    timeout=120
                )

                response.raise_for_status()

                data = response.json()

                answer = data.get(
                    "answer",
                    "No answer received from the server."
                )

            response_placeholder.markdown(answer)

            response_time = datetime.now().strftime("%I:%M %p")
            st.caption(response_time)

            # Save assistant response
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "timestamp": response_time
                }
            )

        except requests.exceptions.Timeout:

            error_message = (
                "⏳ Request timed out. Please try again."
            )

            response_placeholder.error(error_message)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message,
                    "timestamp": datetime.now().strftime("%I:%M %p")
                }
            )

        except requests.exceptions.RequestException as e:

            error_message = f"❌ Connection Error: {e}"

            response_placeholder.error(error_message)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message,
                    "timestamp": datetime.now().strftime("%I:%M %p")
                }
            )

        except Exception as e:

            error_message = f"❌ Unexpected Error: {e}"

            response_placeholder.error(error_message)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message,
                    "timestamp": datetime.now().strftime("%I:%M %p")
                }
            )