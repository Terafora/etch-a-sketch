from turtle import Turtle, Screen, clear

brush = Turtle()
screen = Screen()

brush.pensize(3)

def move_forward():
    brush.forward(10)

def move_backward():
    brush.backward(10)

def turn_left():
    brush.left(10)

def turn_right():
    brush.right(10)

def reset():
    brush.home()
    brush.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()