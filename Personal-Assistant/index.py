#!/c/Users/Acer/anaconda3/python


import os
import pyttsx3


while(True):
    os.system("clear")
    print("      *********** Amanjeet Chat Bot ****************\n\n")
    user_choice = input(" Enter your Choice : ")
    user_choice=user_choice.lower()
    # print()
    # print(user_choice)



    if ("not" in user_choice) or ("don't" in user_choice) or ("donot" in user_choice) or ("dont" in user_choice):
        print("You dono't want to run or execute something..")
        pyttsx3.speak("You dono't want to run or execute something.. ")
        pyttsx3.speak("Press Enter to continue...")
        input("Press Enter to Continue...")



    elif ("run" in user_choice) or ("open" in user_choice) or ("execute" in user_choice):
        if "chrome" in user_choice:
            if os.system("chrome") == 1:
                print("'chrome' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "notepad" in user_choice:
            if os.system("notepad") == 1:
                print("'notepad' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "vs code" in user_choice or "vscode" in user_choice or "vs" in user_choice or "code" in user_choice or "vs-code" in user_choice or ". code" in user_choice:
            if os.system("code") == 1:
                print("'vs code' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "matlab" in user_choice:
            if os.system("matlab") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "vlc" in user_choice:
            if os.system("vlc") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "python" in user_choice or "python3" in user_choice:
            if os.system("python") == 1:
                print("'python' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "jupyter-notebook" in user_choice or "notebook" in user_choice or "jupyter" in user_choice:
            if os.system("jupyter-notebook") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "anaconda" in user_choice or "anaconda3" in user_choice or "conda" in user_choice:
            if os.system("anaconda3") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "pycharm" in user_choice or "pycharm3" in user_choice:
            if os.system("pycharm") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "media-player" in user_choice or "video-player" in user_choice or ("windows" in user_choice and "media" in user_choice and "player" in user_choice) or ("media" in user_choice and "player" in user_choice) or ("windows" in user_choice and "video" in user_choice and "player" in user_choice) or ("video" in user_choice and "player" in user_choice):
            if os.system("wmplayer") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "git" in user_choice:
            if os.system("git") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "firefox" in user_choice:
            if os.system("firefox") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "msexcel" in user_choice or ("ms" in user_choice and "excel" in user_choice) or "excel" in user_choice or "excel-sheet" in user_choice or "spreed-sheeh" in user_choice or ("excel" in user_choice and "sheet" in user_choice) or ("spread" in user_choice and "sheet" in user_choice) :
            if os.system("EXCEL") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "winword" in user_choice or "word" in user_choice or "ms-word" in user_choice or ("ms" in user_choice and "word" in user_choice) or ("document" in user_choice and "file" in user_choice) or "document" in user_choice:
            if os.system("WINWORD") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "power-point" in user_choice or "power-pnt" in user_choice or ("power" in user_choice and "point" in user_choice) or ("power" in user_choice and "pnt" in user_choice) or ("ppt" in user_choice and "file" in user_choice):
            if os.system("POWERPNT") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "winproj" in user_choice or ("project" in user_choice and "win" in user_choice) or ("ms" in user_choice and "project" in user_choice):
            if os.system("WINPROJ") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()


        if "visio" in user_choice or ("ms" in user_choice and "visio" in user_choice) or "diagram" in user_choice:
            if os.system("VISIO") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "outlook" in user_choice or "ms-outlook" in user_choice:
            if os.system("OUTLOOK") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "onenote" in user_choice or "ms-onenote" in user_choice or "microsoft-onenote" in user_choice:
            if os.system("ONENOTE") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "mspub" in user_choice or "pub" in user_choice or "publisher" in user_choice or "mspublisher" in user_choice:
            if os.system("MSPUB") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "msaccess" in user_choice or "access" in user_choice:
            if os.system("MSACCESS") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()


        if "lync" in user_choice or "skipe" in user_choice or "ms-skipe" in user_choice:
            if os.system("lync") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()


        if "edge" in user_choice or "msedge" in user_choice:
            if os.system("msedge") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "canva" in user_choice:
            if os.system("canva") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()


        if "canva" in user_choice:
            if os.system("canva") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "atom" in user_choice :
            if os.system("atom") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "sublime_text" in user_choice  or "sublime" in user_choice :
            if os.system("sublime_text") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()


        if ("control" in user_choice and "panel" in user_choice) or "control-panel" in user_choice or "control_panel" in user_choice or "settings" in user_choice:
            if os.system("Control") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "multisim" in user_choice :
            if os.system("multisim") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()


        if "gimp" in user_choice :
            if os.system("gimp-2.10") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "bracket" in user_choice :
            if os.system("Brakets") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "photoshop" in user_choice :
            if os.system("Photoshop") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()

        if "photoshop" in user_choice :
            if os.system("Photoshop") == 1:
                print("'matlab' is not recognized as an internal or external command, operable program or batch file.")
            print("\n Press Enter to continue...")
            pyttsx3.speak("\n Press Enter to continue...")
            input()


    x = input("To Exit from this program please write only 'yes' : ")
    x=x.lower()
    if x == "yes":
        break