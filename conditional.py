# if else & elif example

a=int(input("Enter your age: "))
if(a>=18):
    print("You are above the age of consent")
elif(a==0):
    print("You are entering zero age.")
elif(a<0):
    print("You are entering negatve age.")
else:
    print("You are below the age of consent")
print("End of the program")