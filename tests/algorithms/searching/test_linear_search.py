import pytest

from algorithms.searching.linear_search import linear_search


def test_linear_search():
    arr = [2, 3, 4, 10, 40]
    assert linear_search(arr, 10) == 3
    assert linear_search(arr, 5) == -1
