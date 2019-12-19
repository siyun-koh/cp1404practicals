from prac06.guitar import Guitar

CURRENT_YEAR = 2019


def run_tests():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2012, 1520.8)

    print("{} get_age() - Expected {}. Got {}.".format(gibson.name, 97, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}.".format(other.name, 7, other.get_age()))
    print("{} is_vintage() - Expected {}. Got {}.".format(gibson.name, True, gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}.".format(other.name, False, other.is_vintage()))


def main():
    run_tests()
main()