from pygorithms.data_structures.queue.linked_list_queue import LinkedListQueue


def test_enqueue():
    q = LinkedListQueue()

    q.enqueue(42)

    assert len(q) == 1


def test_dequeue():
    q = LinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)

    res = q.dequeue()

    assert len(q) == 1
    assert res == 1


def test_dequeue_empty_queue():
    q = LinkedListQueue()

    res = q.dequeue()

    assert res is None
