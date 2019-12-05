import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    quick_picks_number = int(input("How many quick picks?: "))
    while quick_picks_number < 0:
        print("Invalid number entered")
        quick_picks = int(input("How many quick picks?: "))
    for i in range(quick_picks_number):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
