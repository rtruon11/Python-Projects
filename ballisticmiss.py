# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 2 2.0
# Date: 1/29/2018
# Title: BallisticMiss
# Description: User inputs initial velocity (feet per seconds) along with firing angle (degrees) and time (seconds),program prints x-position and y-position (in feet) of the projectilee

import math

initial_velocity = float(input('Enter initial velocity of ballistic missle: '))
firing_angle = float(input('Enter firing angle for ballistic missle: '))
time = float(input('Enter time of ballistic missle: '))

gravity = 32.2  # value of gravity

x_position = (initial_velocity * math.cos(firing_angle) * time)
y_position = (initial_velocity * (math.sin(firing_angle) * time)) - (0.5 * gravity * (math.pow(time,2)))

print ('Height:', x_position, 'feet', '\nDistance:', y_position, 'feet')

##Enter initial velocity of ballistic missle: 5
##Enter firing angle for ballistic missle: 45
##Enter time of ballistic missle: 2
##Height: 5.253219888177298 feet 
##Distance: -55.890964754658825 feet

##Enter initial velocity of ballistic missle: 3
##Enter firing angle for ballistic missle: 90
##Enter time of ballistic missle: 1
##Height: -1.3442208483875104 feet 
##Distance: -13.418010009198328 feet

##Enter initial velocity of ballistic missle: 7
##Enter firing angle for ballistic missle: 25
##Enter time of ballistic missle: 4
##Height: 27.75367873217726 feet 
##Distance: -261.30584900273766 feet
