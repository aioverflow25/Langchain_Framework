from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model = ChatGroq(
    model="gemma2-9b-it"
)
template = PromptTemplate(
    template='Give 5 facts about {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()
chain = template | model | parser
result = chain.invoke({'topic':'M.S. Dhoni'})
print(result)