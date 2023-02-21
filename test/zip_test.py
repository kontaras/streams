'''
Created on Apr 5, 2017

@author: knaryshkin
'''

from streams import streams
import utils
import itertools


def test_basic():
    stream1 = streams.wrap(iter([0, 1, 2]))
    stream2 = ['0', '1', '2']
    result = [(0, '0'), (1, '1'), (2, '2')]
    utils.check_finite(result, stream1.zip(stream2))


def test_multi():
    stream1 = streams.wrap(iter([0, 1, 2]))
    stream2 = ['0', '1', '2']
    stream3 = ["x", "y", "z"]
    result = [(0, '0', "x"), (1, '1', "y"), (2, '2', "z")]
    utils.check_finite(result, stream1.zip(stream2, stream3))


def test_size_mismatch():
    stream1 = streams.wrap([0, 1, 2, 3, 4])
    stream2 = ['0', '1', '2']
    result = [(0, '0'), (1, '1'), (2, '2')]
    utils.check_finite(result, stream1.zip(stream2))

    stream1 = streams.wrap(iter([0, 1, 2]))
    utils.check_finite(result, stream1.zip(stream2 + [4]))


def test_infinite():
    def infinite():
        i = 0
        while True:
            yield i
            i += 1

    def infinite_str():
        i = 0
        while True:
            yield str(i)
            i += 1

    def infinite_tupple():
        i = 0
        while True:
            yield (i, str(i))
            i += 1

    stream = streams.wrap(infinite())
    utils.test_infinite(infinite_tupple(), stream.zip(infinite_str()))

    finite = [1, 2, 3]
    result = [(1, 1), (2, 2), (3, 3)]

    utils.check_finite(result, streams.wrap(itertools.count(1)).zip(finite))
    utils.check_finite(result, streams.wrap(finite).zip(itertools.count(1)))


def test_empty():
    stream = streams.wrap(iter([]))
    finite = streams.wrap([1, 2, 3])

    utils.test_empty(stream.zip(finite))
    utils.test_empty(finite.zip(stream))


def test_lazy():
    size = 4
    stream = streams.wrap(utils.lazy_bomb(size)).zip(utils.lazy_bomb(size))
    for i in range(size):
        next(stream)
