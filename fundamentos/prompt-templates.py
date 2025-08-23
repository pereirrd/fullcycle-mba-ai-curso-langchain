from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hello, {name}! How can I assist you today?"
)

text = template.format(name="Alice")
print(text)