import random


class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

    def generate_power(self):
        low = self.prop - 10
        high = self.prop + 10
        return random.randrange(low, high)
