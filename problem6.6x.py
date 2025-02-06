# Write a program to calculate the grade of a student from his marks 
# from the following scheme:

marks=int(input("Enter your marks out of 100 : "))

if (marks>90):
    print("Student grade is : Ex")
elif (80<marks<=90):
    print("Student grade is : A")
elif (70<marks<=80):
    print("Student grade is : B")
elif (60<marks<=70):
    print("Student grade is : C")
elif (50<=marks<=60):
    print("Student grade is : D")
else:
    print("Student is Fail")
