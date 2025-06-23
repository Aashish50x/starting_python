# Write a program to calculate the factorial of a given number using for loop.
# example = 5! = 5*4*3*2*1

n=int(input("Enter the number : "))
factorial=1

for i in range(1,n+1):
    factorial=factorial*i

print(factorial)
print(f"factorial of {n} is {factorial}.")