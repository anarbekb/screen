import pyscreenshot as ImageGrab
import matplotlib.pyplot as plt
import datetime
import yadisk
from auth import get_token, reset_token
from yd import recursive_upload


if __name__ == '__main__':

    token = get_token()

    y = yadisk.YaDisk(token=token)

    if y.check_token() is False:
        token = reset_token()
        y = yadisk.YaDisk(token=token)

    to_dir = '/test'
    from_dir = '/home/anarvek/vpn'
    recursive_upload(y, from_dir, to_dir)

    # if (token):

    # im = ImageGrab.grab()
    # now = datetime.datetime.now().strftime("%m-%d-%Y-%H.%M.%S")
    #
    # im.save(now + '.png')
    #
    # im.grab_to_file(now + '.png')

    # img = ImageGrab.grab()
    #
    # plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.show()
    # plt.imsave()

