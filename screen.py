import pyscreenshot as image_grab
import matplotlib.pyplot as plt
import datetime
import os


def take_screen():
    im = image_grab.grab()
    now = datetime.datetime.now().strftime("%m-%d-%Y-%H.%M.%S")

    path = get_image_save_path()

    im.save(path + now + '.png')

    # im.grab_to_file()
    #
    # img = image_grab.grab()
    #
    # plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.show()
    # plt.imsave()


def get_image_save_path():
    base_path = os.path.dirname(__file__)

    try:
        f = open(base_path + '/config/path_to_scrteen.txt', 'r')
        path = f.read()
        f.close()
    except FileNotFoundError:
        f = open(base_path + '/config/path_to_scrteen.txt', 'w')
        path = input("Enter the path to screen folder: ")
        path = path + '/'
        f.write(path)
        f.close()

    return path