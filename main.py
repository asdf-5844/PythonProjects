from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('road.gif')

y_positions = [-260, -172, -85, 2, 85, 172, 260]
colors = ['white', 'red', 'orange', 'yellow', 'blue', 'green', 'purple']
all_tur = []

user_bet = screen.textinput("Enter your bet", "Which turtle color will win? (white, red, orange, yellow, blue, green, purple)")

for index in range(0, 7):
    new_tur = Turtle(shape="turtle")
    new_tur.shapesize(2)
    new_tur.speed('fastest')
    new_tur.penup()
    new_tur.goto(x=-350, y=y_positions[index])
    new_tur.color(colors[index])
    all_tur.append(new_tur)

is_on = True
while is_on:
    for turtle in all_tur:
        if turtle.xcor() > 330:
            is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                turtle.write("You won! " + winner + " turtle is the winner.", font=("Courier", 16, "normal"),
                             align="right")
            else:
                turtle.write("You lose! " + winner + " turtle is the winner.", font=("Courier", 16, "normal"),
                             align="right")
        random_speed = random.randint(0, 7)
        turtle.forward(random_speed)

screen.exitonclick()