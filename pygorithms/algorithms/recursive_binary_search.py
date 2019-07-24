def recursive_binary_search(items, target):
    """O(log n)."""
    mid = len(items) // 2

    if len(items) == 0:
        return None
    elif items[mid] == target:
        return mid
    elif items[mid] < target:
        res = recursive_binary_search(items[mid + 1:], target)
        return mid + res + 1 if res is not None else None
    else:
        return recursive_binary_search(items[:mid], target)
