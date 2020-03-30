from PIL import Image
import pytesseract


def read(image):
    return pytesseract.image_to_string(image)


if __name__ == '__main__':
    FILENAME = './testimage2.jpg'
    print(pytesseract.image_to_string(Image.open(FILENAME)))
