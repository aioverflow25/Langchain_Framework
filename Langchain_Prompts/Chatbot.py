from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.schema import HumanMessage, AIMessage
from huggingface_hub import login
import os
load_dotenv()
import streamlit as st
llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation"
)
login(token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))
model = ChatHuggingFace(llm=llm)

st.header("CHATBOT")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input
user_input = st.text_input("You: ", "")

if st.button('send'):
    if user_input.strip().lower() == "exit":
        st.write("Chatbot Session Ended !!")
        st.stop()
    if user_input:
        st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    # Thinking
    with st.spinner("Thinking..... "):
        result = model.invoke(st.session_state.chat_history)
    
    st.session_state.chat_history.append(AIMessage(content=result.content))

#Display Chat History
for message in st.session_state.chat_history:
    if isinstance(message,HumanMessage):
        st.write(f"**You:** {message.content}")
    else:
        st.write(f"**AI:** {message.content}")
