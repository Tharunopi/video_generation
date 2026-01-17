from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_nvidia_ai_endpoints import ChatNVIDIA
load_dotenv()

model_provider = "nvidia"
model_choice = "moonshotai/kimi-k2-thinking"

if model_provider == "nvidia":
    api_key = os.getenv("nvidia_apikey")

elif model_provider == "google":
    api_key = os.getenv("google_api_keys")

class Models:
    @staticmethod
    def scene_creator(model:str=model_choice, temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None | ChatNVIDIA:
        try:
            if model_provider == "nvidia":
                return ChatNVIDIA(model=model, api_key=api_key, temperature=temperature, **kwargs)
            elif model_provider == "nvidia":
                return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def eval_scene(model:str=model_choice, temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None | ChatNVIDIA:
        try:
            if model_provider == "nvidia":
                return ChatNVIDIA(model=model, api_key=api_key, temperature=temperature, **kwargs)
            elif model_provider == "nvidia":
                return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def image_prompt_creator(model:str=model_choice, temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None | ChatNVIDIA:
        try:
            if model_provider == "nvidia":
                return ChatNVIDIA(model=model, api_key=api_key, temperature=temperature, **kwargs)
            elif model_provider == "nvidia":
                return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def eval_image_prompt(model:str=model_choice, temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None | ChatNVIDIA:
        try:
            if model_provider == "nvidia":
                return ChatNVIDIA(model=model, api_key=api_key, temperature=temperature, **kwargs)
            elif model_provider == "nvidia":
                return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None
        
    @staticmethod
    def eval_image(model:str=model_choice, temperature:float=0.7, **kwargs) -> ChatGoogleGenerativeAI | None | ChatNVIDIA:
        try:
            if model_provider == "nvidia":
                return ChatNVIDIA(model=model, api_key=api_key, temperature=temperature, **kwargs)
            elif model_provider == "nvidia":
                return ChatGoogleGenerativeAI(model=model, api_key=api_key, temperature=temperature, **kwargs)

        except Exception as e:
            print(f"{__name__}: {e}")
            return None