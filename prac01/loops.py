for i in range(1, 21, 2):
    print(i, end=' ')
print()

# counts in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# countdown from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# print n stars
star_number = int(input("Number of stars: "))
for i in range(star_number):
    print('*', end=' ')
print()

# print increasing lines of stars
for i in range(1, star_number + 1):
    print('*' * i)
print()