# func_py_image_to_text.py
import pytesseract
from PIL import Image

def func_py_image_to_text(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

print(func_py_image_to_text("text_image.png"))
