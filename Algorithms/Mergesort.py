def merge_sort(array):
    # Base case: if the array is empty or has one element, return it
    if len(array) <= 1:
        return array

    # Find the middle index
    middle = len(array) // 2

    # Divide the array into two halves
    left_half = array[:middle]
    right_half = array[middle:]

    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    merged_array = []
    left_index, right_index = 0, 0

    # Merge the two sorted lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    # Append any remaining elements from both halves
    merged_array.extend(left[left_index:])
    merged_array.extend(right[right_index:])

    return merged_array


if __name__ == "__main__":
    unsorted_array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(unsorted_array)
    print("Sorted array:", sorted_array)
