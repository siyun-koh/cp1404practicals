import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Question 1: Smallest number seen was 5, largest number seen was 20

# Question 2: Smallest number 3, largest number 9. The number 4 could not have appeared due to the step value of 2.

# Question 3: Line 3 outputs a random number between 2.5 and 5.5.

# code that generates random number between 1 and 100 inclusive:

print(random.randint(1, 100))