# Write a python function to print multiplication table of a given number.

def table(s,i):
    if i==11:
        return None
    else:
        print(f"{s} X {i} = {s*i}")
        table(s,i+1)


s=int(input("Enter a number : "))
i=1
table(s,i)