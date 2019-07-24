from pygorithms.data_structures.stack.list_stack import ListStack


def test_push():
    stack = ListStack()

    stack.push(42)

    assert len(stack) == 1


def test_pop():
    stack = ListStack()
    stack.push(42)

    num = stack.pop()

    assert num == 42
    assert len(stack) == 0
