from tkinter import Tk, Button, Label, Entry, IntVar

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

input_var = IntVar()
input_var.set(0)
input =  Entry(width= 6, textvariable=input_var)
input.grid(column=1, row=0, padx=50, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

def converter_miles_to_km():
    result = 1.609 * input_var.get()
    result_label.config(text=f"{result}")

calculate_btn = Button(text="Calculate", command=converter_miles_to_km)
calculate_btn.grid(column=1, row=2)


window.mainloop()
