from io import StringIO
from threading import Thread, Lock

import pandas as pd
import requests

PREFIX_URL = 'https://raw.githubusercontent.com/data1030/data/master/split'

digits = pd.DataFrame()
targets = pd.Series()
lock = Lock()


def get_batch(batch_num):
    global digits
    global targets

    url = '{}/{}.csv'.format(PREFIX_URL, batch_num)
    r = requests.get(url)

    data_string = r.text

    data = pd.read_csv(StringIO(data_string), header=None)

    batch_digits = data.iloc[:, 1:]
    batch_targets = data.iloc[:, 0]

    with lock:
        digits = digits.append(batch_digits, ignore_index=True)
        targets = targets.append(batch_targets, ignore_index=True)


def load_data():
    threads = []
    for i in range(10):
        t = Thread(target=get_batch, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return digits.values, targets.values


if __name__ == '__main__':
    d, t = load_data()
    print(d.shape, t.shape)
