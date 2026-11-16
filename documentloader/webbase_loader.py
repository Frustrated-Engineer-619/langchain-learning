from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-pro-proled-xdr-display-m5-pro-2026-m5-48-gb-1-tb-ssd-tahoe-mmf54hn-a/p/itm4e23ddd174e0a?pid=COMHSHBAFHFNMAXB&lid=LSTCOMHSHBAFHFNMAXBEHCFRZ&marketplace=FLIPKART&q=macbook+pro+air+m5&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=37466097-76cc-48e8-8c04-d04452fca4c5.COMHSHBAFHFNMAXB.SEARCH&ppt=None&ppn=None&ssid=5zwfyedxm80000001794812952084&qH=be917047b5806619&ov_redirect=true'
loader = WebBaseLoader(url)
docs = loader.load()

template = PromptTemplate(
    template='Answer the following question \n {question} from teh following text - \n {text}',
    input_variables=['question','text']
)

chain = template | model | parser

result = chain.invoke({'question':'what is the price of Apple MacBook Pro','text':docs[0].page_content})

print(result)