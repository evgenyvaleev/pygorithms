from pygorithms.algorithms.arrays.recursive_max import recursive_max


def test_recursive_max():
    items = [1, 2, 3, 42, 4, 5]

    res = recursive_max(items)

    assert res == 42
