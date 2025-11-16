from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

class models:
    @staticmethod
    def llm() -> ChatGoogleGenerativeAI|None:
        try:
            model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=os.getenv("google_gemini_apikey"))
            return model
        
        except Exception as e:
            print(f"{__name__} -> {e}")