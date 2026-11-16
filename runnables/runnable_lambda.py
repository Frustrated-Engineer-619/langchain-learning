from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
template1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

joke_gen_chain = RunnableSequence(template1, model, parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda inputs: len(inputs.split()))
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({"topic": "AI"})
print(result['joke'])
print(result['word_count'])


