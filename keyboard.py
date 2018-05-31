from pynput import keyboard
from screen import take_screen


def on_release(key):
    if key == keyboard.Key.scroll_lock:
        take_screen()

    if key == keyboard.Key.pause:
        # Stop listener
        return False