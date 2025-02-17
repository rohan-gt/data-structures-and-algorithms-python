from algorithms.sorting.merge_sort import merge_sort


def test_merge_sort():
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    assert arr == [5, 6, 7, 11, 12, 13]