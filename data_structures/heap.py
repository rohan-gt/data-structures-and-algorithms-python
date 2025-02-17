from typing import Any, Callable, Optional


class Heap:
    """A generic heap class supporting both min-heap and max-heap operations.

    Attributes:
        heap: A list containing the heap elements.
        compare: A callable that defines the comparison strategy.
    """

    def __init__(self, compare: Callable[[Any, Any], bool]) -> None:
        """Initializes the heap with a comparison function.

        Args:
            compare: A function that takes two elements and returns True if the
                first element has higher priority than the second.
        """
        self.heap: list[Any] = []
        self.compare = compare

    def heappush(self, item: Any) -> None:
        """Pushes an item onto the heap.

        Args:
            item: The item to be pushed onto the heap.
        """
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def heappop(self) -> Optional[Any]:
        """Pops the root element from the heap.

        Returns:
            The root element if the heap is not empty; otherwise, None.
        """
        if not self.heap:
            return None
        root = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)
        return root

    def heappushpop(self, item: Any) -> Any:
        """Pushes an item onto the heap and then pops the root element.

        Args:
            item: The item to be pushed onto the heap.

        Returns:
            The root element after the push operation.
        """
        if self.heap and self.compare(self.heap[0], item):
            item, self.heap[0] = self.heap[0], item
            self._heapify_down(0)
        return item

    def heapreplace(self, item: Any) -> Any:
        """Pops the root element and then pushes an item onto the heap.

        Args:
            item: The item to be pushed onto the heap.

        Returns:
            The root element before the push operation.
        """
        root = self.heap[0]
        self.heap[0] = item
        self._heapify_down(0)
        return root

    def _heapify_up(self, index: int) -> None:
        """Maintains the heap property moving upwards from the given index.

        Args:
            index: The starting index to heapify up.
        """
        current = index
        while current > 0:
            parent_index = (current - 1) // 2
            if self.compare(self.heap[current], self.heap[parent_index]):
                self.heap[current], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[current],
                )
                current = parent_index
            else:
                break

    def _heapify_down(self, index: int) -> None:
        """Maintains the heap property moving downwards from the given index.

        Args:
            index: The starting index to heapify down.
        """
        current = index
        size = len(self.heap)
        while 2 * current + 1 < size:
            left_child_index = 2 * current + 1
            right_child_index = 2 * current + 2
            swap_candidate = left_child_index

            if (
                right_child_index < size
                and self.compare(self.heap[right_child_index], self.heap[left_child_index])
            ):
                swap_candidate = right_child_index

            if self.compare(self.heap[swap_candidate], self.heap[current]):
                self.heap[current], self.heap[swap_candidate] = (
                    self.heap[swap_candidate],
                    self.heap[current],
                )
                current = swap_candidate
            else:
                break

    def heapify(self, iterable: list[Any]) -> None:
        """Transforms a list into a heap, in-place, in linear time.

        Args:
            iterable: A list of elements to be transformed into a heap.
        """
        self.heap = iterable
        for i in reversed(range(len(self.heap) // 2)):
            self._heapify_down(i)

    def nsmallest(self, n: int) -> list[Any]:
        """Returns the n smallest elements from the heap.

        Args:
            n: The number of smallest elements to return.

        Returns:
            A list of the n smallest elements.
        """
        return sorted(self.heap)[:n]

    def nlargest(self, n: int) -> list[Any]:
        """Returns the n largest elements from the heap.

        Args:
            n: The number of largest elements to return.

        Returns:
            A list of the n largest elements.
        """
        return sorted(self.heap, reverse=True)[:n]

    def __len__(self) -> int:
        """Returns the number of elements in the heap.

        Returns:
            The number of elements in the heap.
        """
        return len(self.heap)

    def __str__(self) -> str:
        """Returns a string representation of the heap.

        Returns:
            A string representing the heap.
        """
        return str(self.heap)
