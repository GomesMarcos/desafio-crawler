import base64

from utils.main import SCREENSHOT_B64_FILENAME, SCREENSHOT_FILENAME


def convert_from_base64_to_png():
    with open(SCREENSHOT_B64_FILENAME, "rb") as file:
        content = file.read()
        binary_image = base64.b64decode(content)
        _save_image_binary_to_png(binary_image)


def _save_image_binary_to_png(image: bytes):
    with open(SCREENSHOT_FILENAME, "wb") as file:
        file.write(image)


convert_from_base64_to_png()
