def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Get the input array from the user
input_array = list(map(int, input("Enter the integer array containing duplicates (separated by space): ").split()))

# Sort the inputted array
sorted_array = sorted(input_array)

# Get the element to search from the user
element = int(input("Enter the element to search in the sorted array: "))

# Perform binary search
index = binary_search(sorted_array, element)

if index == -1:
    print("Error: Element not found")
else:
    # Count the number of occurrences of the element
    count = sorted_array.count(element)
    print("Sorted array:", sorted_array)
    print(f"Number of occurrences of element {element} is: {count}")
