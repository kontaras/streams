'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils
import itertools

def test_basic():
    l = [1,2,3]
    stream = streams.wrap(iter(l))
    
    utils.checkFinite([1,3], stream.filter(lambda x: x % 2 == 1))

def test_infinite():
    stream = streams.wrap(itertools.count())
    
    if streams._py_major == 2 and streams._py_minor < 7:
        def count(start, step):
            while True:
                yield start
                start += step
    else:
        count = itertools.count

    utils.testInfinite(count(1,2), stream.filter(lambda x: x % 2 == 1))

def test_empty():
    stream = streams.wrap(iter([]))
    
    utils.testEmpty(stream.filter(lambda x: x % 2 == 1))