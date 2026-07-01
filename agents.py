from langgraph.prebuilt import create_react_agent   # FIX: correct import (not langchain.agents.create_agent)
from langchain_mistralai import ChatMistralAI       # FIX: Mistral instead of OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv
import os

load_dotenv()

try:
    import streamlit as st
    mistral_key = st.secrets.get("MISTRAL_API_KEY") or os.getenv("MISTRAL_API_KEY")
except Exception:
    mistral_key = os.getenv("MISTRAL_API_KEY")

llm = ChatMistralAI(model="mistral-small-latest", temperature=0, api_key=mistral_key)


# Model setup — uses MISTRAL_API_KEY from .env
# llm = ChatMistralAI(model="mistral-small-latest", temperature=0)


# 1st agent — searches the web
def build_search_agent():
    return create_react_agent(
        model=llm,
        tools=[web_search]
    )


# 2nd agent — scrapes URLs
def build_reader_agent():
    return create_react_agent(
        model=llm,
        tools=[scrape_url]
    )


# Writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()


# Critic chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:
Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
