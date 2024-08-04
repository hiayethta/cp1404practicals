"""
CP1404 Practical
Car class
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Based on reliability, drive car"""
        random_number = randint(1, 100)
        if random_number < self.reliability:
            distance = 0
