from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model1 = ChatGroq(
    model="gemma2-9b-it"
)
model2 = ChatGroq(
    model="gemma2-9b-it"
)
from langchain.schema.runnable import RunnableParallel
prompt1 = PromptTemplate(
    template= " Give Short and concise notes on {text}",
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template="Give 5 Mcqs quiz Based on the following text -> {text}",
    input_variables=['text']
)
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)
parser = StrOutputParser()
parallel_chains = RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})
merge_chain = prompt3 | model1 | parser

chain = parallel_chains | merge_chain

result = chain.invoke({'text':
                       """
LangChain: A Comprehensive Overview

Introduction

LangChain is an open-source framework designed to simplify the development of applications powered by Large Language Models (LLMs). It enables seamless integration of LLMs with external data sources, APIs, memory, and agents to build robust, scalable, and context-aware applications.

Key Features of LangChain

Prompt Management: Provides tools to create, manage, and optimize prompts for LLM interactions.

Chains: Enables chaining multiple components together, allowing for sequential execution of prompts and functions.

Memory: Implements stateful interactions by storing and retrieving conversational history.

Agents and Tools: Facilitates dynamic decision-making by using LLMs to choose from multiple tools or functions at runtime.

Retrieval-Augmented Generation (RAG): Enhances responses by fetching and incorporating external data sources.

Integrations: Supports a wide range of third-party services, including vector databases (Pinecone, FAISS), APIs, and cloud platforms.

Use Cases

Chatbots and Virtual Assistants: Develop AI-driven conversational agents with memory and tool use.

Document Processing: Automate text summarization, extraction, and analysis from large datasets.

Code Generation and Assistance: Utilize LLMs to generate, debug, and optimize code snippets.

Question Answering Systems: Build intelligent QA models using external knowledge bases.

Autonomous Agents: Create AI agents capable of planning and executing tasks dynamically.

Advantages of Using LangChain

Modular and Flexible: Provides a component-based architecture for easy customization.

Scalability: Supports efficient handling of large-scale AI applications.

Community and Ecosystem: Rapidly growing open-source community with extensive documentation.

Interoperability: Compatible with multiple LLM providers, including OpenAI, Hugging Face, and Anthropic.

Challenges and Considerations

Complexity: Requires knowledge of prompt engineering, chaining, and API integration.

Latency Issues: Performance may depend on the underlying LLM’s response time.

Cost Management: Using multiple LLM calls and external tools can lead to high operational costs.

Future Prospects

LangChain continues to evolve with enhancements in agent-based reasoning, improved memory systems, and better integrations with enterprise solutions. As AI models advance, LangChain is expected to play a pivotal role in the next generation of AI-powered applications.

Conclusion

LangChain stands as a powerful framework for developers and businesses looking to harness the capabilities of LLMs efficiently. With its modular approach, extensive integrations, and active community, LangChain is shaping the future of AI-driven applications.


"""
})

print(result)