import pyscreenshot as image_grab
import datetime
from filesistem import get_image_save_path


def take_screen():
    im = image_grab.grab()
    now = datetime.datetime.now().strftime("%m-%d-%Y-%H.%M.%S")

    path = get_image_save_path()
    full_path = path + now + '.png'
    filename = now + '.png'

    im.save(full_path)

    return filename

    # im.grab_to_file()
    #
    # img = image_grab.grab()
    #
    # plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.show()
    # plt.imsave()
