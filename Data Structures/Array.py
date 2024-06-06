# Creating an array (list) with some initial values
my_array = [1, 2, 3, 4, 5]

# Accessing elements of the array
print("First element:", my_array[0])  # Output: 1
print("Last element:", my_array[-1])  # Output: 5

# Modifying elements of the array
my_array[2] = 10
print("Modified array:", my_array)  # Output: [1, 2, 10, 4, 5]

# Appending elements to the array
my_array.append(6)
print("After append:", my_array)  # Output: [1, 2, 10, 4, 5, 6]

# Removing elements from the array
my_array.remove(4)
print("After removal:", my_array)  # Output: [1, 2, 10, 5, 6]

# Finding the length of the array
print("Length of array:", len(my_array))  # Output: 5

# Iterating over the array
print("Array elements:")
for element in my_array:
    print(element)
