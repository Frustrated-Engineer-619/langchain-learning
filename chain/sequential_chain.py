from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

template1 = PromptTemplate(template="Generate a detailed report on {topic}", input_variables=["topic"])
template2 = PromptTemplate(template="Generate a 5 pointer summary from the following text \n {text}", input_variables=["text"])

parser = StrOutputParser()


chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"Apache kafka"})
print(result)