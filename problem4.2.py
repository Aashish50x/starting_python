# Write a program to accept marks of 6 students and display them in a sorted 
# manner

marks = []
print("enter the marks of student:")
m=int(input())  # 1
marks.append(m)
m=int(input())  # 2
marks.append(m)
m=int(input())  # 3
marks.append(m)
m=int(input())  # 4
marks.append(m)
m=int(input())  # 5
marks.append(m)
m=int(input())  # 6
marks.append(m)

marks.sort()
print(marks)