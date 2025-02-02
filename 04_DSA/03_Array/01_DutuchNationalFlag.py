def dutch_national_flag(arr):
    """
    Sorts an array of 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.

    Args:
        arr: The input array to be sorted.

    Returns:
        None. The input array is modified in-place.
    """

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Example usage
arr = [2, 0, 2, 1, 1, 0]
dutch_national_flag(arr)
print(arr)  # Output: [0, 0, 1, 1, 2, 2]