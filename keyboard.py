from pynput import keyboard
from screen import take_screen
from yd import file_upload
from auth import get_token, reset_token
import yadisk


def on_release(key):
    if key == keyboard.Key.scroll_lock:
        print('Screen take')
        token = get_token()

        y = yadisk.YaDisk(token=token)

        if y.check_token() is False:
            token = reset_token()
            y = yadisk.YaDisk(token=token)

        full_file_path = take_screen()
        file_upload(y, full_file_path, '/test')

    if key == keyboard.Key.pause:
        # Stop listener
        return False