class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def get_age(self, current_year=2024):
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"
