#Program #1: MPG Calculator
#Write a GUI program that calculates a car's gas mileage.
# The program's window should have Entry widgets that let the user enter the number of gallons of gas the car holds,
# and the number of miles it can be driven on a full tank.  When a Calculate MPG button is clicked, the program should display the number of miles that the car may be driven per gallon of gas.
# Use the following formula to calculate miles per gallon:  MPG = miles / gallons.

import tkinter
import tkinter.messagebox
class myGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.topframe.pack(pady=10)
        self.bottomframe.pack(pady=10)
        self.midframe.pack(pady=10)

        self.gallons_label = tkinter.Label(self.topframe, text="Gallons")
        self.gallons_entry = tkinter.Entry(self.topframe, width=10)

        self.miles_label = tkinter.Label(self.topframe, text="Miles")
        self.miles_entry = tkinter.Entry(self.topframe, width=10)

        self.gallons_label.pack(side="left")
        self.gallons_entry.pack(side="left", padx=5)
        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left", padx=5)


        self.value = tkinter.StringVar()
        self.calculate_label = tkinter.Label(self.midframe,textvariable = self.value)
        self.calculate_label.pack()

        self.calculate_button = tkinter.Button(self.topframe, text = 'Calculate', command = self.calculate)
        self.quit_button = tkinter.Button(self.bottomframe, text = 'Quit', command = self.main_window.destroy)

        self.calculate_button.pack(side="left", padx=10)
        self.quit_button.pack(side="right", padx=10)


        tkinter.mainloop()

    def calculate(self):
        try:
            self.gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())
            if self.gallons <= 0:
                raise ValueError

            mpg = miles / self.gallons
            self.value.set(mpg)

        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter a valid number.")
if __name__ == "__main__":
    myGui()