from pygorithms.algorithms.sorting.selection_sort import selection_sort


def test_selection_sort():
    items = [3, 56, 34, 565, 0, 45]

    selection_sort(items)

    for i in range(len(items) - 1):
        assert items[i] <= items[i + 1]
