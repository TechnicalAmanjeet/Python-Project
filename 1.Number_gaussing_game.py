import random 
import os

def gauss(min,max):
  result=random.randint(min,max)
  while(1):
    number=int(input(f"Enter the gaussing number beetween {min} & {max} :"))
    if(number==result):
      print("\nYou gaused right..","gaussed no. is : ",number)
      input("\n please press enter to go ahead...")
      break
    elif(number>result):
      print("\nYou are to high.. ")
      max=number
    else:
      print("\nyou are two low...")
      min=number


while(1):
  os.system("clear")
  print("""********** Number Gausing Game Project *********\n\n""")

  print("1. Do you want to gauss no. beetween by default no... ")
  print("2. or Do you want to gauss no. beetween your choice...")
  print("3. Type 3 to exit...")
  ch= input("\nEnter your choice : ")

  if(int(ch)==1):
    gauss(1,100)
  elif(int(ch)==2):
    while(1):
      min,max=map(int,input("Enter min and max no. in which you want to gauss : ").split())
      if(max<=min):
        print("\nyou Entered value in wrong order.. please enter again in correct order...")
      else:
        gauss(min,max)
        break
      
  elif(int(ch)==3):
    break
  else:
    print("\nyou have entered wrong choice.. please read carefully and then enter : ")
    input("\n Type enter to go ahead...")










