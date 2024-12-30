import streamlit as st
from src.modules.query import query_data
from src.modules.extraction import generate_data_store
from dotenv import load_dotenv
import os
import openai
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "model_settings" not in st.session_state:
    st.session_state.model_settings = {"temperature": 0.7}

st.set_page_config(page_title="RAG Chat Assistant", layout="wide")
st.title("RAG Chat Assistant")

with st.sidebar:
    st.header("🔧 Settings")
    if st.button("Regenerate Data Store"):
        with st.spinner("Regenerating data store..."):
            generate_data_store()
        st.success("Data store regenerated successfully!")

    st.subheader("Model Settings")
    st.slider(
        "Response Temperature",
        0.0,
        1.0,
        st.session_state.model_settings["temperature"],
        key="temperature_slider",
    )
    if st.button("Reset Chat"):
        st.session_state.messages = []
        st.info("Chat reset successfully!")

    st.markdown("---")
    st.markdown("**About this App:**")
    st.write(
        "This is a Retrieval-Augmented Generation (RAG) chat system. Enter a query and get contextual responses sourced from your data."
    )

st.write("💬 Start a conversation below:")
user_input = st.text_input("Your query:", key="query_input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        time.sleep(1)
        response = query_data(user_input)

    if response:
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.session_state.messages.append(
            {"role": "assistant", "content": "No relevant information found."}
        )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if len(message["content"]) > 200:
            with st.expander("Click to expand message"):
                st.markdown(message["content"])
        else:
            st.markdown(message["content"])

if st.session_state.messages:
    with st.expander("💾 Download Chat History"):
        chat_history = "\n".join(
            [
                f"{msg['role'].capitalize()}: {msg['content']}"
                for msg in st.session_state.messages
            ]
        )
        st.download_button(
            label="Download Chat History",
            data=chat_history,
            file_name="chat_history.txt",
            mime="text/plain",
        )
