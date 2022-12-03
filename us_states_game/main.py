import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_name = data.state.to_list()

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50  States Correct",
                                    prompt="What's another states name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_name if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_name:
        guessed_state.append(answer_state)
        name = turtle.Turtle()
        name.penup()
        name.hideturtle()
        state_data = data[data.state == answer_state]
        name.goto(int(state_data.x), int(state_data.y))
        name.write(answer_state)









