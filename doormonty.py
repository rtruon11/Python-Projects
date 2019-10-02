import turtle # import graphics library
import random
import time
from turtle import *
play = turtle.Screen()
key = turtle.Screen()
Richard_Truong = turtle.Turtle ()

Richard_Truong.penup()
Richard_Truong.setpos(50,163)
Richard_Truong.write ("Do you want to play? (press y for yes, n for no)", font=('Arial',16, 'normal'))
time.sleep(1)
Richard_Truong.undo()
def sim():
    Richard_Truong = turtle.Turtle () # create a turtle object
    Richard_Truong.speed(0)
    key = turtle.Screen()
    screen = Screen()
    CS = 'car.gif'
    G1 = 'goat.gif'
    G2 = 'goat.gif'
    G3 = 'goat.gif'
    screen.register_shape(G1)
    screen.register_shape(CS)
    screen.register_shape(G2)
    screen.register_shape(G3)

    screen.bgcolor('white') # change background color

    Richard_Truong.penup()
    Richard_Truong.setpos(-150,-12)
    Richard_Truong.pendown()

    goat = Turtle(G1)
    goat.speed(0)
    goat.penup()
    goat2 = Turtle(G2)
    goat2.speed(0)
    goat2.penup()
    car = Turtle(CS)
    car.speed(0)
    car.penup()

    choice = 0
    i = 0
    goat_counter = 0
    car_counter = 0
    switch = 0

    imagepositions = [ (-100,75), (50,75), (200,75) ]
    while i in range(1):
        choice = 0
        i = 0
        goat_counter = 0
        car_counter = 0
        switch = 0
        goatpos = random.choice(imagepositions)
        goat.setpos(goatpos)
        goat1_position = imagepositions.index(goatpos)+1
        goatpos2 = random.choice(imagepositions)
        goat2.setpos(goatpos2)
        goat2_position = imagepositions.index(goatpos2)+1
        if goat1_position != goat2_position:
            carpos = random.choice(imagepositions)
            car.setpos(carpos)
            car_position = imagepositions.index(carpos)+1

            if car_position != goat2_position and car_position != goat1_position:
                d1 = goat1_position
                d2 = goat2_position
                d3 = car_position
                d11 = int(goat1_position)
                d22 = int(goat2_position)
                d33 = int(car_position)
                i +=1
                for i in range(3):
                    Richard_Truong.setheading(0)
                    Richard_Truong.begin_fill()
                    Richard_Truong.color('black','yellow')
                    Richard_Truong.forward(100) # move forward (# of pixels)
                    Richard_Truong.left(90)   # turn 90 degrees CW
                    Richard_Truong.forward(175)
                    Richard_Truong.left(90)
                    Richard_Truong.forward(100)
                    Richard_Truong.left(90)
                    Richard_Truong.forward(175)
                    Richard_Truong.left(90)
                    Richard_Truong.end_fill()

                    Richard_Truong.penup()
                    Richard_Truong.forward(150)
                    Richard_Truong.pendown()

                d1text = turtle.Turtle ()
                d1text.penup()
                d1text.setpos(goatpos)
                d1text.pendown()
                d1text.write ('Door {}'.format(d11))
                
                d2text = turtle.Turtle ()
                d2text.penup()
                d2text.setpos(goatpos2)
                d2text.pendown()
                d2text.write ('Door {}'.format(d22))
                
                d3text = turtle.Turtle ()
                d3text.penup()
                d3text.setpos(carpos)
                d3text.pendown()
                d3text.write ('Door {}'.format(d33))


                Richard_Truong.penup()
                Richard_Truong.setpos(-65, 60)
                Richard_Truong.pendown()

                for i in range(3):
                    Richard_Truong.begin_fill()
                    Richard_Truong.color('black','green')
                    Richard_Truong.circle(5)
                    Richard_Truong.end_fill()

                    Richard_Truong.penup()
                    Richard_Truong.forward(150)
                    Richard_Truong.pendown()

                def d111():
                    choice = 1
                    print("You picked door number 1!")
                    if choice == d1:
                        print("one goat is behind door #",d2)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos2)
                        print("Do you want to switch to door#",d3)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d3
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            elif choice != car_position:
                                print("You got a goat!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            elif choice != car_position:
                                print("You got a goat!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                    elif choice == d2:
                        print("one goat is behind door #",d1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)

                        print("Do you want to switch to door#",d3)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d3
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                    elif choice == d3:
                        print("one goat is behind door #",d1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        print("Do you want to switch to door#", d2)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d2
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                            
                def d222():
                    choice = 2
                    print("You picked door number 2!")
                    if choice == d1:
                        print("one goat is behind door #",d2)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos2)
                        print("Do you want to switch to door#",d3)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d3
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            elif choice != car_position:
                                print("You got a goat!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            elif choice != car_position:
                                print("You got a goat!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                    elif choice == d2:
                        print("one goat is behind door #",d1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)

                        print("Do you want to switch to door#",d3)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d3
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                    elif choice == d3:
                        print("one goat is behind door #",d1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        print("Do you want to switch to door#", d2)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d2
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1

                    
                def d333():
                    choice = 3
                    print("You picked door number 3!")
                    if choice == d1:
                        print("one goat is behind door #",d2)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos2)
                        print("Do you want to switch to door#",d3)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d3
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            elif choice != car_position:
                                print("You got a goat!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            elif choice != car_position:
                                print("You got a goat!")
                                goat2reveal = Turtle(G3)
                                goat2reveal.penup()
                                goat2reveal.setpos(goatpos)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                    elif choice == d2:
                        print("one goat is behind door #",d1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)

                        print("Do you want to switch to door#",d3)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d3
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                    elif choice == d3:
                        print("one goat is behind door #",d1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        print("Do you want to switch to door#", d2)
                        switch = ord(input("press y for yes or n for no    "))
                        if switch == ord('y'):
                            choice = d2
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1
                        if switch == ord('n'):
                            if choice == car_position:
                                print("Congradulations! You win a car!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                car_counter += 1
                            if choice != car_position:
                                print("You got a goat!")
                                goat1reveal = Turtle(G3)
                                goat1reveal.penup()
                                goat1reveal.setpos(goatpos2)
                                carreveal = Turtle(CS)
                                carreveal.penup()
                                carreveal.setpos(carpos)
                                goat_counter += 1

                    
                key.onkey(d111, "1")
                key.onkey(d222, "2")
                key.onkey(d333, "3")
                key.listen()
                choice = int(choice)
                
            else:
                continue
        else:
            continue
        key.listen()
        Richard_Truong.penup()
        Richard_Truong.setpos(50,163)
        Richard_Truong.wrte ("Do you want to play again? (press y for yes, n for no")
        time.sleep(2)
        Richard_Truong.undo()
    key.listen()
play.onkey(sim,"y")
play.onkey(exit,"n")
play.listen()
key.listen()

        for i in range(2):
            Play_again.forward(150)
            Play_again.right(90)
            Play_again.forward(50)
            Play_again.right(90)
            Play_again.forward(150)
            Play_again.right(90)
            Play_again.forward(50)
            Play_again.right(90)

            Play_again.penup()
            Play_again.forward(200)
            Play_again.pendown()

    for i in range(2):
        
        Play_again.forward(150)
        Play_again.right(90)
        Play_again.forward(50)
        Play_again.right(90)
        Play_again.forward(150)
        Play_again.right(90)
        Play_again.forward(50)
        Play_again.right(90)

        Play_again.penup()
        Play_again.forward(200)
        Play_again.pendown()
        
def change (x,y):
        
        if play_again_x_y == -80 < x > 70 and -100 < y > -50:
            Play_again.write('Do you want to play again pres y?')

        elif play_again_x_y == 70 < x > 220 and -100 < y > -50:
            Play_again.write('Do you want to exit press n?')

screen.onclick(change) #allows user to change object by clicking on screen

                                    if -80 < x > 70 and -100 < y > -50:
                                        Play.again.setpos (-70, -100)
                                        Play_again.write('Do you want to play again pres y?')

                                    elif 70 < x > 220 and -100 < y > -50:
                                        Play.again.setpos (60, -100)
                                        Play_again.write('Do you want to exit press n?')

