import random

import rules
import start_line

'''
1 = snake
2 = water
3 = gun
'''

def game(user):
 computer=random.choice(["s","w","g"])
 if computer==user:
  print("Match draw")
 else:
  if computer=="s" and user=="g":
   print("You win!")
  elif computer=="g" and user=="s":
   print("You lose!")
  elif computer=="w" and user=="g":
   print("You lose!")
  elif computer=="g" and user=="w":
   print("You win!")
  elif computer=="s" and user=="w":
   print("You lose!")
  elif computer=="w" and user=="s":
   print("You win!")
  elif user=="a":
   print("Succesfully stoped the game.\n")
   print("Returned to Home page .")
   start()
  else:
   print("Something went wrong.")
   print("Press any key to restart the game.")
   c=input("")
   start()
  print("Computer's choice was : ",computer)



def start_game():
 user=input("Enter your choice : ")
 game(user)



def start():
  start_line.starting_line()
  a=input("")

  if a=="1":
   play_mode()
  elif a=="2":
   rules.rules()
  elif a=="a":
   start()
  elif a=="exit" or a=="Exit" or a=="EXIT":
   print("Exited")
  else:
   print("Something went wrong")
   print("Press any key to restart.")
   b=input("")
   start()



def custom():
 print("choices can be: 2,3,5,10,20 only.")
 print("How much round : ")
 r_input=input("")
 print(f"Total rounds {r_input}.\n")
 if r_input=="2":
  for _ in range(2):
   start_game()
   print()
 elif r_input=="3":
  for _ in range(3):
   start_game()
   print()
 elif r_input=="5":
  for _ in range(5):
   start_game()
   print()
 elif r_input=="10":
  for _ in range(10):
   start_game()
   print()
 elif r_input=="20":
  for _ in range(20):
   start_game()
   print()
 elif r_input=="a":
  start()
 else:
  print("Please choose valid choice.")
  custom()
  print()



def play_mode():
 print('''
      How would you want to play...
      Press 1 for Single round.
      Press 2 for Custom round.
      Press 3 for Unlimited round.
       
       For Exit , type "exit" and enter.
''')
 mode_in=input("")
 if mode_in=="1":
  start_game()
 elif mode_in=="2":
  custom()
 elif mode_in=="3":
  print("Custom round has started.")
  print("for stop use 'stop' command.")
  i="0"
  while(i=="0"):
   start_game()
   i="0"
 elif mode_in=="stop":
  start()
 elif mode_in=="exit":
  print("Exited")   

 
  
start()
