import OcrModules.OcrReader as Reader
import PdfToImage.ImageConverter as Converter
import csv
import json
import FolderControl
import os

json_load = json.load(open('config.json', 'r'))
input_path = json_load['DirectoryConfig']['input']
output_path = json_load['DirectoryConfig']['output']

targets = FolderControl.folders(input_path)
mapping = FolderControl.sort_files(targets[0], '.csv')[0]

files = FolderControl.sort_files(targets[0], '.pdf')

config_file = open(mapping)
config = csv.reader(config_file)

header = list(range(config.line_num - 1))
result_list = list(range(config.line_num - 1))

next(config)
for row in config:
    cut_image = Converter.cutting_out(files[0], row[1], row[2], row[3], row[4])
    # cut_image.show()
    result_list.append(Reader.read(cut_image))
    header.append(row[0])

output = [header, result_list]

targets = FolderControl.folders(input_path, True)
for f in targets:
    FolderControl.try_mkdir(output_path + '/' + f)

name = os.path.splitext(os.path.basename(files[0]))[0]

outFile = open(output_path + '/' + targets[0] + '/' + name + '.csv', 'w')
writer = csv.writer(outFile)
writer.writerows(output)
