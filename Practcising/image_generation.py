from PIL import Image
import io, base64, requests
from dotenv import load_dotenv

load_dotenv()
url = "https://c4e78eb212a2.ngrok-free.app"

def generate_kaggle():
    response = requests.post(
        url=f"{url}/generate",
        json={"prompt": "A hyper-realistic, close-up portrait of a tribal elder from the Omo Valley, painted with intricate white chalk patterns and adorned with a headdress made of dried flowers, seed pods, and rusted bottle caps. The focus is razor-sharp on the texture of the skin, showing every pore, wrinkle, and scar that tells a story of survival. The background is a blurred, smoky hut interior, with the warm glow of a cooking fire reflecting in the subject's dark, soulful eyes. Shot on a Leica M6 with Kodak Portra 400 film grain aesthetic."},
        timeout=60*10,
        stream=True)
    
    if response.status_code == 200:
        recieved = response.json()
        print(f"Format: {recieved['format']}, Size: {recieved['size']}")
        data = recieved["img_str"]
        img_data = base64.b64decode(data)
        img = Image.open(io.BytesIO(img_data))
        img.show()
    
    else:
        print("Error")

generate_kaggle()