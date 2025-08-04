from turtle import Screen, Turtle
from participant import Participant
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

tim = Participant()
all_turtles = tim.all_turtle
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            wining_color =turtle.pencolor()

            if wining_color == user_bet:
                print(f"you've won! the {wining_color}, turtle is the winner!")

            else:
                print(f"you've lost! the {wining_color}, turtle is the winner!")     

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
     

screen.exitonclick()