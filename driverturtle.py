# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 6
# Date: 03/01/2018
# Title: driveturtle
# Description: drive a car simulation

import turtle

car=turtle.Turtle()
screen = turtle.Screen()
screen.screensize(320,320)
turtle.hideturtle()

def fwd():
    car.forward(45)
    if car.xcor() > 320 or car.xcor () < -320:
        car.setpos(0, 0)
    if car.ycor() > 320 or car.ycor () < -320:
        car.setpos(0, 0)

def rev():
    car.back(90)

def left():
    car.left(45)

def right():
    car.right(45)


screen.onkey(fwd,'Up')
screen.onkey(rev,'Down')
screen.onkey(left,'Left')
screen.onkey(right,'Right')

screen.listen()
