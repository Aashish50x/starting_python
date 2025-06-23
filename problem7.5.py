# Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter the range of natural number : "))
sum1=0

for i in range (1,n+1):
    sum1=sum1+i

print(sum1)


# by while loop 
sum2=0
i=0
while(i<=n):
    sum2=sum2+i
    i+=1
print(sum2)