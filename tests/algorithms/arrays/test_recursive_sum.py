from pygorithms.algorithms.arrays.recursive_sum import recursive_sum


def test_recursive_sum():
    items = [1, 2, 3, 4, 5]

    res = recursive_sum(items)

    assert res == 15
