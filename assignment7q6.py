def remove_duplicates(arr):
    return list(set(arr))

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Get the input array from the user
input_array = list(map(int, input("Enter the list of integer numbers (separated by space): ").split()))

# Remove duplicates from the input array
unique_array = remove_duplicates(input_array)

# Sort the array using selection sort
selection_sorted = selection_sort(unique_array)

# Sort the array using bubble sort
bubble_sorted = bubble_sort(unique_array)

print("Input array:", input_array)
print("Unique array:", unique_array)
print("Selection sorted array:", selection_sorted)
print("Bubble sorted array:", bubble_sorted)
def remove_duplicates(arr):
    return list(set(arr))

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Get the input array from the user
input_array = list(map(int, input("Enter the list of integer numbers (separated by space): ").split()))

# Remove duplicates from the input array
unique_array = remove_duplicates(input_array)

# Sort the array using selection sort
selection_sorted = selection_sort(unique_array)

# Sort the array using bubble sort
bubble_sorted = bubble_sort(unique_array)

print("Input array:", input_array)
print("Unique array:", unique_array)
print("Selection sorted array:", selection_sorted)
print("Bubble sorted array:", bubble_sorted)