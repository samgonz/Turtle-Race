from random import randint
from turtle import Turtle, Screen
import time

users_choice = input('Which color turtle do you think will win? (Red|Green|Blue|Purple)\n').lower()

race_complete = False
winning_color = 'none'

timmy_the_turtle = Turtle()
timmy_the_turtle.color('Blue')
timmy_the_turtle.penup()
timmy_the_turtle.setposition(-400, -50)
timmy_the_turtle.pendown()
timmy_wins = False

tommy_the_turtle = Turtle()
tommy_the_turtle.color('Red')
tommy_the_turtle.penup()
tommy_the_turtle.setposition(-400, -25)
tommy_the_turtle.pendown()
tommy_wins = False

terry_the_turtle = Turtle()
terry_the_turtle.color('purple')
terry_the_turtle.penup()
terry_the_turtle.setposition(-400, 0)
terry_the_turtle.pendown()
terry_wins = False

tracy_the_turtle = Turtle()
tracy_the_turtle.color('green')
tracy_the_turtle.penup()
tracy_the_turtle.setposition(-400, 25)
tracy_the_turtle.pendown()
tracy_wins = False

winning_line = Turtle()
winning_line.penup()
winning_line.setposition(400, 400)
winning_line.setheading(270)
winning_line.pendown()
winning_line.forward(800)
screen = Screen()

def moveForward(turtle):
    forward_amount = randint(1, 50)
    turtle.forward(forward_amount)
    
def winRace():
    global timmy_wins
    global tommy_wins
    global terry_wins
    global tracy_wins
    global winning_color
    
    if timmy_the_turtle.pos()[0] >= winning_line.pos()[0]:
        timmy_wins = True
        winning_color = 'blue'
        return True
    if tommy_the_turtle.pos()[0] >= winning_line.pos()[0]:
        tommy_wins = True
        winning_color = 'red'
        return True
    if terry_the_turtle.pos()[0] >= winning_line.pos()[0]:
        terry_wins = True
        winning_color = 'purple'
        return True
    if tracy_the_turtle.pos()[0] >= winning_line.pos()[0]:
        tracy_wins = True
        winning_color = 'green'
        return True
    return False

while race_complete == False:
    time.sleep(0.5)
    moveForward(timmy_the_turtle)
    moveForward(tommy_the_turtle)
    moveForward(terry_the_turtle)
    moveForward(tracy_the_turtle)
    race_complete = winRace()
    
if users_choice != winning_color:
    print('You Lose!, You did not choose the correct turtle!')
    exit()

match winning_color:
    case "red":
        print('You Win!, Tommy wins!')

    case "blue":
        print('You Win!, Timmy wins!')
    
    case "green":
        print('You Win!, Tracy wins!')
    
    case "purple":
        print('You Win!, Terry wins!')        


    
    
