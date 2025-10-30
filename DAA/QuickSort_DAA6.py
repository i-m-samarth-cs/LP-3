import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, r=False):
    if low < high:
        if r:
            p = random.randint(low, high)
            arr[p], arr[high] = arr[high], arr[p]
            
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1, r)
        quicksort(arr, p + 1, high, r)

if __name__ == "__main__":
    # Test array (must use copies to test both variants)
    test_data = [5, 3, 8, 1, 9, 4, 7]
    
    # Deterministic Sort (r=False)
    arr_d = test_data[:]
    quicksort(arr_d, 0, len(arr_d) - 1, False)
    print("Deterministic:", arr_d)

    # Randomized Sort (r=True)
    arr_r = test_data[:]
    quicksort(arr_r, 0, len(arr_r) - 1, True)
    print("Randomized:", arr_r)
