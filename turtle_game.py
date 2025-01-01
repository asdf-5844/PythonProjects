from turtle import Turtle, Screen
import random

screen = Screen() #Drawing window
screen.setup(width=800, height=600)
screen.bgpic('road.gif') #Set background to a road

#Lists
y_positions = [-260, -172, -85, 2, 85, 172, 260]
colors = ['white', 'red', 'orange', 'yellow', 'blue', 'green', 'purple']
all_tur = []

#Retrieves User Input
user_bet = screen.textinput("Enter your bet", "Which turtle color will win? (white, red, orange, yellow, blue, green, purple)")

for index in range(0, 7): #Draws seven turtles
    new_tur = Turtle(shape="turtle") #turtle shape
    new_tur.shapesize(2) #Increase size
    new_tur.speed('fastest') #Set animation speed to fastest
    new_tur.penup() #Lifts pen so it doesn't draw lines
    new_tur.goto(x=-350, y=y_positions[index]) #Go to starting positions
    new_tur.color(colors[index]) #Assign colors
    all_tur.append(new_tur) #Adds the newly created turtle for later use.

is_on = True
while is_on:
    for turtle in all_tur:
        if turtle.xcor() > 330:
            is_on = False #Stops the race
            winner = turtle.pencolor() #Identifies winning turtle
            if winner == user_bet:
                turtle.write("You won! " + winner + " turtle is the winner.", font=("Courier", 16, "normal"),
                             align="right")
            else:
                turtle.write("You lose! " + winner + " turtle is the winner.", font=("Courier", 16, "normal"),
                             align="right")
        random_speed = random.randint(0, 7)
        turtle.forward(random_speed) #Move turtle forward by random distance

screen.exitonclick() #Exits turtle on a click
