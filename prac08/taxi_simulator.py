from prac08.car import Car
from prac08.taxi import Taxi
from prac08.silver_service_taxi import SilverServiceTaxi

"""Taxi simulator:
Each time, until they quit:
--The user should be presented with a list of available taxis and get to choose one,
--Then they can choose how far they want to drive,
--At the end of each trip, show them the trip cost and add it to their bill."""

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_fare = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            # no error-checking
            taxi_choice = int(input("Choose a taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("How far?: "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_fare += trip_cost
        else:
            print("Invalid option.")
        print("Bill to date: ${:.2f}".format(total_fare))
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxi condition now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
