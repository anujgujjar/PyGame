import random
def main():
  print("===========================================")
  print("username--->")
  username=input("enter your name \n")
  print("Author : ",username)
  print("game.py will accept user and provide some games for fun\n")
  print("===========================================")
  game()

def game():
  selectOption = (input("Please select your Game -->\n A) Dice Rolls \n B) Hide and Seek \n C) Secret Prize \n D) War Card Game\n E) Heads or Tails \n F) Rock, Paper, Scissors \n")) 

  if (selectOption == "A" or selectOption == "a"):
    
    choice_game = 'Dice Rolls'
    computerPoint=0
    userPoint=0
    x=5 #points min required to win game 
        # importing required random module
    while True:
      print("Welcome in your Game",choice_game)
      print("Now please enter your choice no. \n")
    # take the input from user
      ch = int(input("Now Your turn: "))
      while ch> 6 or ch< 1:
         ch = int(input("Enter your valid input here: "))
    # print user given choice
      print("Your choice is: " ,ch)
      print("\n Now its computer turn to initiate....")
  # Computer will select randomly any number
  # among values 1, 2 and 3. Using randint method
  # of random module
      comp_choice = random.randint(1, 6)
  # looping will continue until comp_choice value
  # is equal to the choice value
      while comp_choice == ch:
        comp_choice = random.randint(1,6)
    # initialize value of the variable comp_choice_name
    # variable corresponding to the choice value
      print("computer choice is: " ,comp_choice)
      print(ch , " V/s " , comp_choice)
  # condition for winning the game
      if(ch>comp_choice):
          print("You are the win 1 point-> ",end = " ")
          (userPoint+1)
      else:
        print("Computer win 1 point ->",end = " ")
        (computerPoint+1)
      if(userPoint>=x):  
        print("you are winner of game" )
      elif computerPoint>=x:
        print("Computer are winner of game" )
      else :
        print("\nMax point required to win game is : ",x,"\nplease play upto ",x , "times\n")
      print("Do you want to play again? (Y/N)")
      ans = input()
      # if user input n or N then condition is True
      if ans == 'n' or ans == 'N':
         break
   # after exiting from the while loop
    print("\nThanks for sharing time with us...")
    print("Do you want to play another game? (Y/N)")
    ans1 = input()
    if ans1 == 'n' or ans1 == 'N':
       main()
    else:
       game()

  if (selectOption == "B" or selectOption == "b"):
    choice_game = 'Hide and Seek' 
    computerPoint=0
    userPoint=0
    x=5 #points min required to win game 
    while True:
      print("Welcome in your Game",choice_game)
      print("Now please enter your choice no. \n 1. LeftHand  \n 2. RightHand \n")
  # take the input from user
      ch = int(input("Now Your turn: "))
      while ch> 2 or ch< 1:
         ch = int(input("Enter your valid input here: "))
      if ch == 1:
         choice_name = 'LeftHand'
      else :
         choice_name = 'RightHand'
  # print user given choice
      print("Your choice is: " + choice_name)
      print("\nNow its computer turn to initiate....")
  # Computer will select randomly any number
  # among values 1 and 2. Using randint method
  # of random module
      comp_choice = random.randint(1, 2)
  # looping will continue until comp_choice value
  # is equal to the choice value
    # initialize value of the variable comp_choice_name
    # variable corresponding to the choice value
      if comp_choice == 1:
         comp_choice_name = 'LeftHand'
      else :
         comp_choice_name = 'RightHand'
      print("computer choice is: " + comp_choice_name)
  # condition for winning the game
      if(ch==comp_choice):
          print("\nYou are the win 1 point->-> ",end = " ")
          (userPoint+1)
      else:
          print("\nComputer win 1 point ->\n",end = " ")
          (computerPoint+1)
      if(userPoint>=x):  
        print("you are winner of game" )
      elif computerPoint>=x:
        print("Computer are winner of game" )
      else :
        print("\nMax point required to win game is : ",x,"\nplease play upto ",x , "times\n")
      print("Do you want to play again? (Y/N)")
      ans = input()
      # if user input n or N then condition is True
      if ans == 'n' or ans == 'N':
         break
    # after exiting from the while loop
    print("\nThanks for sharing time with us...")
    print("Do you want to play another game? (Y/N)")
    ans1 = input()
    if ans1 == 'n' or ans1 == 'N':
      main()
    else:
      game()

  if (selectOption == "C" or selectOption == "c"):
    choice_game = 'Secret Prize'
    computerPoint=0
    userPoint=0
    x=5 #points min required to win game 
    while True:
      print("Welcome in your Game",choice_game)
      print("Now please enter your choice no. \n 1. Laptop \n 2. Mobile \n 3. Car \n")
  # take the input from user
      ch = int(input("Now Your turn: "))
      while ch> 3 or ch< 1:
        ch = int(input("Enter your valid input here: "))
      if ch == 1:
        choice_name = 'Laptop'
      elif ch == 2:
        choice_name = 'Mobile'
      else:
        choice_name = 'Car'
  # print user given choice
      print("Your choice is: " + choice_name)
      print("\nNow its computer turn to initiate....")
  # Computer will select randomly any number
  # among values 1, 2 and 3. Using randint method
  # of random module
      comp_choice = random.randint(1, 3)
  # looping will continue until comp_choice value
  # is equal to the choice value
    # initialize value of the variable comp_choice_name
    # variable corresponding to the choice value
      if comp_choice == 1:
        comp_choice_name = 'Laptop'
      elif comp_choice == 2:
        comp_choice_name = 'Mobile'
      else :
          comp_choice_name = 'Car'
      print("computer choice is: " + comp_choice_name)
  # condition for winning the game
      if(ch == comp_choice):
        print(" You are the win 1 point-> ")
        (userPoint+1)
      else :
        print(" Computer win 1 point " )
        (computerPoint+1)
      if(userPoint>=x):  
        print("you are winner of game" )
      elif computerPoint>=x:
        print("Computer are winner of game" )
      else :
        print("\nMax point required to win game is : ",x,"\nplease play upto ",x , "times\n")
      print("Do you want to play again? (Y/N)")
      ans = input()
      # if user input n or N then condition is True
      if ans == 'n' or ans == 'N':
        break
   # after exiting from the while loop
    print("\nThanks for sharing time with us...")
    print("Do you want to play another game? (Y/N)")
    ans1 = input()
    if ans1 == 'n' or ans1 == 'N':
      main()
    else:
      game()

  if (selectOption == "D" or selectOption == "d"):
    choice_game = 'War Card Game'
    computerPoint=0
    userPoint=0
    x=5 #points min required to win game 
    while True:
      print("Welcome in your Game",choice_game)
      print("Now please enter your choice no. \n")
    # take the input from user
      ch = int(input("Now Your turn: "))
      while ch> 13 or ch< 1:
        ch = int(input("Enter your valid input here: "))
  # print user given choice
      print("Your choice is: " ,ch)
      print("\n Now its computer turn to initiate....")
  # Computer will select randomly any number
  # among values 1, 2 and 3.....upto 13. Using randint method
  # of random module
      comp_choice = random.randint(1, 13)
  # looping will continue until comp_choice value
  # is equal to the choice value
      while comp_choice == ch:
        comp_choice = random.randint(1,13)
    # initialize value of the variable comp_choice_name
    # variable corresponding to the choice value
      print("computer choice is: " ,comp_choice)
      print(ch , " V/s " , comp_choice)
  # condition for winning the game
      if(ch>comp_choice):
        print("You are the win 1 point->-> ",end = " ")
        (userPoint+1)
      else:
        print("Computer win 1 point->",end = " ")
        (computerPoint+1)
      if(userPoint>=x):  
        print("you are winner of game" )
      elif computerPoint>=x:
        print("Computer are winner of game" )
      else :
        print("\nMax point required to win game is : ",x,"\nplease play upto ",x , "times\n")
      print("Do you want to play again? (Y/N)")
      ans = input()
      # if user input n or N then condition is True
      if ans == 'n' or ans == 'N':
        break
   # after exiting from the while loop
    print("\nThanks for sharing time with us...")
    print("Do you want to play another game? (Y/N)")
    ans1 = input()
    if ans1 == 'n' or ans1 == 'N':
      main()
    else:
      game()

  if (selectOption == "E" or selectOption == "e"):
    choice_game = 'Heads or Tails'
    computerPoint=0
    userPoint=0
    x=5 #points min required to win game 
    while True:
      print("Welcome in your Game",choice_game)
      print("Now please enter your choice no. \n 1. Heads  \n 2. Tails \n")
  # take the input from user
      ch = int(input("Now Your turn: "))
      while ch> 2 or ch< 1:
        ch = int(input("Enter your valid input here: "))
      if ch == 1:
        choice_name = 'Heads'
      else :
        choice_name = 'Tails'
  # print user given choice
      print("Your choice is: " + choice_name)
      print("\nNow its computer turn to initiate....")
  # Computer will select randomly any number
  # among values 1 and 2. Using randint method
  # of random module
      comp_choice = random.randint(1, 2)
  # looping will continue until comp_choice value
  # is equal to the choice value
    # initialize value of the variable comp_choice_name
    # variable corresponding to the choice value
      if comp_choice == 1:
         comp_choice_name = 'Heads'
      else :
        comp_choice_name = 'Tails'
      print("computer choice is: " + comp_choice_name)
  # condition for winning the game
      if(ch==comp_choice):
        print("\nYou are the win 1 point->-> ",end = " ")
        (userPoint+1)
      else:
        print("\nComputer win 1 point ->\n",end = " ")
        (computerPoint+1)
      if(userPoint>=x):  
        print("you are winner of game" )
      elif computerPoint>=x:
        print("Computer are winner of game" )
      else :
        print("\nMax point required to win game is : ",x,"\nplease play upto ",x , "times\n")
      print("Do you want to play again? (Y/N)")
      ans = input()
      # if user input n or N then condition is True
      if ans == 'n' or ans == 'N':
        break
   # after exiting from the while loop
    print("\nThanks for sharing time with us...")
    print("Do you want to play another game? (Y/N)")
    ans1 = input()
    if ans1 == 'n' or ans1 == 'N':
      main()
    else:
      game()
  if (selectOption == "F" or selectOption == "f"):
    choice_game = 'Rock, Paper, Scissors'
    computerPoint=0
    userPoint=0
    x=5 #points min required to win game 
    while True:
      print("Welcome in your Game",choice_game)
      print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
  # take the input from user
      ch = int(input("Now Your turn: "))
      while ch> 3 or ch< 1:
         ch = int(input("Enter your valid input here: "))
      if ch == 1:
         choice_name = 'Rock'
      elif ch == 2:
         choice_name = 'paper'
      else:
         choice_name = 'scissor'
  # print user given choice
      print("Your choice is: " + choice_name)
      print("\nNow its computer turn to initiate....")
  # Computer will select randomly any number
  # among values 1, 2 and 3. Using randint method
  # of random module
      comp_choice = random.randint(1, 3)
  # looping will continue until comp_choice value
  # is equal to the choice value
      while comp_choice == ch:
        comp_choice = random.randint(1,3)
    # initialize value of the variable comp_choice_name
    # variable corresponding to the choice value
      if comp_choice == 1:
         comp_choice_name = 'Rock'
      elif comp_choice == 2:
         comp_choice_name = 'paper'
      else:
         comp_choice_name = 'scissor'
      print("computer choice is: " + comp_choice_name)
      print(choice_name + " V/s " + comp_choice_name)
  # condition for winning the game
      if((ch == 1 and comp_choice == 2) or
         (ch == 2 and comp_choice ==1 )):
          print("paper wins-> ",end = " ")
          final_result = "paper"
      elif((ch == 1 and comp_choice == 3) or
         (ch == 3 and comp_choice == 1)):
        print("Rock wins ->",end = " ")
        final_result = "Rock"
      else:
         print("scissor wins ->",end = " ")
         final_result = "scissor"
  # Printing either user or computer wins
      if final_result == choice_name:
         print(" You are the win 1 point-> ",end = " ")
         (userPoint+1)
      else:
         print(" Computer win 1 point " )
         (computerPoint+1)
      if(userPoint>=x):  
        print("you are winner of game" )
      elif (computerPoint>=x):
        print("Computer are winner of game" )
      else :
        print("\nMax point required to win game is : ",x,"\nplease play upto ",x , "times\n")
      print("Do you want to play again? (Y/N)")
      ans = input()
        # if user input n or N then condition is True
      if ans == 'n' or ans == 'N':
        break
    print("\nThanks for sharing time with us...")
    print("Do you want to play another game? (Y/N)")
    ans1 = input()
    if ans1 == 'n' or ans1 == 'N':
     main()
    else:
     game()
main() 


