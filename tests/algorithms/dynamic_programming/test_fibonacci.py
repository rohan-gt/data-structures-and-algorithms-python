import pytest

from algorithms.dynamic_programming.fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(10) == 55
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1