from prac_06.guitar import Guitar


def main():
    """Collect user guitars and display their details."""
    guitars = []

    while True:
        name = input("Enter guitar name (blank to stop): ")
        if name == "":
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
