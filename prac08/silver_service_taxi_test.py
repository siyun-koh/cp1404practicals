from prac08.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Argent", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print("Fare: ${:.2f}".format(my_taxi.get_fare()))


main()
