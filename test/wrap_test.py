'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils


def test_basic():
    sample_list = [1, 2, 3]
    stream = streams.wrap(iter(sample_list))

    utils.check_finite(sample_list, stream)


def test_infinite():
    stream = streams.wrap(utils.infinite())

    utils.test_infinite(utils.infinite(), stream)


def test_empty():
    stream = streams.wrap(iter([]))

    utils.test_empty(stream)


def test_lazy():
    size = 4
    stream = streams.wrap(utils.lazy_bomb(size))
    for i in range(size):
        next(stream)
