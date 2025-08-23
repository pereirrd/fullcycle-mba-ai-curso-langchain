from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

gemini_model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
answer = gemini_model.invoke("Hello, world!")
print(answer.content)