'''
Created on Jul 12, 2017

@author: knaryshkin
'''

from streams import streams
import utils


def test_empty():
    stream = streams.wrap(iter([])).paginate(1)

    utils.testEmpty(stream)


def test_simple():
    stream = streams.wrap(iter([0, 1, 2])).paginate(2)
    layers = 0
    for l in stream:
        utils.testWrapped(l)
        values = 0
        for v in l:
            assert v == values + (2 * layers)
            values += 1
        assert values == 2 - layers
        layers += 1
    assert layers == 2

    utils.testEmpty(stream)


def test_exact_page():
    stream = streams.wrap(iter([0, 1, 2, 3])).paginate(2)
    layers = 0
    for l in stream:
        utils.testWrapped(l)
        values = 0
        for v in l:
            assert v == values + (2 * layers)
            values += 1
        assert values == 2
        layers += 1
    assert layers == 2

    utils.testEmpty(stream)


def test_lazy():
    size = 8
    pageSize = 4
    stream = streams.wrap(utils.lazy_bomb(size)).paginate(pageSize)
    for i in range(int(size/pageSize)):
        page = next(stream)
        for i in range(pageSize):
            next(page)
