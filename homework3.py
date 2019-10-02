# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 1
# Date: 1/23/2018
# Title: Program traces out a square
# Description: Trace three squares displayed inside of each other, 1 at 200 pixels, 2 at 150 pixels, 3 at 100 pixels

# Draw a square
import turtle # import graphics library
Richard_Truong = turtle.Turtle()    # create a turtle object
                        # done once

Richard_Truong.forward(200) # move forward (# of pixels)
Richard_Truong.right(90)   # turn 90 degrees CW

Richard_Truong.forward(200)
Richard_Truong.right(90)

Richard_Truong.forward(200)
Richard_Truong.right(90)

Richard_Truong.forward(200)
Richard_Truong.right(90)

Richard_Truong.forward(175)
Richard_Truong.right(90)

Richard_Truong.penup()
Richard_Truong.forward(25)
Richard_Truong.pendown()

Richard_Truong.forward(150)
Richard_Truong.right(90)

Richard_Truong.forward(150)
Richard_Truong.right(90)

Richard_Truong.forward(150)
Richard_Truong.right(90)

Richard_Truong.forward(150)
Richard_Truong.right(90)

Richard_Truong.forward(125)
Richard_Truong.right(90)

Richard_Truong.penup()
Richard_Truong.forward(25)
Richard_Truong.pendown()

Richard_Truong.forward(100)
Richard_Truong.right(90)

Richard_Truong.forward(100)
Richard_Truong.right(90)

Richard_Truong.forward(100)
Richard_Truong.right(90)

Richard_Truong.forward(100)
Richard_Truong.right(90)

Richard_Truong.done()
