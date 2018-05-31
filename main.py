from pynput import keyboard
from keyboard import on_release


if __name__ == '__main__':

    with keyboard.Listener(
            on_release=on_release) as listener:
        listener.join()


    # if (token):



