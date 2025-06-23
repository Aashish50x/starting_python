# if we set default value then it will set default if there no argument will pass for 
# tha function

def name(name="Aashish"):
    print(f"My name is {name}")

# if we cannot pass anything then it will print default 
name()
# if we pass value then it cannot take default value 
name("abc")