from pygorithms.data_structures.stack.linked_list_stack import LinkedListStack


def test_push():
    stack = LinkedListStack()

    stack.push(42)

    assert len(stack) == 1


def test_pop():
    stack = LinkedListStack()
    stack.push(42)

    num = stack.pop()

    assert num == 42
    assert len(stack) == 0
