# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 02/08/2018
# Title: graders
# Description: User inputs grade value, program outputs letter grade

grade = float(input('Enter grade value '))

if (grade < 60):
    print ('Grade is F')

elif (grade >= 60 and grade < 70):
    print ('Grade is D')

elif (grade >= 70 and grade < 80):
    print ('Grade is C')

elif (grade >= 80 and grade < 90):
    print ('Grade is B')

else:
    (grade >= 90 and grade <= 100)
    print ('Grade is A')

##Enter grade value 52.3
##Grade is F

##Enter grade value 69.1
##Grade is D

##Enter grade value 72.1
##Grade is C

##Enter grade value 84.5
##Grade is B

##Enter grade value 100
##Grade is A
