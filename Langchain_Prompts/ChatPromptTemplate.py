from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompts = chat_template.invoke({
    'domain':'cricket',
    'topic':'dusra'
})

print(prompts)