# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 02/08/2018
# Title: turtleloop
# Description: Program draws six squares using a for loop

import turtle # import graphics library

Richard_Truong = turtle.Turtle () # create a turtle object
Richard_Truong.speed(0)

screen = turtle.Screen ()

screen.bgcolor('white') # change background color

Richard_Truong.penup()
Richard_Truong.setpos(-200,100)
Richard_Truong.pendown()

for i in range(3):
    Richard_Truong.forward(100) # move forward (# of pixels)
    Richard_Truong.right(90)   # turn 90 degrees CW
    Richard_Truong.forward(100)
    Richard_Truong.right(90)
    Richard_Truong.forward(100)
    Richard_Truong.right(90)
    Richard_Truong.forward(100)
    Richard_Truong.right(90)

    Richard_Truong.penup()
    Richard_Truong.forward(150)
    Richard_Truong.pendown()

Richard_Truong.penup()
Richard_Truong.setpos(-200,-50)
Richard_Truong.pendown()

for i in range(3):
    Richard_Truong.forward(100) # move forward (# of pixels)
    Richard_Truong.right(90)   # turn 90 degrees CW
    Richard_Truong.forward(100)
    Richard_Truong.right(90)
    Richard_Truong.forward(100)
    Richard_Truong.right(90)
    Richard_Truong.forward(100)
    Richard_Truong.right(90)

    Richard_Truong.penup()
    Richard_Truong.forward(150)
    Richard_Truong.pendown()

