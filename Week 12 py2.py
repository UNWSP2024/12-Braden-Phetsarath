#Program #2:  Joe's Automotive
#Joe's Automotive performs the following routine maintenance service:

# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00
# Write a GUI with check buttons that allows the user to select any or all of these services.
# When the user clicks a button, the total charges should be displayed.

import tkinter as tk

class Joes_Auto:
    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("Joe's Auto Services")

        self.topframe = tk.Frame(self.main_window)
        self.bottomframe = tk.Frame(self.main_window)
        self.topframe.pack(pady=10,padx=10)
        self.bottomframe.pack(pady=10,padx=10)

        self.oil_var = tk.IntVar()
        self.lube_var = tk.IntVar()
        self.rad_var = tk.IntVar()
        self.trans_var = tk.IntVar()
        self.inspect_var = tk.IntVar()
        self.muffler_var = tk.IntVar()
        self.tire_var = tk.IntVar()

        self.cb1 = tk.Checkbutton(self.topframe, text="Oil Change ($30)", variable=self.oil_var)
        self.cb2 = tk.Checkbutton(self.topframe, text="Lube Job ($20)", variable=self.lube_var)
        self.cb3 = tk.Checkbutton(self.topframe, text="Radiator Flush ($40)", variable=self.rad_var)
        self.cb4 = tk.Checkbutton(self.topframe, text="Transmission Fluid ($100)", variable=self.trans_var)
        self.cb5 = tk.Checkbutton(self.topframe, text="Inspection ($35)", variable=self.inspect_var)
        self.cb6 = tk.Checkbutton(self.topframe, text="Muffler Replacement ($200)", variable=self.muffler_var)
        self.cb7 = tk.Checkbutton(self.topframe, text="Tire Rotation ($20)", variable=self.tire_var)

        self.cb1.pack(anchor='w')
        self.cb2.pack(anchor='w')
        self.cb3.pack(anchor='w')
        self.cb4.pack(anchor='w')
        self.cb5.pack(anchor='w')
        self.cb6.pack(anchor='w')
        self.cb7.pack(anchor='w')

        self.calc_buttom = tk.Button(self.bottomframe, text="Calculate Total", command=self.calculate_total)
        self.calc_buttom.pack(side="left", padx=10)

        self.quit_button = tk.Button(self.bottomframe, text="Quit", command=self.main_window.destroy)
        self.quit_button.pack(side="right", padx=10)

        self.total_label = tk.Label(self.bottomframe, text="Total: $0.00", font=("Arial", 12))
        self.total_label.pack(pady=10)

        tk.mainloop()

    def calculate_total(self):
        total = 0

        if self.oil_var.get() == 1:
            total += 30
        if self.lube_var.get() == 1:
            total +=20
        if self.rad_var.get() == 1:
            total += 40
        if self.trans_var.get() == 1:
            total += 100
        if self.inspect_var.get() == 1:
            total += 35
        if self.muffler_var.get() == 1:
            total += 100
        if self.tire_var.get() == 1:
              total += 20

        self.total_label.config(text=f"Total: ${total:.2f}")

if __name__ == "__main__":
    Joes_Auto()
