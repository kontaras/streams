'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils


def test_basic():
    sample_list = [1, 2, 3, 4, 5]
    stream = streams.wrap(iter(sample_list))
    utils.checkFinite(sample_list[:4], stream.limit(4))


def test_high_limit():
    sample_list = [1, 2, 3, 4, 5]
    stream = streams.wrap(iter(sample_list))
    utils.checkFinite(sample_list, stream.limit(6))


def test_infinite():
    stream = streams.wrap(utils.infinte())

    utils.checkFinite(['a', 'a', 'a', 'a'], stream.limit(4))


def test_empty():
    stream = streams.wrap(iter([]))

    utils.testEmpty(stream.limit(4))


def test_zero():
    sample_list = [1, 2, 3, 4, 5]
    stream = streams.wrap(iter(sample_list))

    utils.testEmpty(stream.limit(0))


def test_lazy():
    size = 4
    stream = streams.wrap(utils.lazy_bomb(size)).limit(5)
    for i in range(size):
        next(stream)
