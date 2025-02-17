from algorithms.sorting.selection_sort import selection_sort


def test_selection_sort():
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    assert arr == [11, 12, 22, 25, 64]
