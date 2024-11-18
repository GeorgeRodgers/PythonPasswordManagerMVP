from password_manager import *
from console_styling import *
import time
import os

def main():
    while True:
        os.system('cls')
        print('Password Manager\n')
        print('  Options:\n')
        print('    1. Login')
        print('    2. Create New User')
        print('    3. Exit Password Manager')
        try:
            main_menu_choice = int(input('\nPlease select an option from the menu above:  '))
            
            if main_menu_choice == 1:
                
                os.system('cls')
                username = input('Please enter your Password Manager Username:  ')
                password = input('Please enter your Password Manager Password:  ')
                
            elif main_menu_choice == 2:
                
                os.system('cls')
                print('Password Manager\n')
                print('Create New User\n')
                username = input('Please enter a Username for the Password Manager:  ')
                password = input('Please enter a Password for the Password Manager:  ')
                
                create_user(username, password)
                print('\nReturning to Main Menu')
                time.sleep(2)
                os.system('cls')
                
            elif main_menu_choice == 3:
                print('Exiting application, goodbye')
                time.sleep(2)
                os.system('cls')
                break
            else:
                os.system('cls')
                print(RED + 'Error: option not found' + RESET)
        except:
            print(RED + 'Error: invalid input' + RESET)
            time.sleep(2)
            os.system('cls')

if __name__ == '__main__':
    main()