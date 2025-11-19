# Program #3 Long-Distance Calls
# A long-distance provider charges the following rates for telephone calls:

# Rate Category	Rate per Minute
# Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
# Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
# Off-Peak (midnight through 5:59 P.M.) 	$0.05

# Write a GUI application that allows the user to select a rate category (from a set of radio buttons),
# and enter the number of minutes of the call into an Entry widget.
# An info dialog box should display the charge for the call.

import tkinter as tk
import tkinter.messagebox

class Calls:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Long-Distance Calls")

        self.topframe = tk.Frame(self.main_window)
        self.bottomframe = tk.Frame(self.main_window)
        self.midframe = tk.Frame(self.main_window)

        self.topframe.pack(pady=10,padx=10)
        self.bottomframe.pack(pady=10,padx=10)
        self.midframe.pack(pady=10, padx=10)

        self.minutes_label = tk.Label(self.topframe, text="Enter Total Minutes")
        self.minutes_entry = tk.Entry(self.topframe, width=10)

        self.minutes_label.pack(side="left")
        self.minutes_entry.pack(side="left", padx=5)

        self.rate_var = tk.IntVar()
        self.rate_var.set(1)
        self.rb1 = tk.Radiobutton(self.midframe, text="Daytime (6:00 A.M. through 5:59 P.M.)",
                                  variable=self.rate_var, value=1)
        self.rb2 = tk.Radiobutton(self.midframe, text="Evening (6:00 P.M.  through 11:59 P.M.)",
                                  variable=self.rate_var, value=2)
        self.rb3 = tk.Radiobutton(self.midframe, text="Off-Peak (midnight through 5:59 P.M.)",
                                  variable=self.rate_var, value=3)

        self.rb1.pack(anchor="w")
        self.rb2.pack(anchor="w")
        self.rb3.pack(anchor="w")

        self.calculate_button = tk.Button(self.bottomframe, text='Calculate', command=self.calculate)

        self.quit_button = tk.Button(self.bottomframe, text='Quit', command=self.main_window.destroy)

        self.calculate_button.pack(side="left", padx=10)
        self.quit_button.pack(side="right", padx=10)

        tk.mainloop()

    def calculate(self):
        try:
            minutes = float(self.minutes_entry.get())
            if minutes <= 0:
                raise ValueError

            if self.rate_var.get() == 1:
                rate = .02
            elif self.rate_var.get() == 2:
                rate = .12
            else:
                rate = .05

            total = minutes * rate

            tk.messagebox.showinfo("Call Charge", f"Total Charge: {total:.2f}")
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    Calls()