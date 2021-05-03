import random 

print("""********** Number Gausing Game Project *********""")
while(1):
  min,max=map(int,input("Enter min and max no. in which you want to gauss : ").split())
  if(max<=min):
    print("you Entered value in wrong order.. please enter again in correct order...")
  else:
    break

result=random.randint(min,max)

while(1):
  number=int(input("Enter the gaussing number : "))
  if(number==result):
    print("You gaused right..","gaussed no. is : ",number)
    break
  elif(number>result):
    print("You are to high.. ")
  else:
    print("you are two low...")
  



