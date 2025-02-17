from data_structures.stack import Stack


def test_stack_operations() -> None:
    """
    Test basic operations of the Stack class.
    """
    stack = Stack()

    # Test stack is initially empty
    assert stack.is_empty() is True
    assert stack.size() == 0

    # Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Test stack is not empty and size is correct
    assert stack.is_empty() is False
    assert stack.size() == 3

    # Test peek operation
    assert stack.peek() == 3

    # Test pop operation
    assert stack.pop() == 3
    assert stack.size() == 2
    assert stack.peek() == 2

    # Clear the stack
    stack.clear()

    # Test stack is empty after clearing
    assert stack.is_empty() is True
    assert stack.size() == 0

    # Test pop and peek on empty stack
    assert stack.pop() is None
    assert stack.peek() is None
