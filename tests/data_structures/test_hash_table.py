from pygorithms.data_structures.hash_table import HashTable
import pytest


def test_put_new_key():
    ht = HashTable()

    ht.put('the_answer', 42)

    assert len(ht) == 1
    assert ht.get('the_answer') == 42


def test_put_existing_key():
    ht = HashTable()
    ht.put('the_answer', 42)

    ht.put('the_answer', 7)

    assert len(ht) == 1
    assert ht.get('the_answer') == 7


def test_put_collisions():
    ht = HashTable(resizing=False)

    for i in range(50):
        ht.put(i, i)

    assert len(ht) == 50
    for i in range(50):
        assert ht.get(i) == i


def test_put_resize():
    ht = HashTable()

    for i in range(50):
        ht.put(i, i)

    assert ht._size > ht._initial_size
    assert len(ht) == 50
    for i in range(50):
        assert ht.get(i) == i


def test_get_existing_key():
    ht = HashTable()
    ht.put('the_answer', 42)

    res = ht.get('the_answer')

    assert res == 42


def test_get_nonexistent_key():
    ht = HashTable()
    ht.put('the_answer', 42)

    with pytest.raises(KeyError):
        ht.get('towel')


def test_delete_existing_key():
    ht = HashTable()
    ht.put('the_answer', 42)

    ht.delete('the_answer')

    assert len(ht) == 0


def test_delete_nonexistent_key():
    ht = HashTable()
    ht.put('the_answer', 42)

    with pytest.raises(KeyError):
        ht.delete('towel')


def test_delete_collisions():
    ht = HashTable(resizing=False)
    for i in range(50):
        ht.put(i, i)

    for i in range(50):
        ht.delete(i)

    assert len(ht) == 0
