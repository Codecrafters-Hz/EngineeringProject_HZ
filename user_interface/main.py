from user_interface.ui import UserInterface
import tkinter as tk
def main():
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()
    ui.display_force_values()
    ui.display_average_force()
    ui.display_max_force()
    ui.display_min_force()
    ui.display_force_value(3)
    ui.reset_force_values()

if __name__ == "__main__":
    main()
