from random import randint
from prac08.car import Car


class UnreliableCar(Car):
    """specialised version of Car that includes reliability"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drives the car based on reliability"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
