def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    # Compare elements from the left and right arrays
    # and merge them into a single sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Example usage:
input_list = [12, 11, 13, 5, 6, 7]
sorted_list = merge_sort(input_list)
print("Sorted array:", sorted_list)  # Output: [5, 6, 7, 11, 12, 13]
