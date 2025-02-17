import pytest

from data_structures.array import Array


def test_array_operations() -> None:
    """
    Test basic operations of the Array class.
    """
    # Create an array of size 5 with default value 0
    arr = Array(5, default_value=0)
    assert len(arr) == 5
    assert arr[0] == 0
    assert arr[4] == 0

    # Set and get an element in the array
    arr[2] = 10
    assert arr[2] == 10

    # Test out-of-bounds access
    with pytest.raises(IndexError):
        arr[5] = 20

    with pytest.raises(IndexError):
        _ = arr[5]

    # Test the string representation of the array
    assert repr(arr) == "Array([0, 0, 10, 0, 0])"
