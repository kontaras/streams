from streams import streams
import utils


def test_empty():
    stream = streams.wrap(iter([])).paginate(1)

    utils.test_empty(stream)


def test_simple():
    stream = streams.wrap(iter([0, 1, 2])).paginate(2)
    layers = 0
    for layer in stream:
        utils.test_wrapped(layer)
        values = 0
        for value in layer:
            assert value == values + (2 * layers)
            values += 1
        assert values == 2 - layers
        layers += 1
    assert layers == 2

    utils.test_empty(stream)


def test_exact_page():
    stream = streams.wrap(iter([0, 1, 2, 3])).paginate(2)
    layers = 0
    for layer in stream:
        utils.test_wrapped(layer)
        values = 0
        for value in layer:
            assert value == values + (2 * layers)
            values += 1
        assert values == 2
        layers += 1
    assert layers == 2

    utils.test_empty(stream)


def test_lazy():
    size = 8
    page_size = 4
    stream = streams.wrap(utils.lazy_bomb(size)).paginate(page_size)
    for _ in range(int(size/page_size)):
        page = next(stream)
        for _ in range(page_size):
            next(page)
