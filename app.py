import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("Write a ballad about Gemini Pro in around 3 sentences.")
print(result.content)

