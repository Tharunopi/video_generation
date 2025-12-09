from PIL import Image
import io, base64, requests
from dotenv import load_dotenv

load_dotenv()
url = "https://9badd4dfc96d.ngrok-free.app"

def generate_image(prompt:str, negative_prompt:str, num_inference_steps:int=8, height:int=512, width:int=512, guidance_scale:float=0.0):
    response = requests.post(
        url=f"{url}/generate",
        json={
            "prompt": prompt,
            "num_inference_steps": num_inference_steps,
            "height": height,
            "width": width,
            "guidance_scale": guidance_scale,
            "negative_prompt": negative_prompt,
            },
        timeout=60*10,
        stream=True)
    
    if response.status_code == 200:
        recieved = response.json()
        print(f"Format: {recieved['format']}, Size: {recieved['size']}")
        data = recieved["img_str"]
        img_data = base64.b64decode(data)
        img = Image.open(io.BytesIO(img_data))
        return img
    
    else:
        return False
