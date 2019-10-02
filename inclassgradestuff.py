# grades

ngrades = int(input('Enter number of grades '))
sum = 0.0
numA = 0.0
numB = 0.0

#maxgrade = -9999 alternate method
#mingrade = 9999 alternate method

for i in range(ngrades):
    grade = float(input('Input grade '))
    sum = sum + grade
    if i == 0:
        maxgrade = grade
        mingrade = grade
    if grade > maxgrade:
        maxgrade = grade
    if grade < mingrade:
        mingrade = grade
    if grade >= 90:
        numA = numA + 1
    elif (grade >= 80):
        numB = numB + 1

average = sum / ngrades

print ('Average is %.2f ' % average)
print ('Max grade is %.2f ' % maxgrade)
print ('Min grade is %.2f ' % mingrade)
print ('Number of A grades = %d ' % numA)
print ('Number of B grades = %d ' % numB)
