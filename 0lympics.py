# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 2.0 Class lab
# Date: 1/29/2018
# Title: 0lympics
# Description: Program draws olympic logo in difference colors

import turtle # import graphics library

Richard_Truong = turtle.Turtle () # create a turtle object
                                    # done once

screen = turtle.Screen ()
screen.bgcolor('white') # change background color

Richard_Truong.pensize (5)

Richard_Truong.penup()
Richard_Truong.setpos(-100,0)
Richard_Truong.pendown()

Richard_Truong.pencolor ('blue')

Richard_Truong.circle (50) # draw circle with radius of 50 pixels

Richard_Truong.pencolor ('black')

Richard_Truong.penup()
Richard_Truong.forward(110)
Richard_Truong.pendown()

Richard_Truong.circle (50)

Richard_Truong.pencolor ('red')

Richard_Truong.penup()
Richard_Truong.forward(110)
Richard_Truong.pendown()

Richard_Truong.circle (50)

Richard_Truong.pencolor ('yellow')

Richard_Truong.penup()
Richard_Truong.setpos(-45,-50)
Richard_Truong.pendown()

Richard_Truong.circle (50)

Richard_Truong.pencolor ('green')

Richard_Truong.penup()
Richard_Truong.setpos(65,-50)
Richard_Truong.pendown()

Richard_Truong.circle (50)

Richard_Truong.penup()
Richard_Truong.setpos(-100,0)
Richard_Truong.pendown()

Richard_Truong.pencolor ('blue')

Richard_Truong.circle (50,-300)
Richard_Truong.penup()
Richard_Truong.circle (50,-60)
Richard_Truong.pendown()

Richard_Truong.penup()
Richard_Truong.setpos(10,0)
Richard_Truong.pendown()

Richard_Truong.pencolor ('black')

Richard_Truong.circle (50,-45)
Richard_Truong.penup()
Richard_Truong.circle (50,-135)
Richard_Truong.pendown()
Richard_Truong.circle (50,-95)
Richard_Truong.penup()
Richard_Truong.circle (50,-85)

Richard_Truong.pencolor ('red')

Richard_Truong.setpos(120,0)
Richard_Truong.pendown()
Richard_Truong.circle (50,-45)
