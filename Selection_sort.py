def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# User input
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_arr = selection_sort(arr)
print("Selection Sorted array:", sorted_arr)
