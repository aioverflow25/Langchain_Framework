from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()
from huggingface_hub import login
llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation"
)
login(token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))
model = ChatHuggingFace(llm=llm)
st.header('Reasearch Tool')
user_input = st.text_input('Enter Your Prompt')
if st.button('Summerize'):
    result = model.invoke(user_input)
    st.write(result.content)

