# Write a python program using function to convert Celsius to Fahrenheit.

def temp(a):
    # c/5=(f-32)/9
    return (((f-32)/9)*5)

f=int(input("Enter temperature in Fehrenheit : "))
print(f"temperature in celsius is {temp(f)} C")
