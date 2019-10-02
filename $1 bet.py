#Richard Truong CMPSC121
# Draw a square
import turtle # import graphics libraryt
t1= turtle.Turtle()# create a turtle object
                 # done once
t1.forward(50) # move forward (# of pixels)
t1.right(90)   # turn 90 degrees CW
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.penup ()

t1.forward(100)
t1.pendown ()
t1.pencolor('red')

t1.forward(50) # move forward (# of pixels)
t1.right(90)   # turn 90 degrees CW
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.penup ()

t1.forward(100)
t1.pendown ()
t1.pencolor('blue')

t1.forward(50) # move forward (# of pixels)
t1.right(90)   # turn 90 degrees CW
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.penup ()

t1.done()
