from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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

chat_history = [
    SystemMessage(content="You are a Experiance Doctor ! ")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    else:
        result = model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print(result.content)
    
print(chat_history)