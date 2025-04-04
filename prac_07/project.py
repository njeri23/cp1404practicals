class Project:
    """Represent a Project with details like name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"cost: ${self.cost_estimate:.2f}, complete: {self.percent_complete}%")

    def is_complete(self):
        return self.percent_complete == 100
