from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model = ChatGroq(
    model="gemma2-9b-it"
)
template1 = PromptTemplate(
    template='Givea report on {topic}',
    input_variables=['topic']
)
template2 = PromptTemplate(
    template="Generate Summary on {text}",
    input_variables=['text']
)
parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser 
result = chain.invoke({'topic':'AI Evolution in India'})
chain.get_graph().print_ascii()