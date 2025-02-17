from algorithms.sorting.quick_sort import quick_sort


def test_quick_sort():
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 5, 7, 8, 9, 10]
