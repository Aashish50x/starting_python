# Write a program to find out whether a student has passed or failed if it 
# requires a total of 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

marks1=int(input("Enter your 1st subject marks: "))
marks2=int(input("Enter your 2nd subject marks: "))
marks3=int(input("Enter your 3rd subject marks: "))

outof=int(input("Enter your paper marks out of:"))


if((marks1/outof)*100<33 or (marks2/outof)*100<33 or (marks3/outof)*100<33):
    # or means that one of the state should be true then will be executed 
    print("Fail")
else:
    if(((marks1+marks2+marks3)/outof*3)*100<40):
        print("Fail")
    else:
        print("Pass")
        