from Helpers.workflow import get_compiled_graph
import json

graph = get_compiled_graph()

result = graph.invoke({
        "script": "Ever spent hours studying and still remembered nothing the next day? So today, I’m giving you five study tips that actually work, backed by science. First, use the 25–5 rule: study for 25 minutes with zero distractions, then rest for 5 minutes — it keeps your brain fresh. Next, teach what you learned to someone else; if you can explain it simply, you truly understand it, and even talking to a wall works. Use active recall by closing your book and trying to remember the key ideas instead of rereading everything. Keep your study sessions short and consistent because short bursts help you absorb more than long, exhausting sessions. And finally, keep your notes simple with keywords, bullet points, and quick diagrams — simple notes make revision faster. In the end, studying smart always beats studying hard, so keep learning and stay consistent.",
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