from tkinter import Tk, Canvas, Button, PhotoImage, Label

WHITE = "#ffffff"

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)
canvas = Canvas(width=800, height=800, bg=WHITE)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(400,400, image=logo_image)
canvas.grid(column=1, row=1)



window.mainloop()
