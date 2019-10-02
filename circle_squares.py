# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 02/08/2018
# Title: circle&squares
# Description: Program draws three squares 100 pixel in size each with a different color, Draws a circle above the squares, When clicked on circle changes colored based on square

import turtle # import graphics library

Richard_Truong = turtle.Turtle () # create a turtle object
Richard_Truong.speed(0)

screen = turtle.Screen ()

top_circle = turtle.Turtle ()
top_circle.speed(0)

screen.bgcolor('white') # change background color

Richard_Truong.penup()
Richard_Truong.setpos(-200,-50)
Richard_Truong.pendown()

for i in range(3):
    for j in range(3):
        Richard_Truong.begin_fill()
        Richard_Truong.color('black','red')
        Richard_Truong.forward(100) # move forward (# of pixels)
        Richard_Truong.right(90)   # turn 90 degrees CW
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.end_fill()

        Richard_Truong.penup()
        Richard_Truong.forward(150)
        Richard_Truong.pendown()

        Richard_Truong.begin_fill()
        Richard_Truong.color('black','green')
        Richard_Truong.forward(100) # move forward (# of pixels)
        Richard_Truong.right(90)   # turn 90 degrees CW
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.end_fill()

        Richard_Truong.penup()
        Richard_Truong.forward(150)
        Richard_Truong.pendown()

        Richard_Truong.begin_fill()
        Richard_Truong.color('black','blue')
        Richard_Truong.forward(100) # move forward (# of pixels)
        Richard_Truong.right(90)   # turn 90 degrees CW
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.forward(100)
        Richard_Truong.right(90)
        Richard_Truong.end_fill()

        Richard_Truong.penup()
        Richard_Truong.setpos(0,50)
        Richard_Truong.pendown()

        Richard_Truong.circle(50)

def change (x, y): # call this 'function' when mouse click
    if -150 < y < -50 and -200 < x < -100:

        top_circle.penup()
        top_circle.setpos(0,50)
        top_circle.pendown()
        top_circle.begin_fill()
        top_circle.color('black','red')
        top_circle.circle(50)
        top_circle.end_fill()
        
    elif -150 < y < -50 and -50 < x < 50:
        top_circle.penup()
        top_circle.setpos(0,50)
        top_circle.pendown()
        top_circle.begin_fill()
        top_circle.color('black','green')
        top_circle.circle(50)
        top_circle.end_fill()
        
    else:
        -150 < y < -50 and 100 < x < 200
        top_circle.penup()
        top_circle.setpos(0,50)
        top_circle.pendown()
        top_circle.begin_fill()
        top_circle.color('black','blue')
        top_circle.circle(50)
        top_circle.end_fill()

screen.onclick(change)
