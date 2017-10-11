'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils

def test_basic():
    l = [1,2,3]
    stream = streams.wrap(iter(l))
    
    utils.checkFinite(l, stream)

def test_infinite():
    stream = streams.wrap(utils.infinte())
    
    utils.testInfinite(utils.infinte(), stream)

def test_empty():
    stream = streams.wrap(iter([]))
    
    utils.testEmpty(stream)