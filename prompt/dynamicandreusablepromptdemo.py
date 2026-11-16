from langchain_core.prompts import PromptTemplate
prompt_template = PromptTemplate.from_template('What is the capital of {country}?')
print(prompt_template.format(country='India'))