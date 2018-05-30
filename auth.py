import yadisk
import sys
import os


def auth():
    y = yadisk.YaDisk("7d9ca04e4fe848bbb1d1c6ba4916a5b4", "b7400bc636e144d988e749333afa388b")
    url = y.get_code_url()
    print("Go to the following url: %s" % url)
    code = input("Enter the confirmation code: ")

    try:
        response = y.get_token(code)
    except yadisk.exceptions.BadRequestError:
        print("Bad code")
        sys.exit(1)

    y.token = response.access_token

    if y.check_token():
        return y.token
    else:
        return False


def get_token():
    base_path = os.path.dirname(__file__)

    try:
        f = open(base_path + '/config/token.txt', 'r')
        token = f.read()
        f.close()
    except FileNotFoundError:
        f = open(base_path + '/config/token.txt', 'w')
        token = auth()
        f.write(token)
        f.close()

    return token


def reset_token():
    base_path = os.path.dirname(__file__)

    f = open(base_path + '/config/token.txt', 'w')
    token = auth()
    f.write(token)
    f.close()

    return token
