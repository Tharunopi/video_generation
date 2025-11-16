import json

class agent_2:
    def __init__(self, response):
        self.response = response["structured_response"]

    def extract_scenes_data(self):
        try:
            scenes_data = self.response
            return scenes_data

        except Exception as e:
            print(f"{__name__} -> {e}")

    def construct_jsons(self, scenes_data):
        try:
            scens_metadata_dict = {
                "total_scens": len(scenes_data.scenes)
            }

            actual_scenes = {
                "scenes": [
                    {"scene_id": scene.scene_id,
                        "prompt": scene.prompt,
                        "style": scene.style,
                        "lighting": scene.lighting,
                        "color_palette": scene.color_palette,
                        "composition": scene.composition,
                        "mood": scene.mood,
                        "quality": scene.quality,
                        "shot": scene.shot,
                        "no_text": scene.no_text} for scene in scenes_data.scenes]
            }
            return scens_metadata_dict, actual_scenes

        except Exception as e:
            print(f"{__name__} -> {e}")

    def saver(self, file, path:str) -> None:
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(file, f, indent=2, ensure_ascii=False)
                print(f"{path} -> Done")

        except Exception as e:
            print(f"{__name__} -> {e}")

    def final_step(self) -> bool:
        try:
            scenes_data = self.extract_scenes_data()
            metadata, scenes = self.construct_jsons(scenes_data)
            self.saver(metadata, r"Output/scenes_to_whisk/metadata_json")
            self.saver(scenes, r"Output/scenes_to_whisk/scenes_json")
            return True


        except Exception as e:
            print(f"{__name__} -> {e}")
            return False