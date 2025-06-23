# Write a python function which converts inches to cms.

def conversion(inch):
    cms=inch*2.54
    return cms

inch=int(input("Enter distance in inch : "))
print(f"{conversion(inch)} cm")
