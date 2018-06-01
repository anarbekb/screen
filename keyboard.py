from pynput import keyboard
from screen import take_screen
from filesistem import get_image_save_path
import yd
from auth import get_token, reset_token
import yadisk
import socket
from log import write_log


def on_release(key):
    if key == keyboard.Key.scroll_lock:
        print('Screen take')
        token = get_token()

        y = yadisk.YaDisk(token=token)

        if y.check_token() is False:
            token = reset_token()
            y = yadisk.YaDisk(token=token)

        filename = take_screen()
        try:
            yd.file_upload(y, get_image_save_path() + filename, yd.get_yd_dir() + filename)
        except socket.timeout:
            write_log('Timeout error')

    if key == keyboard.Key.pause:
        # Stop listener
        return False
