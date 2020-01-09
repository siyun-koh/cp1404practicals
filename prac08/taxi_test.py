from prac08.taxi import Taxi


def main():
    """creating and testing taxi object"""
    prius = Taxi("Prius 1", 100)
    prius.drive(40)
    print(prius)
    print("Fare: ${:.2f}".format(prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print(prius)
    print("Fare: ${:.2f}".format(prius.get_fare()))


main()
