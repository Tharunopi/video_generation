import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from langchain.agents import create_agent
from Models.gemini import models
from Engines.system_prompt_reader import promptReaderEngine
from Data_class.whisk_response_format import whiskPromptsCollection
from Data_class.whisk_context import whiskContext
from Memory.sql_lite_saver import longShortMemory
from langgraph.graph.state import CompiledStateGraph
from typing import Tuple

class agent_scene_whisk:
    @staticmethod
    def agent() -> Tuple[CompiledStateGraph, dict]|None:
        try:
            configs = {
            "configurable":{
                "thread_id": "tharun_1", 
                "user_id": "tharun"
            }}

            whisk_agent = create_agent(
                model=models.llm(),
                tools=None,
                system_prompt=promptReaderEngine.read("scene_whisk"),
                response_format=whiskPromptsCollection,
                context_schema=whiskContext
                # checkpointer=longShortMemory.get_memory("Databases/scene_whisk_checkpoint.db"),
                # store=longShortMemory.get_memory("Databases/scene_whisk_store.db")
            )

            return (whisk_agent, configs)

        except Exception as e:
            print(f"{__name__} -> {e}")
            return None