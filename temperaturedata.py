#Richard Truong
#03/29/18
#COMPSCI 121 002
#HW 7

import random
import math
import statistics

temperature_F = []

index = int(input("How many test are there? Test = "))

for i in range(index):
    if index >= 5 and index <= 15:
        temperature_F.append(float(input(("What are the temperatures (In Fahrenheit): "))))
    else:
        quit()
    
def max_temp():
    print("The maximum value of the index is:",max(temperature_F))
    
def min_temp():
    print("The minimum value of the index is:",min(temperature_F))
    
def average_temp():
    average = sum(temperature_F)/len(temperature_F)
    print("The average temperature from the index is: %.1f" % average)
    aboveaverage = 0
    for k in temperature_F:
        if k > sum(temperature_F)/len(temperature_F):
            aboveaverage += 1
    print("There are", aboveaverage, "temperature values above the average")
    
def std_temp():
    deviation = statistics.stdev(temperature_F)
    print("The standard deviation of the data is: %.1f" % deviation)
    
def median_temp():
    temperature_F.sort()
    if len(temperature_F)%2 == 0:
        print("The median temperature value is:",((temperature_F[int((len(temperature_F)/2)-1)]+(temperature_F[int(len(temperature_F)/2)]))/2))
    if len(temperature_F)%2 == 1:
        print("The median temperature value is:",temperature_F[math.ceil(len(temperature_F)/2)-1])
        
def sort_temp():
    temperature_F.sort()
    print("The given vaues sorted from least to greatest are:", temperature_F)
    
def reverse_temp():
    temperature_F.reverse()
    print("The given vaues sorted from greatest to least are:",temperature_F)
    
def above_freeze():
    above_freeze = 0
    for k in temperature_F:
        if k > 32:
            above_freeze += 1
    print('The amount of values above freezing are', above_freeze)
    
def below_freeze():
    below_freeze = 0
    for k in temperature_F:
        if k <= 32:
            below_freeze += 1
    print('The amount of values below freezing are', below_freeze)
    
max_temp()
min_temp()
average_temp()
std_temp()
median_temp()
sort_temp()
reverse_temp()
above_freeze()
below_freeze()

##How many test are there? Test = 5
##What are the temperatures (In Fahrenheit): 21
##What are the temperatures (In Fahrenheit): 21
##What are the temperatures (In Fahrenheit): 12
##What are the temperatures (In Fahrenheit): 21
##What are the temperatures (In Fahrenheit): 123
##The maximum value of the index is: 123.0
##The minimum value of the index is: 12.0
##The average temperature from the index is: 39.6
##There are 1 temperature values above the average
##The standard deviation of the data is: 46.8
##The median temperature value is: 21.0
##The given vaues sorted from least to greatest are: [12.0, 21.0, 21.0, 21.0, 123.0]
##The given vaues sorted from greatest to least are: [123.0, 21.0, 21.0, 21.0, 12.0]
##The amount of values above freezing are 1
##The amount of values below freezing are 4

##How many test are there? Test = 12
##What are the temperatures (In Fahrenheit): 12
##What are the temperatures (In Fahrenheit): 31
##What are the temperatures (In Fahrenheit): 32
##What are the temperatures (In Fahrenheit): 45
##What are the temperatures (In Fahrenheit): 56
##What are the temperatures (In Fahrenheit): 63
##What are the temperatures (In Fahrenheit): 46
##What are the temperatures (In Fahrenheit): 24
##What are the temperatures (In Fahrenheit): 68
##What are the temperatures (In Fahrenheit): 45
##What are the temperatures (In Fahrenheit): 56
##What are the temperatures (In Fahrenheit): 32
##The maximum value of the index is: 68.0
##The minimum value of the index is: 12.0
##The average temperature from the index is: 42.5
##There are 7 temperature values above the average
##The standard deviation of the data is: 16.7
##The median temperature value is: 45.0
##The given vaues sorted from least to greatest are: [12.0, 24.0, 31.0, 32.0, 32.0, 45.0, 45.0, 46.0, 56.0, 56.0, 63.0, 68.0]
##The given vaues sorted from greatest to least are: [68.0, 63.0, 56.0, 56.0, 46.0, 45.0, 45.0, 32.0, 32.0, 31.0, 24.0, 12.0]
##The amount of values above freezing are 7
##The amount of values below freezing are 5

##How many test are there? Test = 7
##What are the temperatures (In Fahrenheit): 213
##What are the temperatures (In Fahrenheit): -342
##What are the temperatures (In Fahrenheit): 123
##What are the temperatures (In Fahrenheit): 434
##What are the temperatures (In Fahrenheit): -405
##What are the temperatures (In Fahrenheit): 749
##What are the temperatures (In Fahrenheit): -206
##The maximum value of the index is: 749.0
##The minimum value of the index is: -405.0
##The average temperature from the index is: 80.9
##There are 4 temperature values above the average
##The standard deviation of the data is: 425.7
##The median temperature value is: 123.0
##The given vaues sorted from least to greatest are: [-405.0, -342.0, -206.0, 123.0, 213.0, 434.0, 749.0]
##The given vaues sorted from greatest to least are: [749.0, 434.0, 213.0, 123.0, -206.0, -342.0, -405.0]
##The amount of values above freezing are 4
##The amount of values above freezing are 3
