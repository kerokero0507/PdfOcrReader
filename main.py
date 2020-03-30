import OcrModules.OcrReader as Reader
import PdfToImage.ImageConverter as Converter
import csv

FILENAME = 'TestData/TestReport.pdf'
CONFIGNAME = 'TestData/OcrMapping_TestReport.csv'

config_file = open(CONFIGNAME)
config = csv.reader(config_file)

header = list(range(config.line_num - 1))
result_list = list(range(config.line_num - 1))

next(config)
for row in config:
    cut_image = Converter.cutting_out(FILENAME, row[1], row[2], row[3], row[4])
    # cut_image.show()
    result_list.append(Reader.read(cut_image))
    header.append(row[0])

print(result_list)

output = [header, result_list]

print(output)

outFile = open('TestReport.csv', 'w')
writer = csv.writer(outFile)
writer.writerows(output)
