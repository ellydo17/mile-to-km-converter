from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=500)
window.config(padx=10, pady=10)

def button_clicked():
    km["text"] = int(mile.get()) * 1.609

# Entry
mile = Entry(width=10)
mile.grid(column=1, row=0)

# Label
is_equal = Label(text="is equal to", font=("Arial", 12))
is_equal.grid(column=0, row=1)

mile_unit = Label(text="Miles", font=("Arial", 12))
mile_unit.grid(column=2, row=0)

km = Label(text="0", font=("Arial", 12))
km.grid(column=1, row=1)

km_unit = Label(text="Km", font=("Arial", 12))
km_unit.grid(column=2, row=1)

# Button
calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)

window.mainloop()  # keep the window on the screen


