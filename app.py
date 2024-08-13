import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

os.environ["GOOGLE_API_KEY"] = "AIzaSyDSjM13zy6Pv5Cm47Hk7va3XF7YJKYHBNA"

llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("Write a ballad about Gemini Pro in around 3 sentences.")
print(result.content)

