from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  

load_dotenv()

model1 = ChatOpenAI(model="gpt-4o")
model2 = ChatOpenAI(model="gpt-5.5")

parser = StrOutputParser()

template1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}",
    input_variables=["topic"]
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(template1, model1, parser),
    'linkedin': RunnableSequence(template2, model2, parser)
})

result = parallel_chain.invoke({"topic": "AI in healthcare"})
print(result['tweet'])
print(result['linkedin'])
