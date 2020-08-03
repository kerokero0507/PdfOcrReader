import pdf2image

import OcrModules.OcrReader as Reader, FolderControl
import PdfToImage.ImageConverter as Converter
import csv
import json
import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver


def getext(filename):
    return os.path.splitext(filename)[-1].lower()


class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) == '.pdf':
            print('ファイルを検知しました(作成)：' + event.src_path)
            run(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) == '.pdf':
            print('ファイルを検知しました(更新)：' + event.src_path)
            run(event.src_path)


def run(filename):
    json_load = json.load(open('config.json', 'r'))
    input_path = json_load['DirectoryConfig']['input']
    output_path = json_load['DirectoryConfig']['output']
    password = json_load['DirectoryConfig']['PassWord']

    targets = FolderControl.folders(input_path)
    i = 0
    index = 0
    for f in targets:
        if f == os.path.dirname(filename):
            index = i
            break
        i = i + 1

    mapping = FolderControl.sort_files(targets[index], '.csv')[0]

    files = [filename]

    config_file = open(mapping)
    config = csv.reader(config_file)

    header = list(range(config.line_num - 1))
    result_list = list(range(config.line_num - 1))

    next(config)
    for row in config:
        try:
            image_page = Converter.to_image(files[0])[int(row[5])]
        except pdf2image.exceptions.PDFPageCountError:
            image_page = Converter.to_image_unlock(files[0], password)[int(row[5])]

        cut_image = Converter.cutting_out(image_page, row[1], row[2], row[3], row[4])
        # cut_image.show()
        result_list.append(Reader.read(cut_image))
        header.append(row[0])

    output = [header, result_list]

    targets = FolderControl.folders(input_path, True)
    for f in targets:
        FolderControl.try_mkdir(output_path + '/' + f)

    name = os.path.splitext(os.path.basename(files[0]))[0]

    out_file = open(output_path + '/' + targets[index] + '/' + name + '.csv', 'w')
    writer = csv.writer(out_file)
    writer.writerows(output)


if __name__ in '__main__':
    _json_load = json.load(open('config.json', 'r'))
    _input_path = _json_load['DirectoryConfig']['input']

    for target_dir in FolderControl.folders(_input_path):
        event_handler = ChangeHandler()
        observer = PollingObserver()
        observer.schedule(event_handler, target_dir, recursive=True)
        observer.start()
        print('監視を開始します:' + target_dir)

    while True:
        time.sleep(1)
