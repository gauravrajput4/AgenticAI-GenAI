import uvicorn
from anyio.itertools import chain
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key)

# 1. Create chat prompt template
system_template="Translate the following into {language}:"
prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system",system_template),
        ("user","{text}")
    ]
)

# 2. output Parser
parser=StrOutputParser()

#create chain
chain=prompt_template|model|parser

# App definition
app = FastAPI(title="LangChain Server",version="1.0",description="A simple API server using LangChian runnable interface")

# Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)