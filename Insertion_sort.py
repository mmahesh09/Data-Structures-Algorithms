def insertion_sort(arr):
    """
    Perform Insertion Sort on a list.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def get_user_input():
    """
    Get a list of numbers from user input.
    
    Returns:
    list: A list of integers entered by the user.
    """
    user_input = input("Enter numbers separated by spaces: ")
    # Convert the user input string into a list of integers
    num_list = [int(x) for x in user_input.split()]
    return num_list

def main():
    """
    Main function to handle the insertion sort process.
    """
    # Get user input
    numbers = get_user_input()
    
    # Check if the list is empty
    if not numbers:
        print("The list is empty. Please enter some numbers.")
        return
    
    # Sort the list using insertion sort
    sorted_list = insertion_sort(numbers)
    
    # Print the sorted list
    print("Sorted list:", sorted_list)

if __name__ == "__main__":
    main()
