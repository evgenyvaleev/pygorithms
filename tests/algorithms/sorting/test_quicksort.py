from pygorithms.algorithms.sorting.quicksort import quicksort


def test_quicksort():
    items = [56, 45, 56456, 345, 33, 113, 545]

    items = quicksort(items)

    for i in range(len(items) - 1):
        assert items[i] <= items[i + 1]
