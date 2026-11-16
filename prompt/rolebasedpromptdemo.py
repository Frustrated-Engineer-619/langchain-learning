from langchain_core.prompts import ChatPromptTemplate

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "What is the capital of {country}?")
])

chat_prompt = chat_prompt_template.format_messages(country='India')

print(chat_prompt)