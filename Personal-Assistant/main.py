import pyttsx3
import os

while(1):
    os.system('clear')
    
    print("""      ************* Menu Program ************
    
             press 1 : To open google chrome
             press 2 : To open notepad
             press 3 : To open Matlab
             press 4 : To Exit
             press 5 : Ms-office
    
    """)
    
    user_choice = int(input(" what do you want to run : "))
    
    if user_choice == 1:
        if os.system("chrome")==1:
            print("'chrome' is not recognized as an internal or external command, operable program or batch file.")
        print("\n Press Enter to continue...")
        pyttsx3.speak("\n Press Enter to continue...")
        input()
            
    elif user_choice == 2:
        if os.system("notepad")==1:
            print("'notepad' is not recognized as an internal or external command, operable program or batch file.")
        pyttsx3.speak("\n Press Enter to continue...")
        input("\n Press Enter to continue...")
            
    elif user_choice == 3:
        if os.system("matlab")==1:
            print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
        pyttsx3.speak("\n Press Enter to continue...")
        input("\n Press Enter to continue...")
            
    elif user_choice == 5:
        if os.system("msoffice")==1:
            print(" 'msoffice' is not recognized as an internal or external command, operable program or batch file.")
            pyttsx3.speak("'msoffice' is not recognized as an internal or external command, operable program or batch file.")

        pyttsx3.speak("\n Press Enter to continue...")
        input("\n Press Enter to continue...")
        
    else:
        break

