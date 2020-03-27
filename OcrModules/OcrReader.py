from PIL import Image
import pytesseract

FILENAME = './testimage2.jpg'

print(pytesseract.image_to_string(Image.open(FILENAME)))
