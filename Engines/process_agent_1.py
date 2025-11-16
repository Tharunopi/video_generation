import json

class agent_1:
    def __init__(self, response):
        self.response = response

    def extract_scenes_data(self):
        try:
            scenes_data = self.response["structured_response"]
            return scenes_data

        except Exception as e:
            print(f"{__name__} -> {e}")

    def construct_jsons(self, scenes_data):
        try:
            scens_metadata_dict = {
                "total_scens": len(scenes_data.scenes),
                "total_duration": f"{sum(i.duration_seconds for i in scenes_data.scenes) / 60} minutes"
            }

            actual_scenes = {
                "scenes": [
                    {"scene_id": scene.scene_id,
                        "title": scene.title,
                        "summary": scene.summary,
                        "visual_description": scene.visual_description,
                        "emotion": scene.emotion,
                        "camera_direction": scene.camera_direction,
                        "dialogue": scene.dialogue,
                        "duration_seconds": scene.duration_seconds} for scene in scenes_data.scenes]
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
            self.saver(metadata, r"Output/script_to_scenes/metadata_json")
            self.saver(scenes, r"Output/script_to_scenes/scenes_json")
            return True


        except Exception as e:
            print(f"{__name__} -> {e}")
            return False