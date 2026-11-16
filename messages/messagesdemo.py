from langchain.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os       

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-5.5")

system_message = SystemMessage(content="You are a helpful assistant.")
human_message = HumanMessage(content="What is the capital of India?")

messages = [system_message, human_message]

response = llm.invoke(messages)

print(response.content)
