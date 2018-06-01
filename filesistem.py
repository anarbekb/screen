import os


def get_image_save_path():
    base_path = os.path.dirname(__file__)

    try:
        f = open(base_path + '/config/path_to_screen.txt', 'r')
        path = f.read()
        f.close()
    except OSError:
        f = open(base_path + '/config/path_to_screen.txt', 'w')
        path = input("Enter the path to screen folder: ")
        path = path + '/'
        f.write(path)
        f.close()

    return path
