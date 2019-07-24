# Find the sum of a given array.


def recursive_sum(items):
    """O(n)."""
    if len(items) == 1:
        return items[0]

    return items[0] + recursive_sum(items[1:])
