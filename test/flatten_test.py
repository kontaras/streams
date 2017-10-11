'''
Created on Dec 5, 2016

@author: knaryshkin
'''

from streams import streams
import utils

def test_basic():
    l = [[1,2],[3]]
    stream = streams.wrap(iter(l))
    
    utils.checkFinite([1,2,3], stream.flatten())

def test_infinite():
    stream = streams.wrap(utils.infinte(['a']))
    utils.testInfinite(utils.infinte(), stream.flatten())
    
    stream = streams.wrap([utils.infinte(), utils.infinte()])
    utils.testInfinite(utils.infinte(), stream.flatten())

def test_empty():
    stream = streams.wrap(iter([]))
    
    utils.testEmpty(stream.flatten())