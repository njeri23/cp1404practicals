from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    taxi = SilverServiceTaxi("LuxuryCar", 100, 2)
    taxi.drive(25)
    print(taxi)
    print(f"Fare: ${taxi.get_fare()}")

if __name__ == '__main__':
    test_silver_service_taxi()
