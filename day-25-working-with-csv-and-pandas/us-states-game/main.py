import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data["state"].to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="What's another state's name?")
    answer = answer.title()

    if answer == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_data = pandas.DataFrame({'state': missing_states})
        missing_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_data = states_data[states_data['state'] == f"{answer}"]
        t.goto(int(answer_data.x), int(answer_data.y))
        t.write(f"{answer}")

