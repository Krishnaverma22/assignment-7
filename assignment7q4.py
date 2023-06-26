def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Get the number of students from the user
n = int(input("Enter the number of students: "))

# Initialize an empty list to store the marks
marks_list = []

# Get the marks for each student
for i in range(n):
    mark = int(input(f"Enter the marks for student {i+1}: "))
    marks_list.append(mark)

# Sort the list using merge sort
sorted_list = merge_sort(marks_list)

# Print the sorted list
print("List after sorting is:", sorted_list)

