def selection_sort(items):
    """O(n^2)."""
    for i in range(len(items) - 1):
        min_ind = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_ind]:
                min_ind = j

        items[i], items[min_ind] = items[min_ind], items[i]
