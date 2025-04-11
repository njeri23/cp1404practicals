class Taxi:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0
        self.current_fare_distance = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def drive(self, distance):
        distance_driven = min(distance, self.fuel)
        self.fuel -= distance_driven
        self.odometer += distance_driven
        self.current_fare_distance += distance_driven
        return distance_driven

    def start_fare(self):
        self.current_fare_distance = 0

    def get_fare(self):
        return round(1.20 * self.current_fare_distance, 2)


if __name__ == "__main__":
    taxi = Taxi("Prius", 100)
    taxi.drive(40)
    print(taxi)
    print(f"Fare: ${taxi.get_fare()}")
