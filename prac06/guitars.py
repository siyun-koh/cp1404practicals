from prac06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print("Added", add_guitar)
        name = input("Name: ")

        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

        if guitars:
            guitars.sort()
            print("These are the guitars I own: ")
            for i, guitar in enumerate(guitars):
                vintage_string = ""
                if guitar.is_vintage():
                    vintage_string = "(vintage)"
                print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                          vintage_string))


if __name__ == '__main__':
    main()
