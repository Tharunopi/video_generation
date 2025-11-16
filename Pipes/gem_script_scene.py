import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from langchain.agents import create_agent
from Models.gemini import models
from Engines.system_prompt_reader import promptReaderEngine
from Data_class.scenes import sceneCollection
from Data_class.context import sceneContext
from Memory.sql_lite_saver import longShortMemory
from langgraph.graph.state import CompiledStateGraph
from typing import Tuple

class agent_script_to_scene:
    @staticmethod
    def agent() -> Tuple[CompiledStateGraph, dict]|None:
        try:
            configs = {
            "configurable":{
                "thread_id": "tharun_1", 
                "user_id": "tharun"
            }}
            
            scene_generation_agent = create_agent(
                model=models.llm(),
                tools=[],
                system_prompt=promptReaderEngine.read("script_scene"),
                response_format=sceneCollection,
                context_schema=sceneContext
                # checkpointer=longShortMemory.get_memory("Databases/script_scene_checkpoint.db"),
                # store=longShortMemory.get_memory("Databases/script_scene_store.db")
            )
            return (scene_generation_agent, configs)
        
        except Exception as e:
            print(f"{__name__} -> {e}")
            return None

        