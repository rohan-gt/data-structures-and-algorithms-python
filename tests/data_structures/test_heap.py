import pytest

from data_structures.heap import Heap


def min_compare(x: int, y: int) -> bool:
    """Comparison function for min-heap."""
    return x < y


def max_compare(x: int, y: int) -> bool:
    """Comparison function for max-heap."""
    return x > y


@pytest.fixture
def min_heap() -> Heap:
    """Fixture to create a min-heap."""
    return Heap(min_compare)


@pytest.fixture
def max_heap() -> Heap:
    """Fixture to create a max-heap."""
    return Heap(max_compare)


def test_heappush_min_heap(min_heap: Heap) -> None:
    """Test heappush operation for min-heap."""
    min_heap.heappush(3)
    min_heap.heappush(1)
    min_heap.heappush(2)
    assert min_heap.heap == [1, 3, 2]


def test_heappop_min_heap(min_heap: Heap) -> None:
    """Test heappop operation for min-heap."""
    min_heap.heappush(3)
    min_heap.heappush(1)
    min_heap.heappush(2)
    assert min_heap.heappop() == 1
    assert min_heap.heappop() == 2
    assert min_heap.heappop() == 3
    assert min_heap.heappop() is None


def test_heappush_max_heap(max_heap: Heap) -> None:
    """Test heappush operation for max-heap."""
    max_heap.heappush(3)
    max_heap.heappush(1)
    max_heap.heappush(2)
    assert max_heap.heap == [3, 1, 2]


def test_heappop_max_heap(max_heap: Heap) -> None:
    """Test heappop operation for max-heap."""
    max_heap.heappush(3)
    max_heap.heappush(1)
    max_heap.heappush(2)
    assert max_heap.heappop() == 3
    assert max_heap.heappop() == 2
    assert max_heap.heappop() == 1
    assert max_heap.heappop() is None


def test_heappushpop_min_heap(min_heap: Heap) -> None:
    """Test heappushpop operation for min-heap."""
    min_heap.heappush(3)
    min_heap.heappush(1)
    min_heap.heappush(2)
    assert min_heap.heappushpop(0) == 0
    assert min_heap.heappushpop(4) == 1
    assert min_heap.heap == [2, 3, 4]


def test_heapreplace_min_heap(min_heap: Heap) -> None:
    """Test heapreplace operation for min-heap."""
    min_heap.heappush(3)
    min_heap.heappush(1)
    min_heap.heappush(2)
    assert min_heap.heapreplace(0) == 1
    assert min_heap.heapreplace(4) == 0
    assert min_heap.heap == [2, 3, 4]


def test_heapify_min_heap(min_heap: Heap) -> None:
    """Test heapify operation for min-heap."""
    min_heap.heapify([3, 1, 2])
    assert min_heap.heap == [1, 3, 2]


def test_nsmallest_min_heap(min_heap: Heap) -> None:
    """Test nsmallest operation for min-heap."""
    min_heap.heapify([3, 1, 2, 4, 5])
    assert min_heap.nsmallest(3) == [1, 2, 3]


def test_nlargest_min_heap(min_heap: Heap) -> None:
    """Test nlargest operation for min-heap."""
    min_heap.heapify([3, 1, 2, 4, 5])
    assert min_heap.nlargest(3) == [5, 4, 3]
