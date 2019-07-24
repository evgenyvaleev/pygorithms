from pygorithms.data_structures.linked_list import LinkedList
import pytest


def test_prepend_empty_list():
    lst = LinkedList()

    lst.prepend(42)

    assert lst.first.value == 42
    assert lst.last.value == 42
    assert len(lst) == 1


def test_prepend_non_empty_list():
    lst = LinkedList()
    lst.prepend(1)

    lst.prepend(2)

    assert lst.first.value == 2
    assert lst.last.value == 1
    assert lst.first.next_item == lst.last
    assert len(lst) == 2


def test_append_empty_list():
    lst = LinkedList()

    lst.append(42)

    assert lst.first.value == 42
    assert lst.last.value == 42
    assert len(lst) == 1


def test_append_non_empty_list():
    lst = LinkedList()
    lst.append(1)

    lst.append(2)

    assert lst.first.value == 1
    assert lst.last.value == 2
    assert lst.first.next_item == lst.last
    assert len(lst) == 2


def test_insert_in_the_middle():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    target = lst.find(2)

    lst.insert(target, 42)

    assert lst.first.next_item.value == 42
    assert lst.first.next_item.next_item == target
    assert len(lst) == 4


def test_insert_first():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    target = lst.first

    lst.insert(target, 42)

    assert lst.first.value == 42
    assert lst.first.next_item == target
    assert len(lst) == 3


def test_find():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)

    res = lst.find(2)

    assert res.value == 2


def test_find_last():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(2)
    first_el = lst.find(2)

    last_el = lst.find_last(2)

    assert last_el.value == 2
    assert last_el != first_el


def test_find_at():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)

    res = lst.find_at(1)

    assert res.value == 2


def test_find_at_wrong_index():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)

    with pytest.raises(KeyError):
        lst.find_at('towel')


def test_find_at_index_bigger_than_len():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)

    with pytest.raises(KeyError):
        lst.find_at(42)


def test_delete_first_empty_list():
    lst = LinkedList()

    with pytest.raises(ValueError):
        lst.delete(lst.first)


def test_delete_first_one_element_list():
    lst = LinkedList()
    lst.append(42)

    lst.delete(lst.first)

    assert lst.first is None
    assert lst.last is None
    assert len(lst) == 0


def test_delete_first_multiple_element_list():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)

    lst.delete(lst.first)

    assert lst.first.value == 2
    assert lst.first == lst.last
    assert len(lst) == 1


def test_delete_last_empty_list():
    lst = LinkedList()

    with pytest.raises(ValueError):
        lst.delete(lst.last)


def test_delete_last_one_element_list():
    lst = LinkedList()
    lst.append(42)

    lst.delete(lst.last)

    assert lst.first is None
    assert lst.last is None
    assert len(lst) == 0


def test_delete_last_multiple_element_list():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)

    lst.delete(lst.last)

    assert lst.last.value == 1
    assert lst.first == lst.last
    assert len(lst) == 1


def test_delete():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    target = lst.find(2)

    lst.delete(target)

    assert lst.first.next_item == lst.last
    assert len(lst) == 2


def test_clear():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)

    lst.clear()

    assert lst.first is None
    assert lst.last is None
    assert len(lst) == 0
