import os
import datetime

log_name = 'log.txt'


def write_log(message):
    log_path = base_path = os.path.dirname(__file__) + '/' + log_name
    curren_date = datetime.datetime.now().strftime("%m-%d-%Y-%H.%M.%S")

    try:
        f = open(log_path, 'a')
        f.writelines(
            curren_date +
            message
        )
        f.close()
    except FileNotFoundError:
        f = open(log_path, 'w')
        f.writelines(
            curren_date +
            message
        )
        f.close()