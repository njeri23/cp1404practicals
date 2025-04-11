from taxi import Taxi

def run_tests():
    my_taxi = Taxi("Prius", 100)
    print(my_taxi)
    my_taxi.drive(30)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare()}")

if __name__ == '__main__':
    run_tests()
