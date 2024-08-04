"""
CP1404 Practical
Car class
"""

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability
