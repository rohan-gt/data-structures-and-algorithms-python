def insertion_sort(arr: list[int]) -> None:
    """
    Sort an array of integers using the insertion sort algorithm.

    Args:
        arr: A list of integers to be sorted.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print("Sorted array is:", arr)