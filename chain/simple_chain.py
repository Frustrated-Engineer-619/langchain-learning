from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
template = PromptTemplate(template="Generate 5 interesting facts about {topic}", input_variables=["topic"])
parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({"topic":"Apache kafka"})
print(result)


chain.get_graph().print_ascii()
    
