from tkinter import *


def calculate_km():
    miles = float(user_input.get())
    kilometers = miles * 1.609344
    kilometer_label.config(text=f"{round(kilometers)}")


# Screen
window = Tk()
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

# Title
window.title("Mile to Km Converter")

# Entry
user_input = Entry(width=20)
user_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=("Arial", 20, "normal"))
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=("Arial", 20, "normal"))
equal_to_label.grid(column=0, row=1)

kilometer_label = Label(text="0", font=("Arial", 20, "normal"))
kilometer_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 20, "normal"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", width=20, command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()
