# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 4
# Date: 02/15/2018
# Title: tempconversion
# Description: User enters fahrenheit start value and increasing value and ending value, program converts to centigrade

Fahrenheit = 0
Centigrade = 0

startFt = float(input('Enter start Fahrenheit value '))

incrFt = float(input('Enter increment value of Fahrenheit '))

endFt = float(input('Enter end Fahrenheit value '))

print ('Fahrenheit             Centigrade')

while Fahrenheit <= endFt:

    Centigrade = Fahrenheit + 32

    print (Fahrenheit,'                    ',Centigrade)

    Fahrenheit = Fahrenheit + incrFt

##Enter start Fahrenheit value 0
##Enter increment value of Fahrenheit 2
##Enter end Fahrenheit value 30
##Fahrenheit             Centigrade
##0                      32
##2.0                      34.0
##4.0                      36.0
##6.0                      38.0
##8.0                      40.0
##10.0                      42.0
##12.0                      44.0
##14.0                      46.0
##16.0                      48.0
##18.0                      50.0
##20.0                      52.0
##22.0                      54.0
##24.0                      56.0
##26.0                      58.0
##28.0                      60.0
##30.0                      62.0

##Enter start Fahrenheit value 2.5
##Enter increment value of Fahrenheit 1.4
##Enter end Fahrenheit value 20
##Fahrenheit             Centigrade
##0                      32
##1.4                      33.4
##2.8                      34.8
##4.199999999999999                      36.2
##5.6                      37.6
##7.0                      39.0
##8.4                      40.4
##9.8                      41.8
##11.200000000000001                      43.2
##12.600000000000001                      44.6
##14.000000000000002                      46.0
##15.400000000000002                      47.400000000000006
##16.8                      48.8
##18.2                      50.2
##19.599999999999998                      51.599999999999994

