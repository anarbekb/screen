import os


def system_notify(header, text):
    command = 'notify-send \"{}\" \"{}\"' .format(header, text)
    os.system(command)
