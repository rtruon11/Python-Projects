# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 03/01/2018
# Title: functionstemp
# Description: code 1 converts fahrenheit to centigrade, code 2 converts centigrade to fahrenheit, code 3 prints instructions, code 4 exits program 

while 1==1:

    def F2C (degF):
        degC = (degF-32) * (5/9)
        return degC

    def C2F (degC):
        degF = (degC*(9/5)+32)
        return degF

    def instructions():
        print ('This program converts temperature readings from Centigrade to Fahrenheit.')
        print ('Please enter the numeric code to determine the operation.')
        print ('Code = 1 Convert Fahrenheit to Centigrade')
        print ('Code = 2 Convert Centigrade to Fahrenheit')
        print ('Code = 3 Display Instructions')
        print ('Code = 4 Quit')

    code = int(input('Code number: '))

    if (code == 1):
        degF = float(input('Enter degrees Fahrenheit '))
        degC = F2C (degF)
        print ('degrees C = ', degC)

    if (code == 2):
        degC = float(input('Enter degress Centigrade '))
        degF = C2F (degC)
        print ('degrees F = ', degF)
        
    if (code == 3):
        instructions ()

    if (code == 4):
        quit()

##Code number: 1
##Enter degrees Ferinheit 40
##degrees C =  4.444444444444445

##Code number: 2
##Enter degress Centigrade 4.444444444444445
##degrees F =  40.0

##Code number: 3
##This program converts temperature readings from Centigrade to Fahrenheit.
##Please enter the numeric code to determine the operation.
##Code = 1 Convert Fahrenheit to Centigrade
##Code = 2 Convert Centigrade to Fahrenheit
##Code = 3 Display Instructions
##Code = 4 Quit

##Code number: 4
