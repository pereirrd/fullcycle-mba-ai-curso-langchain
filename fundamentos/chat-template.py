from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

system = ("system", "You are an assistant that answers questions in a {style} style.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])
messages = chat_prompt.format_messages(
    style="funny",
    question="What is the capital of France?"
)

for message in messages:
    print(f"{message.type}: {message.content}")

gemini_model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
answer = gemini_model.invoke(messages)
print(answer.content)