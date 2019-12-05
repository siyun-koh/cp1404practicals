numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]: 3
# numbers[-1]: 2
# numbers[3]: 1
# numbers[:-1]: 3, 1, 4, 1, 5, 9, 2
# numbers[3:4]: 1
# 5 in numbers: True
# 7 in numbers: False
# "3" in numbers: False
# numbers + [6, 5, 3]: 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

print(numbers + [6, 5, 3])

# 1. Change the first element of numbers to "ten"
numbers[0] = "ten"

# 2. Change the last element of numbers to 1
numbers[-1] = 1

# 3. Get all elements from numbers except the first two
numbers[2:]

# 4. Check if 9 is an element in numbers
9 in numbers

