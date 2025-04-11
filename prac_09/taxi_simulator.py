from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display list of taxis with index numbers."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    """Main program to simulate taxi driving."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_fare = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)

    while True:
        choice = input(">>> ").lower()
        if choice == 'q':
            break
        elif choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (IndexError, ValueError):
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi:
                current_taxi.start_fare()
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    print(f"Your trip cost you ${fare:.2f}")
                    total_fare += fare
                except ValueError:
                    print("Invalid distance")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare:.2f}")
        print(menu)

    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()
