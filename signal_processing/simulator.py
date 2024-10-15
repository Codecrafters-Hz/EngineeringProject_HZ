import random

class ForceSimulator:
    def __init__(self):
        self.force_values = [0] * 8

    def simulate_force_values(self):
        self.force_values = [random.uniform(0, 100) for _ in range(8)]
        return self.force_values

    def get_force_value(self, index):
        if 0 <= index < len(self.force_values):
            return self.force_values[index]
        else:
            raise IndexError("Index out of range")

    def average_force(self):
        return sum(self.force_values) / len(self.force_values)

    def max_force(self):
        return max(self.force_values)

    def min_force(self):
        return min(self.force_values)

    def reset_force_values(self):
        self.force_values = [0] * 8
