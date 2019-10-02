#Name: Richard Truong
#Date: 03/29/18
#COMPSCI 121

student_grades = {    
      'Andrew' : [56, 79, 90, 22, 50],   
      'Colin' : [88, 62, 68, 75, 78],
      'Alan' : [95, 88, 92, 85, 85],
      'Mary' : [76, 88, 85, 82, 90],
      'Tricia' : [99, 92, 95, 89, 99]
      }
avg = []
names = []
for name, grade in student_grades.items():
   # print (name, grade)
   avg.append(sum(grade)/len(grade))
   names.append(name)

max(avg)

print (avg)
print (names)
print ('The student with the max average is', names[avg.index(max(avg))])
assi_average1 = []
assi_average2 = []
assi_average3 = []
assi_average4 = []
assi_average = []

i = 0
test1_avg = 0
for k in range(len(student_grades)):
   for names, grade in student_grades.items():
      test1_avg += sum(student_grades[names][0+i:1+i])
   i += 1
   print(test1_avg/len(student_grades))
   test1_avg = 0
   
for name, grade in student_grades.items():
   highest_grade = []
   highest_grade.append(sum(student_grades[name]))
   i = 0
   
##curve = 500-max(highest_grade)
##for k in range(len(student_grades)):
##   for names, grade in student_grades.items():
##      student_grades[name][i] += curve/5
##   i +=1
##   
##print(student_grades)
##

##[59.4, 74.2, 89.0, 84.2, 94.8]
##['Andrew', 'Colin', 'Alan', 'Mary', 'Tricia']
##The student with the max average is Tricia
##82.8
##81.8
##86.0
##70.6
##80.4
