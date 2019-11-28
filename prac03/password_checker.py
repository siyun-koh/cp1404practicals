# without function
MIN_PASS_LENGTH = 8

"""password = input("Please enter a password of minimum {} characters: ".format(MIN_PASS_LENGTH))
while len(password) < MIN_PASS_LENGTH:
    print("Your password is too short. Please enter a new one.")
    password = input("Please enter a password of minimum {} characters: ".format(MIN_PASS_LENGTH))
    
    print('*' * len(password))
"""


def main():
    password = get_password(MIN_PASS_LENGTH)
    print_asterisk(password)


def get_password(min_pass_length):
    password = input("Please enter a password of minimum {} characters: ".format(MIN_PASS_LENGTH))
    while len(password) < MIN_PASS_LENGTH:
        print("Your password is too short. Please enter a new one.")
        password = input("Please enter a password of minimum {} characters: ".format(MIN_PASS_LENGTH))
    return password


def print_asterisk(sequence):
    print('*' * len(sequence))


main()
