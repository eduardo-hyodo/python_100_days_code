import tkinter

window = tkinter.Tk()
window.title("Window")
window.minsize(width=500, height=300)

# def add(*args):
#     result = 0
#     for name in args:
#         result += name
#     return result


def change_label():
    my_label.config(text=my_input.get()) 
#Label
# my_label = tkinter.Label(text=add(1,2,3,4,5), font=("Arial", 24, "bold"))
my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_button_1 =  tkinter.Button(text="Click Me", command=change_label)
my_button_1.grid(column=1, row=1)

my_button_2 =  tkinter.Button(text="Click Me")
my_button_2.grid(column=2, row=0)

my_input = tkinter.Entry()
my_input.grid(column=3, row=2)


window.mainloop()
