from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
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

messages = [
    SystemMessage(content="You are a helpful assistance"),
    HumanMessage(content="Hello How Are You")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)
