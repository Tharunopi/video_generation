from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from Utils.models import Models
from Utils.output_structure import *

class Agents:
    def __init__(self):
        self.__scene_agent = create_agent(model=Models.scene_creator(), response_format=listScenes)
        self.__eval_scene_agent = create_agent(model=Models.eval_scene(), response_format=evalReportScenes)
        self.__image_prompt_agent = create_agent(model=Models.image_prompt_creator(), response_format=imagePromptList)
        self.__eval_image_prompt_agent = create_agent(model=Models.eval_image_prompt(), response_format=evalReportImagePrompt)

    def get_scene_agent(self) -> CompiledStateGraph:
        return self.__scene_agent
    
    def get_eval_scene_agent(self) -> CompiledStateGraph:
        return self.__eval_scene_agent
    
    def get_image_prompt_agent(self) -> CompiledStateGraph:
        return self.__image_prompt_agent
    
    def get_eval_image_prompt_agent(self) -> CompiledStateGraph:
        return self.__eval_image_prompt_agent