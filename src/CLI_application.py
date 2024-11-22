from password_manager import *
from console_styling import *
import os, time, pwinput, pyperclip

def invalid_input():
    print(RED + '\nError: invalid input, press Enter to continue' + RESET)
    input()

def header():
    os.system('cls')
    print('Password Manager\n')

def main():
    while True:
        header()
        print('  Options:\n')
        print('    1. Login')
        print('    2. Create New User')
        print('    3. Exit Password Manager')
        try:
            
            main_menu_choice = int(input('\nPlease Select an Option from the Menu Above:  '))
            
            if main_menu_choice == 1:
                
                while True:
                    header()
                    print('  Password Manager Login\n\n  Press Enter to Return to the Main Menu\n')
                    username = input('\n\n  Username:  ')
                    
                    if username == '':
                        break
                    
                    elif not found_user(username):
                        
                        print(RED + f'\n  Sorry, account for {username} not found' + RESET + '\n\n  Press Enter to Continue')
                        input()
                    
                    elif found_user(username):
                        
                        attempts = 0
                        
                        while attempts < 3:
                            
                            if attempts > 0:
                                
                                header()
                                print('  Password Manager Login\n\n  Press Enter to Return to the Main Menu\n')
                                print(RED + f'  Password Incorrect, {3-attempts} attempts left' + RESET)
                                print(f'\n  Username:  {username}')
                            
                            attempts += 1
                            master_password = pwinput.pwinput(prompt='\n  Password:  ', mask='●')
                            
                            if master_password == '':
                                
                                break
                            
                            elif login(username, master_password):
                                
                                first_loop = True
                                
                                while True:
                                    
                                    accounts = list_accounts(username)
                                    header()
                                    
                                    if first_loop:
                                        
                                        print(GREEN + f'  User: {username}, Logged In'+ RESET + '\n\n  Accounts List\n')
                                    
                                    else:
                                        
                                        print('  Accounts List\n')
                                    
                                    for i in range(len(accounts)):
                                        
                                        print(f'    {i+1}. {get_account(username, i+1)}')
                                    
                                    print(f'    {len(accounts)+1}. Add account')
                                    print(f'    {len(accounts)+2}. Delete Password Manager Account')
                                    print(f'    {len(accounts)+3}. Logout')
                                    first_loop = False
                                    
                                    try:
                                        
                                        user_menu_choice = int(input('\n  Please Select an Option from the Menu Above:  '))
                                        
                                        if 0 < user_menu_choice <= len(accounts):
                                            
                                            hidden = True
                                            account = get_account(username, user_menu_choice)
                                            account_details = retrieve_account_details(username, master_password, user_menu_choice)
                                            
                                            while True:
                                                
                                                header()
                                                print(f'  Details for {account}\n\n    Username:  {account_details[0]}\n\n    Password:  {'●'*len(account_details[1]) if hidden else account_details[1]}\n')
                                                print('  1. Show/Hide Username and Password')
                                                print('  2. Copy Username')
                                                print('  3. Copy Password')
                                                print('  4. Update Username')
                                                print('  5. Update Password')
                                                print('  6. Delete Account')
                                                print('  7. Return to the User Menu')
                                                
                                                try:
                                                    
                                                    acount_menu_choice = int(input('\n  Please Select an Option from the Menu Above:  '))
                                                    
                                                    if acount_menu_choice == 1:
                                                        
                                                        if hidden:
                                                            
                                                            hidden = False
                                                            
                                                        else:
                                                            
                                                            hidden = True
                                                            
                                                    elif acount_menu_choice == 2:
                                                        
                                                        pyperclip.copy(account_details[0])
                                                        print(f'\n  Username for {account} Copied\n\n  Press Enter to Continue')
                                                        input()
                                                        
                                                    elif acount_menu_choice == 3:
                                                        
                                                        pyperclip.copy(account_details[1])
                                                        print(f'\n  Password for {account} Copied\n\n  Press Enter to Continue')
                                                        input()
                                                        
                                                    elif acount_menu_choice == 4:
                                                        
                                                        confirm_master_password = pwinput.pwinput(prompt='\n  Confirm Password:  ', mask='●')
                                                        
                                                        if master_password == confirm_master_password:
                                                            
                                                            updated_account_username = input('\n  New Username:')
                                                            account_details[0] = updated_account_username
                                                            update_password(username, confirm_master_password, account, account_details[0], account_details[1])
                                                            print(f'\n  Username for {account} Updated\n\n  Press Enter to Continue')
                                                            input()
                                                            
                                                        else:
                                                            
                                                            print(RED + f'\n  Incorrect Password'+ RESET +'\n\n  Press Enter to Continue')
                                                            input()
                                                            
                                                    elif acount_menu_choice == 5:
                                                        
                                                        confirm_master_password = pwinput.pwinput(prompt='\n  Confirm Password:  ', mask='●')
                                                        
                                                        if master_password == confirm_master_password:
                                                            
                                                            updated_account_password = pwinput.pwinput(prompt='\n  New Password:  ', mask='●')
                                                            confirm_updated_account_password = pwinput.pwinput(prompt='\n  Confirm New Password:  ', mask='●')
                                                            
                                                            if updated_account_password == confirm_updated_account_password:
                                                                
                                                                hidden = True
                                                                account_details[1] = updated_account_password
                                                                update_password(username, confirm_master_password, account, account_details[0], account_details[1])
                                                                print(f'\n  Password for {account} Updated\n\n  Press Enter to Continue')
                                                                input()
                                                                
                                                            else:
                                                                
                                                                print(RED + f'\n  Passwords Do Not Match'+ RESET +'\n\n  Press Enter to Continue')
                                                                input()
                                                                
                                                        else:
                                                            
                                                            print(RED + f'\n  Incorrect Password'+ RESET +'\n\n  Press Enter to Continue')
                                                            input()
                                                            
                                                    elif acount_menu_choice == 6:
                                                        
                                                        confirm_master_password = pwinput.pwinput(prompt='\n  Confirm Password:  ', mask='●')
                                                        
                                                        if master_password == confirm_master_password:
                                                            
                                                            delete_password(username, confirm_master_password, user_menu_choice)
                                                            print(f'\n  Account for {account} Deleted\n\n  Press Enter to Continue')
                                                            input()
                                                            break
                                                        
                                                        else:
                                                            
                                                            print(RED + f'\n  Incorrect Password'+ RESET +'\n\n  Press Enter to Continue')
                                                            input()
                                                            
                                                    elif acount_menu_choice == 7:
                                                        
                                                        break
                                                    else:
                                                        
                                                        invalid_input()
                                                        
                                                except:
                                                    
                                                    invalid_input()
                                        
                                        elif user_menu_choice == len(accounts)+1:
                                            
                                            while True:
                                                
                                                header()
                                                print('  Please Enter the Details for the Account\n\n  Press Enter to Return to the User Menu\n')
                                                account = input('  Account:  ')
                                                
                                                if account == '':
                                                    
                                                    user_menu_choice = None
                                                    break
                                                
                                                elif check_account(username, account):
                                                    
                                                    print(RED + f'\n  Account for {account} Already Exists'+ RESET +'\n\n  Press Enter to Continue')
                                                    input()
                                                
                                                else:
                                                    
                                                    account_username = input('\n  Username:  ')
                                                    
                                                    while True:
                                                        
                                                        header()
                                                        print('  Please Enter the Details for the Account\n\n  Press Enter to Return to the User Menu\n')
                                                        print(f'  Account:  {account}\n')
                                                        print(f'  Username:  {account_username}')
                                                        account_password = pwinput.pwinput(prompt='\n  Password:  ', mask='●')
                                                        
                                                        if account_password == '':
                                                            
                                                            break
                                                        
                                                        confirm_account_password = pwinput.pwinput(prompt='\n  Confirm Password:  ', mask='●')
                                                        
                                                        if confirm_account_password == '':
                                                            
                                                            break
                                                        
                                                        elif account_password != confirm_account_password:
                                                            
                                                            print(RED + f'\n  Passwords do not match'+ RESET +'\n\n  Press Enter to Continue')
                                                            input()
                                                        
                                                        elif add_password(username, master_password, account, account_username, account_password):
                                                            
                                                            print(GREEN + f'\n  Account for {account} Added'+ RESET + '\n\n  Press Enter to Return to the User Menu\n')
                                                            input()
                                                            break
                                                    break
                                        
                                        elif user_menu_choice == len(accounts)+2:
                                            
                                            confirm_master_password = pwinput.pwinput(prompt='\n  Confirm Password:  ', mask='●')
                                            
                                            if master_password == confirm_master_password:
                                                
                                                delete_user(username)
                                                
                                            attempts = 3
                                            break
                                        
                                        elif user_menu_choice == len(accounts)+3:
                                            
                                            attempts = 3
                                            break
                                        
                                        else:
                                            
                                            invalid_input()
                                    
                                    except:
                                        
                                        invalid_input()
                    
                    break
            
            elif main_menu_choice == 2:
                
                user_created = False
                
                while not user_created:
                    
                    header()
                    print('  Please Enter a Username for the Password Manager\n\n  Or Press Enter to Return to the Main Menu\n')
                    username = input('  Username:  ')
                    
                    if username == '':
                        
                        break
                    
                    elif found_user(username):
                        
                        print(RED + '\n  Sorry this username is taken' + RESET + '\n\n  Press Enter to Continue')
                        input()
                    
                    else:
                        
                        while True:
                            
                            header()
                            print('  Please Enter a Master Password for the Password Manager\n\n  Or Press Enter to Return to the Main Menu\n')
                            master_password = pwinput.pwinput(prompt='  Password:  ', mask='●')
                            
                            if master_password == '':
                                
                                break
                            
                            else:
                                
                                header()
                                print('  Please confirm Master Password for the Password Manager\n')
                                confirm_master_password = pwinput.pwinput(prompt='  Password:  ', mask='●')
                                
                                if master_password == confirm_master_password:
                                    
                                    create_user(username, master_password)
                                    header()
                                    print(GREEN + f'  New user, {username}, created successfully'+ RESET + '\n\n  Press Enter to Return to the Main Menu\n')
                                    input()
                                    user_created = True
                                    break
                                
                                else:
                                    
                                    print(RED + f'  Passwords do not match' + RESET + '\n\n  Press Enter to try again\n')
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
                
                invalid_input()
        
        except:
            
            invalid_input()

if __name__ == '__main__':
    main()