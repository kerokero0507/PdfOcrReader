from pdf2image import convert_from_path
from pdf2image import convert_from_bytes
from pikepdf import Pdf
from PIL import Image
import pdf2image.exceptions

def to_image(pdf_path):
    return convert_from_path(pdf_path)


def to_image_unlock(filepath, pw):
    data = Pdf.open(filepath, password=pw)
    newPdf = Pdf.new()
    newPdf.pages.extend(data.pages)
    newPdf.save(filepath)

    return to_image(filepath)


def cutting_out(image, left, upper, right, lower):
    return image.crop((int(left), int(upper), int(right), int(lower)))


if __name__ == '__main__':
    path = "TestFile/test.pdf"
    images = convert_from_path(path)

    imageDir = "./TestFile"
    images[0].save('test{}.jpeg'.format(0), 'JPEG')

    path = "TestFile/11 EJ-CL568-C921810-2019-4-3.pdf"
    # images = to_image_unlock(path, 'RICOHG')
    try:
        images = to_image(path)
        images[0].save('test{}.png'.format(0), 'PNG')
    except pdf2image.exceptions.PDFPageCountError as e:
        print(type(e))
        print(str(e))
        if 'Incorrect password' in str(e):
            print('パスワードエラーだよ')
        else:
            raise
