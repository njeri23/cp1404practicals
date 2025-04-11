from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def get_fare(self):
        fare = super().get_fare() * self.fanciness + self.flagfall
        return round(fare, 2)

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

if __name__ == '__main__':
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f"Fare: ${taxi.get_fare()}")
