import turtle
import pandas as pd
from state_board import StateBoard

screen =  turtle.Screen()
screen.setup(width=800,height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df_50_states =  pd.read_csv("50_states.csv")
all_states = df_50_states["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state =  screen.textinput(title="Guess the State", 
                                     prompt="What's another state's name?")
    if answer_state != None:
        answer_state = answer_state.title()
    if answer_state == "Exit":
        # missing_states = df_50_states.groupby("state").filter(lambda x: x.state.item() not in guessed_states ) 
        # df_misssing_states = pd.DataFrame(
        #         data=missing_states.state.to_list(),
        #         columns=["State"],
        # )
        # df_misssing_states.to_csv("missing_states.csv")
        # or without Pandas
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df_misssing_states = pd.DataFrame(missing_states)
        df_misssing_states.to_csv("missing_states.csv")
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        r_state = df_50_states[df_50_states["state"] == answer_state]
        StateBoard(r_state.state.item(), float(r_state["x"]), float(r_state["y"]))

# missing_states = missing_states.to_list()
# missing_states.to_csv("missing_states.csv")

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
