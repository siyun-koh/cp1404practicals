passwordMinLength = 8

password = input("Please enter a password of minimum {} characters: ".format(passwordMinLength))
while len(password) < passwordMinLength:
    print("Your password is too short. Please enter a new one.")
    password = input("Please enter a password of minimum {} characters: ".format(passwordMinLength))

print('*' * len(password))

