from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label

WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Arial"
FONT = (FONT_NAME, 16, "bold") 

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


lbl_user_input = Label(text="Email/User:", font=FONT, bg=WHITE, fg=BLACK) 
lbl_user_input.grid(column=0, row=2)
input_user_input = Entry(width=35)
input_user_input.grid(column=1, row=2,columnspan=2)

lbl_password = Label(text="Password:", font=FONT, bg=WHITE, fg=BLACK) 
lbl_password.grid(column=0, row=3)
input_password = Entry(width=21)
input_password.grid(column=1, row=3)
btn_generate_pwd = Button(text="Generate Password")
btn_generate_pwd.grid(column=2, row=3)

btn_add_pwd = Button(text="Add", width=36)
btn_add_pwd.grid(column=1, row=4, columnspan=2)


window.mainloop()
