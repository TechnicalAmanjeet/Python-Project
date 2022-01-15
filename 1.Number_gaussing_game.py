import random 
import os

def gauss(min,max):

  result=random.randint(min,max)
  while(1):
    try:
      number = int(input(f"\n Enter the gaussing number beetween {min} & {max} : "))
      break
    except:
      print("\n please enter integer value only...")
  while(1):

    if(number==result):
      print("\nYou gaused right..","gaussed no. is : ",number)
      input("\n please press enter to go ahead...")
      break
    elif(number>result):
      while (1):
        try:
          number = int(input(f"\n {number} is too high. guess again : "))
          break
        except:
          print("\n please enter integer value only...")

    else:
      while (1):
        try:
          number = int(input(f"\n{number} is too low. guess again : "))
          break
        except:
          print("\n please enter integer value only...")

def computer_gauss(user_min,user_max):
  while(1):
    gauss_by_computer = random.randint(user_min,user_max)
    user_choice = input(f"\n Gauss by computer : {gauss_by_computer}. is it too low (l) or too high (h) or correct (c) : ")

    if(user_choice.upper()=='L'):
      user_min = gauss_by_computer+1
    elif(user_choice.upper()=='H'):
      user_max = gauss_by_computer-1
    elif(user_choice.upper()=='C'):
      print(f"\n Yey! computer has gaussed your number.. you gaussed {gauss_by_computer}.. ")
      input("\n please press enter to go ahead...")
      break



while(1):
  os.system("clear")
  os.system("clear")
  print("""        ********** Number Gausing Game Project *********
  
  
   Press 1 : if you want to gauss no. beetween by default no... 
   Press 2 : if you want to gauss no. beetween your choice...
   Press 3 : if you have a guessed no. and computer has to guess b/w ( 1-100 )...
   Press 4 : if you have a gaussed no. and computer has to gauss b/w given by you lower and higher bound...
   Press 5 : to exit from Program...
    
  """)

  while (1):
    try:
      ch= int(input("\nEnter your choice : "))
      break
    except:
      print("\n please enter integer value only...")

  if(int(ch)==1):
    gauss(1,100)
  elif(int(ch)==2):
    while(1):
      # min,max=map(int,input("Enter min and max no. in which you want to gauss : ").split())
      while (1):
        try:
          min = int(input("Enter Minimum number in which you want to gauss : "))
          break
        except:
          print("\n please enter integer value only...")

      while (1):
        try:
          max = int(input("Enter Maximum number in which you want to gauss : "))
          break
        except:
          print("\n please enter integer value only...")

      if(max<=min):
        print("\nyou Entered value in wrong order.. please enter again in correct order...")
      else:
        gauss(min,max)
        break
  elif(ch==3):
    print("\n gauess a number beetween 1-100 in you mind... ")
    input("\n press enter to continue... ")
    computer_gauss(1,100)

  elif(ch==4):
    # print("\n Gauss a number in your mind... ")
    input("\n Gauss a number in your mind and press enter to continue...")
    lower = int(input("\n Enter your lower bound : "))
    heigher = int(input("\n Enter your heigher bound : "))
    print(f"\n You have gauessed a number beetween {lower}-{heigher} in your mind... ")
    input("\n press enter to continue... ")
    computer_gauss(lower,heigher)


  elif(int(ch)==5):
    break
  else:
    print("\nyou have entered wrong choice.. please read carefully and then enter : ")
    input("\n Type enter to go ahead...")










