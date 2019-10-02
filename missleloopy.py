# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 4
# Date: 02/15/2018
# Title: missleloopy
# Description: User enters fahrenheit start value and increasing value and ending value, program converts to centigrade

import math

y_position = 0
time = 0

initial_velocity = float(input('Enter initial velocity of ballistic missle: '))
firing_angle = float(input('Enter firing angle for ballistic missle: '))
time_increment = float(input('Enter time increment of ballistic missle: '))

gravity = 32.2  # value of gravity

print ('Time           Distance                              Height')

while y_position >= 0:
    x_position = (initial_velocity * math.cos(firing_angle)) * (time)
    y_position = (initial_velocity * math.sin(firing_angle)) * (time) - (0.5 * gravity * (math.pow(time,2)))

    time = time + time_increment

    print (time,'         ', x_position, 'feet','                ', y_position, 'feet')

