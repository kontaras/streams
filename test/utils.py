'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams


def checkFinite(expected, stream):
    testWrapped(stream)

    for i in expected:
        j = next(stream)
        assert i == j  # , "Stream did not return an expected value."

    testEmpty(stream)


def testInfinite(expected, stream):
    testWrapped(stream)

    for _ in range(1000):
        assert next(stream) == next(expected),\
            "Infinite stream did not return an expected value"


def testEmpty(stream):
    testWrapped(stream)

    try:
        foo = next(stream)
        print(foo)
        assert False, "Expected stream to throw StopIteration. It did not."
    except StopIteration:
        pass  # Expected error


def testWrapped(stream):
    assert isinstance(stream, streams.Stream)


def infinte(value='a'):
    while True:
        yield value
