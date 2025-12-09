from typing_extensions import TypedDict, List

class AgentState(TypedDict):
    script: str
    scenes: List[dict]
    image_prompt: list[dict]
    eval_result_scenes: str
    eval_result_image_prompt: str
    is_approved_scenes: bool
    is_approved_image_prompt: bool
    revision_count_scenes: int
    revision_count_image_prompt: int

    images: List
    images_to_eval: List
    images_to_regen: List
    image_generation_count: int
    eval_image: List
