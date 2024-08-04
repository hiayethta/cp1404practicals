"""
CP1404
Taxi class
"""
from prac_09.car import Car
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a special version of Taxi"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super.__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare with extra charge"""
        return self.flagfall + super().get_fare()