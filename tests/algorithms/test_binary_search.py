from pygorithms.algorithms.binary_search import binary_search


def test_binary_search_first_element():
    items = [1, 2, 3, 4, 5, 6, 10, 55, 67, 2456]
    target = 1

    res = binary_search(items, target)

    assert res == 0


def test_binary_search_element_in_the_middle():
    items = [1, 2, 3, 4, 5, 6, 10, 55, 67, 2456]
    target = 55

    res = binary_search(items, target)

    assert res == 7


def test_binary_search_nonexistent_element():
    items = [1, 2, 3, 4, 5, 6, 10, 55, 67, 2456]
    target = 42

    res = binary_search(items, target)

    assert res is None
