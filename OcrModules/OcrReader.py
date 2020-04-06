from PIL import Image
import pytesseract


def read(image):
    return pytesseract.image_to_string(image, config='--psm 6')


if __name__ == '__main__':
    FILENAME = './test_cutimage.png'
    print(pytesseract.image_to_string(Image.open(FILENAME),config='--psm 6'))
