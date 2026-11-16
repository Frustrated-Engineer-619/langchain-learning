from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o",max_tokens=30)  
response = model.invoke("What is Agentic AI?")
print(response.content)
