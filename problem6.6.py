# Write a program to calculate the grade of a student from his marks 
# from the following scheme:

marks=int(input("Enter your marks out of 100 : "))

if (marks<=100 and marks>=90):
    grade="Ex"
elif (marks>=80 and marks<90):
    grade="A"
elif (marks>=70 and marks<80):
    grade="B"
elif (marks>=60 and marks<70):
    grade="C"
elif (marks>=50 and marks<60):
    grade="D"
elif(marks<50 and marks>=0):
    grade="F"
else :
    grade="Invalid"
print("Your grade is : ", grade)
