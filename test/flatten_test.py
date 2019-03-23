'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils


def test_basic():
    sample_list = [[1, 2], [3, 4]]
    stream = streams.wrap(iter(sample_list))

    utils.checkFinite([1, 2, 3, 4], stream.flatten())


def test_recursive():
    sample_list = [streams.wrap([1, 2]), streams.wrap([3])]
    stream = streams.wrap(iter(sample_list))

    utils.checkFinite([1, 2, 3], stream.flatten())


def test_infinite():
    stream = streams.wrap(utils.infinte(['a']))
    utils.testInfinite(utils.infinte(), stream.flatten())

    stream = streams.wrap([utils.infinte(), utils.infinte()])
    utils.testInfinite(utils.infinte(), stream.flatten())


def test_empty():
    stream = streams.wrap(iter([]))

    utils.testEmpty(stream.flatten())


def test_lazy():
    size = 4
    stream = streams.wrap(utils.lazy_bomb(size/2, [1, 2])).flatten()
    for i in range(size):
        next(stream)
