import base64
from io import BytesIO
from pollinations import PILImage

def get_processed_image(img: PILImage):
    buffered = BytesIO()
    img.save(buffered, format="PNG")

    return base64.b64encode(buffered.getvalue()).decode("utf-8")