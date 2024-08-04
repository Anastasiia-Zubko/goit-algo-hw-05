def binary_search(arr, x):
    """
    Perform binary search on a sorted array to find the number of iterations
    and the upper bound.
    """
    low = 0
    high = len(arr) - 1
    num_iterations = 0
    upper_bound = None

    while low <= high:
        num_iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            upper_bound = arr[mid]
            while mid > 0 and arr[mid - 1] == x:
                mid -= 1
            upper_bound = arr[mid]
            return num_iterations, upper_bound

    if low < len(arr):
        upper_bound = arr[low]
    return num_iterations, upper_bound
