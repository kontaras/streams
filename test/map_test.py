'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils


def test_basic():
    stream = streams.wrap(iter([0, 1, 2]))
    utils.check_finite(['0', '1', '2'], stream.map(str))


def test_infinite():
    def infinte():
        i = 0
        while True:
            yield i
            i += 1

    def infinte_str():
        i = 0
        while True:
            yield str(i)
            i += 1

    stream = streams.wrap(infinte())
    utils.test_infinite(infinte_str(), stream.map(str))


def test_empty():
    stream = streams.wrap(iter([]))

    utils.test_empty(stream.map(str))


def test_lazy():
    size = 4
    stream = streams.wrap(utils.lazy_bomb(size)).map(lambda x: x)
    for i in range(size):
        next(stream)
