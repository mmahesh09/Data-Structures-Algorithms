def merge_sort(arr):
    # Base case: if the list is empty or has one item, it's already sorted
    if len(arr) <= 1:
        return arr

    # Recursive case: divide the list into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0

    # Merge the two halves by comparing the elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right list
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    
    return sorted_list

def main():
    # Take user input for the list
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert the input string into a list of integers
    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Please enter valid integers.")
        return
    
    if not numbers:
        print("The list is empty.")
    else:
        print("Original list:", numbers)
        sorted_list = merge_sort(numbers)
        print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()
