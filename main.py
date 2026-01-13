from Helpers.workflow import get_compiled_graph
import json
from Utils.video_content.script import Script

graph = get_compiled_graph()

result = graph.invoke({
        "script": Script.get_script(),
        "scenes": [],
        "eval_result_scenes": None,
        "is_approved_scenes": None,
        "revision_count_scenes": 0,
        "image_prompt": [],
        "eval_result_image_prompt": None,
        "is_approved_image_prompt": None,
        "revision_count_image_prompt": 0,
        "images": [],
        "image_generation_count": 0,
        "eval_image": [],
        "images_to_eval": []
    })

with open(r"C:\Stack overflow\video_generation\Data\output.json", "w") as f:
    json.dump(result, f, indent=2)