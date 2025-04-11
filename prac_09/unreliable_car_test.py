from unreliable_car import UnreliableCar

def test_drive():
    car = UnreliableCar("TestCar", 100, 50)
    distance = car.drive(30)
    print(f"Drove: {distance}km")
    print(car)

if __name__ == '__main__':
    test_drive()
