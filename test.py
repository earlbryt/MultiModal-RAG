# This is a test with the Google Gemini API

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage


if 'GOOGLE_API_KEY' in os.environ:  # This is for testing purposes, delete any existing environment variables before running the script
    del os.environ['GOOGLE_API_KEY']

load_dotenv("env\.env")
api_key = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("Write a epic about Space Travel in around 3 sentences.")
print(result.content)

