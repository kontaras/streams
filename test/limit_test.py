'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils


def test_basic():
    l = [1, 2, 3, 4, 5]
    stream = streams.wrap(iter(l))
    utils.checkFinite(l[:4], stream.limit(4))


def test_high_limit():
    l = [1, 2, 3, 4, 5]
    stream = streams.wrap(iter(l))
    utils.checkFinite(l, stream.limit(6))


def test_infinite():
    stream = streams.wrap(utils.infinte())

    utils.checkFinite(['a', 'a', 'a', 'a'], stream.limit(4))


def test_empty():
    stream = streams.wrap(iter([]))

    utils.testEmpty(stream.limit(4))


def test_zero():
    l = [1, 2, 3, 4, 5]
    stream = streams.wrap(iter(l))

    utils.testEmpty(stream.limit(0))
