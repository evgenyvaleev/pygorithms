def quicksort(items):
    """O(n * log n)."""
    if len(items) < 2:
        return items
    else:
        pivot_index = len(items) // 2
        pivot = items[pivot_index]
        left = [num for i, num in enumerate(items) if num <= pivot and i != pivot_index]
        right = [num for i, num in enumerate(items) if num > pivot and i != pivot_index]

        return quicksort(left) + [pivot] + quicksort(right)
