# Write a program to find whether a given number is prime or not. 

a=int(input("Enter the number : "))

if a<=1:
    print("number is not prime below 2.")

for i in range(2,a):
    if(a%i)==0:
        print("The given number is not prime.")
        break
    else:
        print("The number is prime.")
        break