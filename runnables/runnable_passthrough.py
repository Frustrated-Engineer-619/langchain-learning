from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

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
    

joke_gen_chain = RunnableSequence(template1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(template2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "programming"})
print(result['joke'])  
print("================================") 
print(result['explanation'])