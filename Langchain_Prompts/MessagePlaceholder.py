from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat Prompt Template
chat_template = ChatPromptTemplate.from_messages([
    ('system','you are a customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chathistory = []

with open('Langchain_Prompts\chathistory.txt') as f:
    chathistory.append(f.readlines())

print(chathistory)

# Create prompt

prompt = chat_template.invoke({
    'chat_history':chathistory,
    'query':'where is my refund'
})

print(prompt)
