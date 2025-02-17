import pytest

from data_structures.linked_list import (
    SinglyLinkedList,
    DoublyLinkedList,
    CircularLinkedList,
    DoublyCircularLinkedList
)


class TestSinglyLinkedList:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Fixture to set up a new SinglyLinkedList before each test."""
        self.list = SinglyLinkedList()

    def test_empty_list(self) -> None:
        """Test that a new list is empty."""
        assert self.list.head is None
        assert str(self.list) == ""

    def test_append_single_item(self) -> None:
        """Test appending a single item to the list."""
        self.list.append(1)
        assert str(self.list) == "1"
        assert self.list.head is not None
        assert self.list.head.data == 1

    def test_append_multiple_items(self) -> None:
        """Test appending multiple items to the list."""
        items = [1, 2, 3, 4, 5]
        for item in items:
            self.list.append(item)
        assert str(self.list) == "1 -> 2 -> 3 -> 4 -> 5"

    def test_iteration(self) -> None:
        """Test iterating over the list."""
        items = [1, 2, 3]
        for item in items:
            self.list.append(item)
        assert list(self.list) == items


class TestDoublyLinkedList:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Fixture to set up a new DoublyLinkedList before each test."""
        self.list = DoublyLinkedList()

    def test_empty_list(self) -> None:
        """Test that a new list is empty."""
        assert self.list.head is None
        assert str(self.list) == ""

    def test_append_single_item(self) -> None:
        """Test appending a single item to the list."""
        self.list.append(1)
        assert str(self.list) == "1"
        assert self.list.head is not None
        assert self.list.head.data == 1
        assert self.list.head.prev is None

    def test_append_multiple_items(self) -> None:
        """Test appending multiple items to the list."""
        items = [1, 2, 3]
        for item in items:
            self.list.append(item)
        assert str(self.list) == "1 <-> 2 <-> 3"

        # Test prev links
        current = self.list.head
        prev = None
        while current:
            assert current.prev == prev
            prev = current
            current = current.next

    def test_iteration(self) -> None:
        """Test iterating over the list."""
        items = [1, 2, 3]
        for item in items:
            self.list.append(item)
        assert list(self.list) == items


class TestCircularLinkedList:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Fixture to set up a new CircularLinkedList before each test."""
        self.list = CircularLinkedList()

    def test_empty_list(self) -> None:
        """Test that a new list is empty."""
        assert self.list.head is None
        assert str(self.list) == ""

    def test_append_single_item(self) -> None:
        """Test appending a single item to the list."""
        self.list.append(1)
        assert str(self.list) == "1"
        assert self.list.head is not None
        assert self.list.head.data == 1
        assert self.list.head.next == self.list.head

    def test_append_multiple_items(self) -> None:
        """Test appending multiple items to the list."""
        items = [1, 2, 3]
        for item in items:
            self.list.append(item)
        assert str(self.list) == "1 -> 2 -> 3 -> (head)"

        # Verify circular nature
        current = self.list.head
        for _ in range(len(items)):
            assert current is not None
            current = current.next
        assert current == self.list.head

    def test_iteration(self) -> None:
        """Test iterating over the list."""
        items = [1, 2, 3]
        for item in items:
            self.list.append(item)
        assert list(self.list) == items


class TestDoublyCircularLinkedList:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Fixture to set up a new DoublyCircularLinkedList before each test."""
        self.list = DoublyCircularLinkedList()

    def test_empty_list(self) -> None:
        """Test that a new list is empty."""
        assert self.list.head is None
        assert str(self.list) == ""

    def test_append_single_item(self) -> None:
        """Test appending a single item to the list."""
        self.list.append(1)
        assert str(self.list) == "1"
        assert self.list.head is not None
        assert self.list.head.data == 1
        assert self.list.head.next == self.list.head
        assert self.list.head.prev == self.list.head

    def test_append_multiple_items(self) -> None:
        """Test appending multiple items to the list."""
        items = [1, 2, 3]
        for item in items:
            self.list.append(item)
        assert str(self.list) == "1 <-> 2 <-> 3 <-> (head)"

        # Verify circular nature and prev links
        current = self.list.head
        prev = None
        for _ in range(len(items)):
            assert current is not None
            if prev:
                assert current.prev == prev
            prev = current
            current = current.next
        assert current == self.list.head
        assert self.list.head is not None
        assert self.list.head.prev == prev

    def test_iteration(self) -> None:
        """Test iterating over the list."""
        items = [1, 2, 3]
        for item in items:
            self.list.append(item)
        assert list(self.list) == items
