from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

template = PromptTemplate(
    template="Write a summary for the following text - \n {text}",
    input_variables=["text"]
)
 
loader = TextLoader('kafka.txt')
docs = loader.load()

chain = template | model | parser
result = chain.invoke({'text': docs[0].page_content})
print(result)