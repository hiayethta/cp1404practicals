"""
CP1404 Practical
Testing file for Taxi
"""

from prac_09.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(f"{my_taxi} {my_taxi.get_fare()}")  # Taxi details and current fare
my_taxi.start_fare()  # Restart fare
my_taxi.drive(100)
print(f"{my_taxi} {my_taxi.get_fare()}")
