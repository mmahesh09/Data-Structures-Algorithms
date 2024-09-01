def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# User input
arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
target = int(input("Enter the target number: "))

# Perform search
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
