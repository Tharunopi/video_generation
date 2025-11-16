from Pipes.gem_script_scene import agent_script_to_scene
from Pipes.gem_scene_whisk import agent_scene_whisk
from Engines.file_reader import fileReader
from Engines.process_agent_1 import agent_1
from Engines.process_agent_2 import agent_2
from Engines.output_reader import outputReader
import time

agent_1_, config = agent_script_to_scene.agent()
agent_2_, config = agent_scene_whisk.agent()
script = fileReader.read_script()
print(len(script))

response_1 = agent_1_.invoke(
    {
        "messages": [
            {"role": "user", "content": "only 2 character have dialogue uncle bobby and naratoor we are not going to show the narattor on screen only voice over. the video starts in mrng and ends in evening like a school. Ensure the character consistency and environment consistency and flow. Only 2 characters and no other characters. Also define the environment and character actions properly. Everything should be defined elaborately"}
        ],
        "context": {
            "script": script
        }
    },
    config=config
)

agent_1_response = agent_1(response_1)
agent_1_status = agent_1_response.final_step()

if agent_1_status:
    time.sleep(70)
    read_scenes = outputReader.read(r"Output\script_to_scenes\scenes_json")
    print(len(read_scenes))

    response_2 = agent_2_.invoke(
    {
        "messages": [
            {"role": "user", "content": "I have given scenes to you now generate whisk json prompt. Environe and character consistency and flow is very important. the character acitons should be defined properly and accurately."}
        ],
        "context": {
            "script": read_scenes
        }
    },
    config=None
    )
    print(response_2["response"][-1].content)

    # agent_2_response = agent_2(response_2)
    # agent_2_status = agent_2_response.final_step()