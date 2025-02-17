import pytest

from algorithms.dynamic_programming.knapsack import knapsack


def test_knapsack():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    assert knapsack(W, wt, val, n) == 220