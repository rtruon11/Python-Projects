import turtle # import graphics library
import random # import random function
import time # import time function
from turtle import * #imports function to do gifs into Turtle

play = turtle.Screen()
key = turtle.Screen() #?
screen = turtle.Screen () #allows user to click onto screen
Richard_Truong = turtle.Turtle ()
Play_again = turtle.Turtle() #play or exit button Turtle drawing box

Play_again.penup ()
Play_again.setpos (-120,-100)
Play_again.pendown ()

for i in range(2): #creates text option for either play again or exit
    Play_again.speed(0)
    Play_again.begin_fill()
    Play_again.color('black','green')
    for j in range (2):
        Play_again.forward(170)
        Play_again.right(90)
        Play_again.forward(40)
        Play_again.right(90)
    Play_again.end_fill()
    Play_again.penup()
    Play_again.forward(200)
    Play_again.pendown()

Play_again.penup ()
Play_again.setpos (-115,-125)
Play_again.pendown ()
Play_again.write('Do you want to play again? Press y', font=('Arial',10, 'normal'))

Play_again.penup ()
Play_again.setpos (100,-125)
Play_again.pendown ()
Play_again.write('Do you want to exit? Press n', font=('Arial',10, 'normal'))
