import random
import os

def win(user,computer):
    if((user=='R' and computer=='S') or (user=='S' and computer=='P') or (user=='p' and computer=='R')):
        return 1

def playgame():
    array = ['r','p','s']
    compter_choice = random.choice(array).upper()
    user_choice = input("\n Your Choice? Rock ('r') , Paper ('p') and Scisser ('s') : ")
    user_choice=user_choice.upper()

    if user_choice == compter_choice:
        print("\n It's a tie...")

    # r>s , s>p , p>r
    elif win(user_choice,compter_choice):
        print("\n wow! you won...")

    else:
        print("\n OHh! You lost...")

    print(f"\n user choice : {user_choice} and computer choice : {compter_choice}.")

    input("\n Press enter key to continue...")
    return

if __name__=="__main__":
    while 1:
        os.system("clear")
        print("""       *********** Rock , Paper and Scisser Game. ************

    Press 1. To Play Game.
    Press 2. To Exit.
            """)

        user_choice = int(input("\n Enter your choise : "))
        if user_choice == 1 :
            playgame()
        elif user_choice==2:
            break

        else:
            print("\n Oops! wrong choice please correct your choice..")
            input("\n Press Enter to continue...")

