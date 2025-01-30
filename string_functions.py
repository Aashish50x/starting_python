# using string functions
a = "Aashish Kumar"
print(a)

# To find length
print(len(a))

# checking that the string is ends with given char/value 
print(a.endswith("ar"))  # gives true or false

# checking that the string is start with given char/value 
print(a.startswith("Aa")) 

b = "aashish"
# lets capitalize the string 
print(b.capitalize())  # capitalize the first word of string


# 1. Changing Case
s = "hello World"
print(s.upper())   # "HELLO WORLD"
print(s.lower())   # "hello world"
print(s.title())   # "Hello World"
print(s.capitalize()) # "Hello world"
print(s.swapcase())   # "HELLO wORLD" swap upper case to lower and vise versa

# 2. Checking String Properties
s = "Python123"
print(s.isalpha())   # False (contains numbers)
print(s.isdigit())   # False (contains letters)
print(s.isalnum())   # True  (letters + numbers)
print(s.isspace())   # False (not just spaces)
print(s.islower())   # False (has uppercase letters)
print(s.isupper())   # False (has lowercase letters)


# 3. Finding & Replacing
s = "Hello, world!"
print(s.find("world"))   # 7 (index of "world")  it raises -1 of not found
print(s.index("world"))  # 7 (same as find, but raises error if not found)
print(s.replace("world", "Python"))  # "Hello, Python!"


# 4. Splitting & Joining
s = "apple,banana,orange"
print(s.split(","))  # ['apple', 'banana', 'orange']

words = ["Python", "is", "awesome"]
print(" ".join(words))  # "Python is awesome"


# 5. Stripping Whitespaces
s = "   hello   "
print(s.strip())   # "hello"  (removes spaces from both ends)
print(s.lstrip())  # "hello   " (left strip)
print(s.rstrip())  # "   hello" (right strip)


# 6. Formatting Strings
name = "Aashish"
age = 19
print(f"My name is {name} and I am {age} years old.")  # f-string method
print("My name is {} and I am {} years old.".format(name, age))  # format method
print("My name is %s and I am %d years old." % (name, age))  # Old method


# 7. Counting & Checking Start/End
s = "banana"
print(s.count("a"))  # 3 (counts occurrences of "a")
print(s.startswith("ban"))  # True
print(s.endswith("na"))  # True

# replace 
p = "I am leaning python."
print(p.replace("I am","We are")) #replace 'i am' by 'we are' 