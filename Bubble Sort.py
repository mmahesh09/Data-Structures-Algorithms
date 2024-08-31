def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.
    
    Parameters:
    arr (list): The list of numbers to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Track whether any swaps were made during this pass
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made, the list is sorted
        if not swapped:
            break
    return arr

def main():
    # Prompt the user for input
    input_list = input("Enter numbers separated by spaces: ").strip()
    
    # Check if the input is empty
    if not input_list:
        print("The list is empty. Please enter some numbers.")
        return
    
    # Convert the input string to a list of numbers
    try:
        num_list = list(map(int, input_list.split()))
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        return
    
    # Sort the list using Bubble Sort
    sorted_list = bubble_sort(num_list)
    
    # Print the sorted list
    print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()
