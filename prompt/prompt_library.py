# Prepare prompt template
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a highly capable assistant trained to analyze and summarize documents.
Return ONLY valid JSON matching the exact schema below.

{format_instructions}

Analyze this document:
{document_text}
""")


# we can create any number of prompts and add them to a dictionary

#PromptTemplate:

#A template for building single-turn prompts using string formatting.

#Used for models that accept plain text input (like GPT-3 text-davinci-003, or other completion-based models).

#ChatPromptTemplate
#A specialized prompt builder for chat-based LLMs (like GPT-3.5-turbo, GPT-4).

#Supports multi-turn message formatting with roles like system, user, assistant.