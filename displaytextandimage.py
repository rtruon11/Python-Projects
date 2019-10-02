# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 02/08/2018
# Title: 
# Description:

import turtle # import graphics library
from turtle import *

Richard_Truong = turtle.Turtle () # create a turtle object
Richard_Truong.speed(0)

screen = turtle.Screen ()

screen = Screen()
rick = 'rick.gif'
sea = 'sea.gif'
dog = 'dog.gif'

screen.register_shape(rick)
screen.register_shape(sea)
screen.register_shape(dog)

screen.bgcolor('white') # change background color

Richard_Truong.penup()
Richard_Truong.setpos(-200,-50)
Richard_Truong.pendown()

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

def change (x, y): # call this 'function' when mouse click
    if -150 < y < -50 and -200 < x < -100:
        Richard_Truong.undo()
        rickturtle = Turtle(rick)
        Richard_Truong.speed(0)
        Richard_Truong.penup()
        Richard_Truong.setpos(0,50)
        Richard_Truong.pendown()
        Richard_Truong.color('red')
        Richard_Truong.write ('Thank you for clicking this red box', font=('Arial',16, 'normal'))

        Richard_Truong.penup()
        Richard_Truong.setpos(-200,-50)
        Richard_Truong.pendown()

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

    elif -150 < y < -50 and -50 < x < 50:
        Richard_Truong.undo()
        Richard_Truong.speed(0)
        seaturtle = Turtle(sea)
        Richard_Truong.penup()
        Richard_Truong.setpos(0,50)
        Richard_Truong.pendown()
        Richard_Truong.color('green')
        Richard_Truong.write ('Thank you for clicking this green box', font=('Arial',16, 'normal'))

        Richard_Truong.penup()
        Richard_Truong.setpos(-200,-50)
        Richard_Truong.pendown()

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

    else:
        -150 < y < -50 and 100 < x < 200
        Richard_Truong.undo()
        Richard_Truong.speed(0)
        dogturtle = Turtle(dog)
        Richard_Truong.penup()
        Richard_Truong.setpos(0,50)
        Richard_Truong.pendown()
        Richard_Truong.color('blue')
        Richard_Truong.write ('Thank you for clicking this blue box', font=('Arial',16, 'normal'))

        Richard_Truong.penup()
        Richard_Truong.setpos(-200,-50)
        Richard_Truong.pendown()

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

screen.onclick(change)
