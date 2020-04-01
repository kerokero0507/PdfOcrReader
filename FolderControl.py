import os


def folders(targetpath, name_only=False):
    dir_list = []
    for folder, subfolders, files in os.walk(targetpath):
        for subfolder in subfolders:
            if not name_only:
                print(folder + '/' + subfolder)
                dir_list.append(folder + '/' + subfolder)
            else:
                dir_list.append(subfolder)

    return dir_list


def files(target_dir):
    file_list = []
    for folder, subfolders, files in os.walk(target_dir):
        for f in files:
            file_list.append(folder + '/' + f)

    return file_list


def sort_files(dir_path, ext):
    result = []
    for x in os.listdir(dir_path):
        root, ex = os.path.splitext(x)
        if ex == ext:
            result.append(dir_path + '/' + x)

    return result


def try_mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':
    PATH = 'TestData/MaterialReport'
    folder = folders(PATH)
    f = files(folder[0])
    print(f)
    print(sort_files(folder[0], '.csv')[0])
    try_mkdir(PATH + '/testdir')
