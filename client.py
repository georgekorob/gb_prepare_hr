import gevent
import gevent.monkey

from urllib.request import urlopen

gevent.monkey.patch_all()

urls = ['http://yandex.ru', 'http://google.com', 'http://ria.ru']


def get_data(url):
    print(f'Getting {url}')
    data = urlopen(url).read()
    data_len = len(data)
    print(f'received: {data_len}')


jobs = [gevent.spawn(get_data, u) for u in urls]

gevent.wait(jobs)
