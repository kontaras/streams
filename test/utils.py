from streams import streams


def check_finite(expected, stream):
    test_wrapped(stream)

    for i in expected:
        j = next(stream)
        assert i == j, "Stream did not return an expected value."

    test_empty(stream)


def test_infinite(expected, stream):
    test_wrapped(stream)

    for _ in range(1000):
        assert next(stream) == next(expected),\
            "Infinite stream did not return an expected value"


def test_empty(stream):
    test_wrapped(stream)

    try:
        next(stream)
        assert False, "Expected stream to throw StopIteration. It did not."
    except StopIteration:
        pass  # Expected error


def test_wrapped(stream):
    assert isinstance(stream, streams.Stream)


def infinite(value='a'):
    while True:
        yield value


def lazy_bomb(limit, item=None):
    i = 0
    while i < limit:
        i += 1
        yield item
    raise Exception("Function is not lazy")
