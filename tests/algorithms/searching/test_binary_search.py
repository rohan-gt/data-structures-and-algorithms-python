import pytest

from algorithms.searching.binary_search import binary_search_iterative, binary_search_recursive


def test_binary_search_iterative():
    arr = [2, 3, 4, 10, 40]
    assert binary_search_iterative(arr, 10) == 3
    assert binary_search_iterative(arr, 5) == -1


def test_binary_search_recursive():
    arr = [2, 3, 4, 10, 40]
    assert binary_search_recursive(arr, 0, len(arr) - 1, 10) == 3
    assert binary_search_recursive(arr, 0, len(arr) - 1, 5) == -1
