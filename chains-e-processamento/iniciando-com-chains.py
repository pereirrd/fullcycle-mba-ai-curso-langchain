from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

question_template = PromptTemplate(
    input_variables=["name"],
    template="Hello, {name}! How can I assist you today?"
)

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

chain = question_template | model

result = chain.invoke({"name": "Rodrigo"})
print(result.content)