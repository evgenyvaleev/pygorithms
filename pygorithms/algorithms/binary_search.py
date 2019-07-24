def binary_search(items, target):
    """O(log n)."""
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        elif items[mid] > target:
            high = mid - 1

    return None
