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
    print(f"\n user choice : {user_choice} and computer choice : {compter_choice}.")
    if user_choice == compter_choice:
        return "tie"

    # r>s , s>p , p>r
    elif win(user_choice,compter_choice):
        return "won"

    else:
        return "lost"



if __name__=="__main__":
    while 1:
        os.system("clear")
        print("""       *********** Rock , Paper and Scisser Game. ************

    Press 1. To Play Game .
    Press 2. To Play Game as a series of your choice.
    Press 3. To Exit.
            """)

        user_choice = int(input("\n Enter your choise : "))
        if user_choice == 1 :
            if playgame() == "tie":
                print("\n It's a tie...")
            elif playgame() == "won":
                print("\n Yey! you won the game...")
            else:
                print("\n Ooh! you lost. Better luck next time")

        elif user_choice==2:

            game_count = int(input("\n How many times do you want to play this game : "))
            total_count = 1
            total = game_count
            user = 0
            computer = 0
            tie = 0
            while game_count:
                os.system("clear")
                print("""       *********** Rock , Paper and Scisser Game. ************

                            """)
                print(f"\n Score : game ({total_count}/{total}) , user_won : {user} , user_lost : {computer} and tie : {tie}.")
                n = playgame()
                if n == "tie":
                    print("\n It's a tie...")
                    tie=tie+1
                elif n == "won":
                    user=user+1
                    print("\n Yey! you won the game...")
                else:
                    computer=computer+1
                    print("\n Ooh! you lost. Better luck next time")

                input("\n press enter to continue...")
                game_count=game_count-1
                total_count = total_count+1

            print(f"\n Score : Total game : {total_count-1} , user_won : {user} , user_lost : {computer} and tie : {tie}.")

            if user == computer :
                print("\n Oops! it's a tie!... ")
            elif user > computer :
                print("\n Yey You Won this series...")
            else:
                print("\n ooh! you lost this battle...")

            input("\n Press Enter to continue>>.")


        elif user_choice==3:
            print("\n Thank you so omuch for playing.. ")
            print("\n Press enter to continue...")
            break

        else:
            print("\n Oops! wrong choice please correct your choice..")
            input("\n Press Enter to continue...")

