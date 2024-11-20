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
            
            main_menu_choice = int(input('\nPlease Select an Option from the Menu Above:  '))
            
            if main_menu_choice == 1:
                
                os.system('cls')
                print('Password Manager\n')
                print('  Please Enter Your Login credentials\n')
                username = input('  Username:  ')
                
                if login(username, master_password)
            
            elif main_menu_choice == 2:
                
                user_created = False
                
                while not user_created:
                    
                    os.system('cls')
                    print('Password Manager\n')
                    print(('  Please Enter a Username for the Password Manager\n\n  Or Press Enter to Return to the Main Menu\n'))
                    username = input('  Username:  ')
                    
                    if username == '':
                        
                        break
                    
                    elif found_user(username):
                        
                        print(RED + '\n  Sorry this username is taken' + RESET + '\n\n  Press Enter to Continue')
                        input()
                    
                    else:
                        
                        while True:
                            
                            os.system('cls')
                            print('Password Manager\n')
                            print(('  Please Enter a Master Password for the Password Manager\n\n  Or Press Enter to Return to the Main Menu\n'))
                            master_password = pwinput.pwinput(prompt='  Password:  ', mask='●')
                            
                            if master_password == '':
                                
                                break
                            
                            else:
                                
                                os.system('cls')
                                print('Password Manager\n')
                                print(('  Please confirm Master Password for the Password Manager\n'))
                                confirm_master_password = pwinput.pwinput(prompt='  Password:  ', mask='●')
                                
                                if master_password == confirm_master_password:
                                    
                                    create_user(username, master_password)
                                    os.system('cls')
                                    print('Password Manager\n')
                                    print((GREEN + f'  New user, {username}, created successfully'+ RESET + '\n\n  Press Enter to Return to the Main Menu\n'))
                                    input()
                                    user_created = True
                                    break
                                
                                else:
                                    
                                    print((RED + f'  Passwords do not match' + RESET + '\n\n  Press Enter to try again\n'))
                                    input()
                
            elif main_menu_choice == 3:
                
                print('\nExiting application', end='')
                time.sleep(0.5)
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