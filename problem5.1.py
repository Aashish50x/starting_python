# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

a={
    "chaye" :'tea',
    'ghar':'home',
    'hva':'air',
    'pani':'water'
}

b=input("Enter the word you want to search:")
print(a[b])


# to add more inputs by user
c=input("Enter the word you want to add:")
d=input("Enter the word's meaning:")
a[c]=d
print(a)

