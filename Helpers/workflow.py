from Utils.graph import Graph

from Utils.nodes.scene_creator_node import scene_creater_agent
from Utils.nodes.eval_scene_node import eval_scene_agent
from Utils.nodes.regenerate_scene_node import regenerate_scene_agent
from Utils.nodes.should_loop_scenes_node import should_loop_scenes

from Utils.nodes.image_prompt_node import image_prompt_agent
from Utils.nodes.eval_image_prompt_node import eval_image_prompt_node
from Utils.nodes.regenerate_image_prompt_node import regenerate_image_agent
from Utils.nodes.should_loop_image_prompt import should_loop_image_prompt

from Utils.nodes.image_generation_node import image_generation_agent
from Utils.nodes.eval_image_node import eval_generated_image
from Utils.nodes.regenerate_image_node import image_regeneration_agent
from Utils.nodes.should_stop_image_generation import should_stop

from langgraph.graph import START, END

graph = Graph.get_graph()

def get_compiled_graph():
    graph.add_node("create_scene", scene_creater_agent)
    graph.add_node("eval_scene", eval_scene_agent)
    graph.add_node("regenerate_scene", regenerate_scene_agent)

    graph.add_node("create_image_prompt", image_prompt_agent)
    graph.add_node("eval_image_prompt", eval_image_prompt_node)
    graph.add_node("regenerate_image_prompt", regenerate_image_agent)

    graph.add_node("generate_image", image_generation_agent)
    graph.add_node("eval_image", eval_generated_image)
    graph.add_node("regenerate_image", image_regeneration_agent)

    graph.add_edge(START, "create_scene")
    graph.add_edge("create_scene", "eval_scene")
    graph.add_conditional_edges("eval_scene", should_loop_scenes, {"end": "create_image_prompt", "revise": "regenerate_scene"})
    graph.add_edge("regenerate_scene", "eval_scene")

    graph.add_edge("create_image_prompt", "eval_image_prompt")
    graph.add_conditional_edges("eval_image_prompt", should_loop_image_prompt, {"end": "generate_image", "revise": "regenerate_image_prompt"})
    graph.add_edge("regenerate_image_prompt", "eval_image_prompt")

    graph.add_edge("generate_image", "eval_image")
    graph.add_conditional_edges("eval_image", should_stop, {"end": END, "revise": "regenerate_image"})
    graph.add_edge("regenerate_image", "eval_image")

    workflow = graph.compile()

    return workflow