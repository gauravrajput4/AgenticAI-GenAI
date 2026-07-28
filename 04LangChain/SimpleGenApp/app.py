import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#LangSmith Tracking
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING_V2"]=os.getenv("LANGSMITH_TRACING_V2")
os.environ["LANGSMITH_PROJECT_OS"]=os.getenv("LANGSMITH_PROJECT_OS")

# Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

# streamlit Framework
st.title("Langchain Demo with Gemma Model")
input_text=st.text_input("What question you have in mind")

# Ollama gemma2:2b model
llm = ChatOllama(
    model="gemma2:2b",
    temperature=0
)
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke(({"question":input_text})))


