# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 02/08/2018
# Title: inlabsquareloop
# Description: Program draws one square using a for loop

import turtle

Richard_Truong = turtle.Turtle () # create a turtle object
Richard_Truong.speed(0)

screen = turtle.Screen ()

screen.bgcolor('white') # change background color

Richard_Truong.penup()
Richard_Truong.setpos(-50,100)
Richard_Truong.pendown()

for i in range(1):
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
