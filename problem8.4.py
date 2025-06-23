# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n==1:
        return n
    else:
        return n+sum(n-1)
    
n1=int(input("Enter natural number : "))
print(sum(n1))
