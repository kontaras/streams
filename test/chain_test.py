from streams import streams
import utils


def test_basic():
    sample_list = [1, 2]
    stream = streams.wrap(iter(sample_list))
    utils.check_finite([1, 2, 3, 4], stream.chain([3, 4]))


def test_empty():
    stream = streams.wrap(iter([]))
    utils.test_empty(stream.chain([]))
    utils.check_finite([3, 4], stream.chain([3, 4]))