from pdf2image import convert_from_path
from PIL import Image


def to_jpeg(pdf_path):
    return convert_from_path(pdf_path)


def cutting_out(image_path, left, upper, right, lower):
    images = convert_from_path(image_path)
    return images[0].crop((int(left), int(upper), int(right), int(lower)))


if __name__ == '__main__':
    path = "./TestFile/test.pdf"
    images = convert_from_path(path)

    imageDir = "./TestFile"
    images[0].save('test{}.jpeg'.format(0), 'JPEG')

