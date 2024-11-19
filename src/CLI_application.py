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
                print('Password Manager\n')
                username = input('Please enter your Password Manager Username:  ')
                if not found_user(username):
                    
                    print(RED + '\nUser does not exists' + RESET + '\n\nPress Enter to continue')
                    next = input()
                    
                else:
                    
                    password = input('\nPlease enter your Password Manager Password:  ')
                    
                    if login(username, password):
                        
                        while True:
                            os.system('cls')
                            print('Password Manager\n')
                            print(GREEN + f'{username} logged in successfully\n' + RESET)
                            print('  Options:\n')
                            print('    1. Get Password')
                            print('    2. Add Password')
                            print('    3. Logout')
                            try:
                                user_menu_choice = int(input('\nPlease select an option from the menu above:  '))
                                
                                if user_menu_choice == 1:
                                    os.system('cls')
                                    print('Password Manager')
                                    retrieve_passwords(username)
                                
                                elif user_menu_choice == 2:
                                    os.system('cls')
                                    print('Password Manager')
                                    service = input('\nPlease enter the name of the Service you want to save a password for:  ')
                                    service_username = input(f'\nWhat username do you use for {service}:  ')
                                    service_password = input(f'\nWhat password do you use for {service}:  ')
                                    
                                    add_password(username, service, service_username, service_password)
                                
                                elif user_menu_choice == 3:
                                    break
                                
                                else:
                                    
                                    print(RED + '\nError: option not found' + RESET)
                                    print('\nPress Enter to return')
                                    input()
                                
                            except:
                                
                                print(RED + '\nError: invalid input' + RESET)
                                print('\nPress Enter to return')
                                input()
                        
                    else:
                        
                        print(RED + '\nPassword Incorrect\n' + RESET + '\nPress Enter to continue')
                        input()
                
            elif main_menu_choice == 2:
                
                os.system('cls')
                print('Password Manager\n')
                print('Create New User\n')
                username = input('Please enter a Username for the Password Manager:  ')
                
                if found_user(username):
                    
                    print(RED + '\nSorry this user name is taken' + RESET)
                    print('\nPress Enter Return to Main Menu')
                    input()
                
                else:
                    
                    password = input('\nPlease enter a Password for the Password Manager:  ')
                    create_user(username, password)
                    print('\nPress Enter Return to Main Menu')
                    input()
                
            elif main_menu_choice == 3:
                
                print('\nExiting application, goodbye')
                for i in range(3):
                    print('.', end='')
                    time.sleep(0.5)
                os.system('cls')
                break
            
            else:
                
                print(RED + '\nError: invalid input, press Enter to continue' + RESET)
                input()
                
        except:
            
            print(RED + '\nError: invalid input, press Enter to continue' + RESET)
            input()

if __name__ == '__main__':
    main()