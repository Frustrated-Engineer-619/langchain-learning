from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=["text"]
)

report_gen_chain = RunnableSequence(template1,model,parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>200,RunnableSequence(template2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)

result = final_chain.invoke({'topic':'AI'})
print(result)