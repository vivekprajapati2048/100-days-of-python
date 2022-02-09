from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Etch a Sketch

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
    
def move_left():
    tim.left(15)
    
def move_right():
    tim.right(15)

def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()