out_file = open("name.txt", "w")
name = input("Enter your name: ")
out_file.write(name + "\n")
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is: ", name)

print("\n")

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

print("\n")

in_file = open("numbers.txt", "r")
numberSum = 0
for line in in_file:
    number = int(line)
    numberSum += number
in_file.close()
print("Sum of all numbers: ", numberSum)