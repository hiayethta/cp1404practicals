"""CP1404 Practical - Guitar class"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise values for guitar class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return:  guitar information"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Calculates the age of the guitar"""
        present_year = 2024
        guitar_age = present_year - self.year
        return guitar_age
