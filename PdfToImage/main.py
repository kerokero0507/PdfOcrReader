from pdf2image import convert_from_path

path = "./TestFile/test.pdf"
images = convert_from_path(path)

imageDir = "./TestFile"
images[0].save('test{}.jpeg'.format(0), 'JPEG')

