from tkinter import Tk, Canvas, Button, PhotoImage, Label

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "FiraCode Nerd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=400, bg=YELLOW, highlightthickness=0)
check_marker = "✔"
tomate_img = PhotoImage(file="./tomato.png")
canvas.create_image(150,200, image=tomate_img)
canvas.create_text(155,220, text="00:00", fill="black", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

lbl_over_head = Label(text="Timer", font=(FONT_NAME,40, "bold"), bg=YELLOW, fg=GREEN) 
lbl_over_head.grid(column=1, row=0)
btn_start = Button(text="start" )
btn_start.grid(column=0, row=2)
btn_reset =  Button(text="reset" )
btn_reset.grid(column=2, row=2)
lbl_check = Label(text=check_marker,font=(FONT_NAME,40, "bold"),  bg=YELLOW, fg=GREEN)
lbl_check.grid(column=1, row=3)



window.mainloop()
