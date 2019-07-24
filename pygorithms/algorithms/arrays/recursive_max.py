# Given an array of numbers, find the max number.


def recursive_max(items):
    """O(n)."""
    if len(items) == 1:
        return items[0]

    prev_max = recursive_max(items[1:])
    return prev_max if prev_max > items[0] else items[0]
