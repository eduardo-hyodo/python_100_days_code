from tkinter import END, Tk, Canvas, Entry, Button, PhotoImage, Label

WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Arial"
FONT = (FONT_NAME, 16, "bold") 
user_info = ""

def save():
    with open("data.txt", mode="a") as file:
        global user_info
        user_info = input_website.get() + "|"
        user_info += input_user_input.get() + "|"
        user_info += input_password.get()
        if user_info != "":
            file.write(user_info + "\n")
    clear()

def clear():
    input_website.delete(0,END)
    # input_user_input.delete(0,END)
    input_password.delete(0,END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)
canvas = Canvas(width=200, height=200, bg=WHITE)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(column=1, row=0)

lbl_website = Label(text="Website:", font=FONT, bg=WHITE, fg=BLACK) 
lbl_website.grid(column=0, row=1)
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()


lbl_user_input = Label(text="Email/User:", font=FONT, bg=WHITE, fg=BLACK) 
lbl_user_input.grid(column=0, row=2)
input_user_input = Entry(width=35)
input_user_input.grid(column=1, row=2,columnspan=2)
input_user_input.insert(0,"user@example.com")

lbl_password = Label(text="Password:", font=FONT, bg=WHITE, fg=BLACK) 
lbl_password.grid(column=0, row=3)
input_password = Entry(width=21)
input_password.grid(column=1, row=3)
btn_generate_pwd = Button(text="Generate Password")
btn_generate_pwd.grid(column=2, row=3)

btn_add_pwd = Button(text="Add", width=36, command=save)
btn_add_pwd.grid(column=1, row=4, columnspan=2)


window.mainloop()
