import pytest

from algorithms.dynamic_programming.lcs import lcs


def test_lcs():
    X = "AGGTAB"
    Y = "GXTXAYB"
    assert lcs(X, Y) == 4