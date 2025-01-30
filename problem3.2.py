# print name and date in the letter 

# modern and advance method
name = input("Enter your name :")
date = input("Enter date :")
letter = ''' 
Dear |name|,
You are selected!
|date|'''
print(letter.replace("|name|", name ).replace("|date|",date))


name = input("Enter your name :")
date = input("Enter date :")
print(f"\nDear {name},\nYou are selected!\n{date}\n")


name = input("Enter your name :")
date = input("Enter date :")
print(f"""
      Dear {name},
      You are selected!
      {date}
      """)