# The list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] - The first element of the list, which is 3.
# numbers[-1] - The last element of the list, which is 2.
# numbers[3] - The element at index 3, which is 1.
# numbers[:-1] - The list excluding the last element: [3, 1, 4, 1, 5, 9].
# numbers[3:4] - A slice from index 3 to 4 (excluding 4): [1].
# 5 in numbers - Check if 5 is in the list: True.
# 7 in numbers - Check if 7 is in the list: False.
# "3" in numbers - Check if the string "3" is in the list: False, as it's an integer 3, not a string.
# numbers + [6, 5, 3] - Concatenate the list with [6, 5, 3]: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3].

# Changing the first element of numbers to "ten" (string, not number 10)
numbers[0] = "ten"

# Changing the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
