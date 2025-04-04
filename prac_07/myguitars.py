from guitar import Guitar
import csv


def load_guitars(filename="guitars.csv"):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(guitars, filename="guitars.csv"):
    """Save a list of Guitar objects to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Print all guitars in the list."""
    if not guitars:
        print("No guitars to display.")
    else:
        for i, guitar in enumerate(guitars, 1):
            print(f"{i}. {guitar}")


def add_new_guitar():
    """Prompt user to enter a new guitar's details and return the Guitar object."""
    name = input("Enter guitar name: ")
    while True:
        try:
            year = int(input("Enter year: "))
            break
        except ValueError:
            print("Please enter a valid year.")
    while True:
        try:
            cost = float(input("Enter cost: "))
            break
        except ValueError:
            print("Please enter a valid cost.")
    return Guitar(name, year, cost)


def main():
    print("🎸 My Guitars Program 🎸")
    guitars = load_guitars()
    print(f"{len(guitars)} guitars loaded from file.")

    while True:
        print("\nMenu:")
        print("(D)isplay guitars")
        print("(A)dd new guitar")
        print("(Q)uit and save")
        choice = input(">>> ").strip().lower()

        if choice == 'd':
            display_guitars(guitars)
        elif choice == 'a':
            new_guitar = add_new_guitar()
            guitars.append(new_guitar)
            print(f"{new_guitar.name} added.")
        elif choice == 'q':
            save_guitars(guitars)
            print(f"{len(guitars)} guitars saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from the menu options.")


if __name__ == "__main__":
    main()

