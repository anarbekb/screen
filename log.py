import os
import datetime

log_name = 'log.txt'


def write_log(message):
    log_path = base_path = os.path.dirname(__file__) + '/logs/' + log_name
    curren_date = datetime.datetime.now().strftime("%m-%d-%Y-%H.%M.%S")

    try:
        f = open(log_path, 'a')
        f.write(
            curren_date + ' ' +
            message + '\n'
        )
        f.close()
    except OSError:
        f = open(log_path, 'w')
        f.write(
            curren_date + ' ' +
            message + '\n'
        )
        f.close()