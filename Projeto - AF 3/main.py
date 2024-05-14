import os
import getpass
from my_functions import register, login
from pharmacy_menu import menu

## All Code
while True:
    try: 
        ## ---------------------------------------
        ## Initial Menu
        print(f"======[4Disease Pharmacy]======")
        print(f"1. Login")
        print(f"2. Register")
        print(f"3. Exit\n")
        
        option_choice = int(input("Option: "))
        print(f"===============================")
        ## ---------------------------------------

        ## ---------------------------------------
        ## Customer Decision Path
        if option_choice == 1:
            print(f"Option: Login\n")

            input("Press Enter to Continue...")
            os.system("cls")

            print(f"====================")
            username = input(f"Username: ")
            password = getpass.getpass(f"Password: ")
            print(f"====================\n")
            user = login(username, password)
                                
            if user:
                print(f"Logged with Sucess.")
                input("Press Enter to Continue...")
                os.system("cls")
                menu(user)
            else:
                print(f"Username or Password Incorrect.")
                input("Press Enter to Continue...")
                os.system("cls")
        ## ---------------------------------------
        ## Employee Decision Path
        elif option_choice == 2:
            print(f"Option: Register\n")

            input("Press Enter to Continue...")
            os.system("cls")

            print(f"====================")
            r_username = input(f"Username: ")
            r_password = getpass.getpass(f"Password: ")
            print(f"====================\n")

            register(r_username, r_password)

            print(f"Registered with Sucess.")
            input("Press Enter to Continue...")
            os.system("cls")
        ## ---------------------------------------

        ## ---------------------------------------
        ## Exit Code
        elif option_choice == 3:
            input("Press Enter to Continue...")
            os.system("cls")
            break
        ## ---------------------------------------

        ## ---------------------------------------
        ## Error Message
        else:
            print(f"Invalid Option. Please type Again.")
            input("Press Enter to Continue...")
            os.system("cls")
        ## ---------------------------------------
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        print(f"===============================")
        input("Press Enter to Continue...")
        os.system("cls")