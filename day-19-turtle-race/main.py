from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

for idx, color in enumerate(colors): 
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[idx])
    new_turtle.penup()
    x_pos = -230
    y_pos = -50 + idx * 30 
    new_turtle.goto(x=x_pos, y=y_pos)
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
               
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            if user_bet.lower() == winning_color.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()