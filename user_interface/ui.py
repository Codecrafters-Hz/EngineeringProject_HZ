import tkinter as tk
from signal_processing.simulator import ForceSimulator

class UserInterface:
    def __init__(self, root):
        self.simulator = ForceSimulator()

        root.geometry("900x450")
        root.title("CodeCrafters")
        self.button = tk.Button(root, text="Show Sample Force Value", command=self.display_force_values)
        self.button.pack(pady=10)
        self.force_label = tk.Label(root, text="")
    def display_force_values(self):
        force_values = self.simulator.simulate_force_values()

        self.force_label.pack(pady=10)
        self.force_label.config(text=f"Simulated Force Values: {force_values}")


    def display_average_force(self):
        avg_force = self.simulator.average_force()
        print("Average Force:", avg_force)

    def display_max_force(self):
        max_force = self.simulator.max_force()
        print("Max Force:", max_force)

    def display_min_force(self):
        min_force = self.simulator.min_force()
        print("Min Force:", min_force)

    def display_force_value(self, index):
        try:
            force_value = self.simulator.get_force_value(index)
            print(f"Force Value at index {index}:", force_value)
        except IndexError as e:
            print(e)

    def reset_force_values(self):
        self.simulator.reset_force_values()
        print("Force values have been reset.")
