import posixpath
import os
import yadisk
import log


def recursive_upload(y, from_dir, to_dir):
    for root, dirs, files in os.walk(from_dir):
        p = root.split(from_dir)[1].strip(os.path.sep)
        dir_path = posixpath.join(to_dir, p)

        try:
            y.mkdir(dir_path)
        except yadisk.exceptions.PathExistsError:
            pass

        for file in files:
            file_path = posixpath.join(dir_path, file)
            p_sys = p.replace("/", os.path.sep)
            in_path = os.path.join(from_dir, p_sys, file)
            try:
                y.upload(in_path, file_path)
            except yadisk.exceptions.PathExistsError:
                pass


def file_upload(y, file, to_dir):
    try:
        y.upload(file, to_dir)
    except yadisk.exceptions.PathExistsError:
        pass
    print('Screen uploaded')


def publish(y, path_file_yd):
    y.publish(path_file_yd)
    link = y.get_meta(path_file_yd)

    return link.public_url


def get_yd_dir():
    base_path = os.path.dirname(__file__)

    try:
        f = open(base_path + '/config/path_to_screen_yd.txt', 'r')
        path_yd = f.read()
        f.close()
    except OSError:
        log.write_log('File not found: /config/path_to_screen_yd.txt')

        f = open(base_path + '/config/path_to_screen_yd.txt', 'w')
        path_yd = input("Enter the path to screen in YandexDisk folder(simple: image/screen/): ")
        f.write(path_yd)
        f.close()

    return path_yd
