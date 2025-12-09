from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("google_api_key")

class Models:
    @staticmethod
    def scene_creator(model:str="gemini-2.5-flash", temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None:
        try:
            return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def eval_scene(model:str="gemini-2.5-flash", temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None:
        try:
            return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def image_prompt_creator(model:str="gemini-2.5-flash", temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None:
        try:
            return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def eval_image_prompt(model:str="gemini-2.5-flash", temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None:
        try:
            return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def eval_image(model:str="gemini-2.5-flash", temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None:
        try:
            return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None