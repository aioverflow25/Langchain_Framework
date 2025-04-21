from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, load_prompt
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
st.header('Reasearch Paper Tool')
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

#prompt = template.invoke(
#    {
 #       'paper_input':paper_input,
 #       'style_input':style_input,
 #       'length_input':length_input
 #   }
#)

if st.button('Summerize'):
    chain = template | model
    result = chain.invoke(
        {
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
        }
    )
    st.write(result.content)