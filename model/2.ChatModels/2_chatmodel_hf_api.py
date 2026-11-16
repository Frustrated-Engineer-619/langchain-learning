import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")

print(response.content)