from algorithms.sorting.insertion_sort import insertion_sort


def test_insertion_sort():
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    assert arr == [5, 6, 11, 12, 13]