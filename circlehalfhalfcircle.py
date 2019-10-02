# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 2.0 Class lab
# Date: 1/29/2018
# Title: Circles and 1 half and half
# Description: Draws full circle at 50 pixel radius, half circle 50 pixel apart at 50 pixel radius, another half circle 50 pixel apart at 50 pixel radius 

import turtle # import graphics library

Richard_Truong = turtle.Turtle () # create a turtle object
                                    # done once

screen = turtle.Screen ()
screen.bgcolor('gray') # change background color

Richard_Truong.pencolor ('yellow')

Richard_Truong.circle (50) # draw circle with radius of 50 pixels

Richard_Truong.pencolor ('blue')

Richard_Truong.penup()
Richard_Truong.forward(100)
Richard_Truong.pendown()

Richard_Truong.circle (50,180)

Richard_Truong.right (270)
Richard_Truong.forward(100)
Richard_Truong.right (270)

Richard_Truong.penup ()
Richard_Truong.forward (150)
Richard_Truong.right (270)
Richard_Truong.pendown ()

Richard_Truong.pencolor ('green')

Richard_Truong.forward (100)
Richard_Truong.right (270)

Richard_Truong.circle (50,180)

Richard_Truong.right (270)
Richard_Truong.forward (100)

