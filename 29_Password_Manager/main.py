from tkinter import END, Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox
from random import randint, choice, shuffle

WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Arial"
FONT = (FONT_NAME, 16, "bold") 

# Password Generator
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [ choice(letters) for _ in range(randint(8, 10))]
    password_list += [ choice(symbols) for _ in range(randint(2, 4))]
    password_list += [ choice(numbers) for _ in range(randint(2, 4))]
    
    shuffle(password_list)

    password = "".join(password_list) 
    input_password.delete(0,END)
    input_password.insert(0, password)

# Save FILE
def save():
    user_website = input_website.get() 
    user_input = input_user_input.get() 
    user_pwd = input_password.get()
    
    if len(user_website) == 0 or len(user_input) == 0 or len(user_pwd) == 0:
        messagebox.showerror(title="Input empty", message="Please make sure you haven't left any fields empty")
    else:
        is_ok_to_save =  messagebox.askokcancel( title=user_website,
                                  message=f"These are the details entered:\n"
                                        f"Email: {user_input} \n"
                                        f"Password:{user_pwd}\n"
                                        f"Is it ok to save?") 
        if is_ok_to_save:
            with open("data.txt", mode="a") as file:
                file.write(f"{user_website} | {user_input} | {user_pwd} \n")
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
btn_generate_pwd = Button(text="Generate Password", command=password_generator)
btn_generate_pwd.grid(column=2, row=3)

btn_add_pwd = Button(text="Add", width=36, command=save)
btn_add_pwd.grid(column=1, row=4, columnspan=2)


window.mainloop()
