from turtle import Turtle
import random

COLOR = ["red", "green", "blue", "yellow", "orange", "purple"]
Y_POSITION = [-70, -40, -10, 20, 50, 80]
 


class Participant:
    all_turtle = []
    def __init__(self):

        for turtle_index in range (0, 6):
            new_turtle = Turtle("turtle")
            new_turtle.penup()
            new_turtle.color(COLOR[turtle_index])
            new_turtle.goto(x = -230, y = Y_POSITION[turtle_index])
            self.all_turtle.append(new_turtle)

    # def move(self):
    #     for turtle in all_turtle:
    #         rand_dist = random.randint(0, 10)
    #         turtle.forward(rand_dist)
