from data_structures.queue import Queue, PriorityQueue


def test_queue_operations() -> None:
    """
    Test basic operations of the Queue class.
    """
    queue = Queue()
    assert queue.is_empty() is True
    assert queue.size() == 0

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.is_empty() is False
    assert queue.size() == 3
    assert queue.peek() == 1

    assert queue.dequeue() == 1
    assert queue.size() == 2
    assert queue.peek() == 2

    queue.clear()
    assert queue.is_empty() is True
    assert queue.size() == 0
    assert queue.dequeue() is None
    assert queue.peek() is None


def test_priority_queue_operations() -> None:
    """
    Test basic operations of the PriorityQueue class.
    """
    pq = PriorityQueue()
    assert pq.is_empty() is True
    assert pq.size() == 0

    pq.enqueue('low', 1)
    pq.enqueue('medium', 2)
    pq.enqueue('high', 3)
    assert pq.is_empty() is False
    assert pq.size() == 3
    assert pq.peek() == 'high'

    assert pq.dequeue() == 'high'
    assert pq.size() == 2
    assert pq.peek() == 'medium'

    pq.clear()
    assert pq.is_empty() is True
    assert pq.size() == 0
    assert pq.dequeue() is None
    assert pq.peek() is None
