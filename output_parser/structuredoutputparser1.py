from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

response_schemas = [
    ResponseSchema(name="name", description="Name of the person"),
    ResponseSchema(name="age", description="Age of the person"),
    ResponseSchema(name="city", description="City where the person lives"),
    ResponseSchema(name="skills", description="List of technical skills")
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template = "Extract the person information from the following text : {text} \n {format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"text":"John is a 30 year old software engineer living in New York. He has expertise in Python, JavaScript, and cloud computing."})
print(result)