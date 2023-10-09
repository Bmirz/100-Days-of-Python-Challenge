#Oct. 7, 2023 - Creating my first GUI utlizing Tkinter

# "import *" allows us to use all functions in the import with directly referencing every time
from tkinter import *

#-------Window-------

window = Tk()

window.title("Miles to Km Converter")
window.minsize(width=150, height=150)
window.config(padx=50, pady=50)

# Miles entry
miles_input = Entry(width=10)
#Add some text to begin with
miles_input.insert(END, string="0")
#Gets text in entry
print(miles_input.get())
miles_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

#Connector label
connector_label = Label(text="is equal to", font=("Arial", 12))
connector_label.grid(column=0, row=1)

# Kilometer converstion label
convertion_label = Label(text="0", font=("Arial", 12))
convertion_label.grid(column=1, row=1)

# Km label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

#Calculate button
def miles_to_km():
    print("Button click")
    new_text = str(int(miles_input.get()) * 1.60934)
    convertion_label.config(text=new_text)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)


# '.mainloop()' must be at the end of the program always
window.mainloop()