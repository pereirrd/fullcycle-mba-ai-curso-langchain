from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import chain
from dotenv import load_dotenv

load_dotenv()

@chain
def square(input_dict:int) -> dict:
    x = input_dict["x"]
    return {"square_result" : x * x} 

question_template = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}."
)

model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

chain = square | question_template | model

result = chain.invoke({"x": 10})
print(result.content)