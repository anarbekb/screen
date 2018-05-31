import posixpath
import os
import yadisk


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