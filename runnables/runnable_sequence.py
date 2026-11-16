from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from regex import template

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
template1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template="Explain the following joke - {joke}",
    input_variables=["joke"]
)
    

chain = RunnableSequence(template1, model, parser, template2, model, parser)
result = chain.invoke({"topic": "programming"})
print(result)