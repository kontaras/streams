from streams import streams
import utils


def test_basic():
    seen = []
    stream = streams.wrap(iter([1, 2, 3, 4])).peek(lambda x: seen.append(x))
    next(stream)
    next(stream)
    next(stream)

    assert seen == [1, 2, 3]
