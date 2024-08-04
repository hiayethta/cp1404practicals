"""
CP1404 Practical

Program to test Unreliable Car object
"""
from prac_09.car import Car
from prac_09.unreliable_car import UnreliableCar

uc1 = UnreliableCar("Corolla", 100, 30)
uc1.drive(20)
print(uc1)
