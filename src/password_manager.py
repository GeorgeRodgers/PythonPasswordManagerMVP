"""
Import os and json modules
'*' imports all functions from encryption.py and console_styling.py
"""
import os, json
from encryption import *
from console_styling import *

"""
The program needs to be able to check if a user exists
This can be done by check for password file
"""
def found_user(username):
    if os.path.exists(f'{username}_passwords.json'):
        return True
    else:
        return False

"""
The password manager requires data to persist between runs of the application
Create a new user with their own password file and store a copy of the hashed master password and a salt
The first step is checking if the user exists
If a user exists the function will stop and return 'False'
The user does not exist the program continues to create a key and save it for the new user
To create the passwords file it is opened in write mode ('w') as file
Opening as file ensures it is closed after the operation
'json.dump()' adds empty dictionary we have passed to the file as an argument
The dictionary is formatted to list account with the username/email and password 
The second argument is the file the dictionary is being sent to
The console prints a statement and the function returns true
"""

def create_user(username, master_password):
    if found_user(username):
        return False
    
    salt = generate_salt()
    hashed_master_password = hash_master_password(master_password, salt)
    
    with open(f'{username}_passwords.json', 'w') as file:
        json.dump({'user_authentication': {'hashed_master_password': hashed_master_password, 'salt': salt}}, file, indent="")
    return True

"""
In order to authenticated the user and use the stored encrypted password the program need a function to store them
The file is opened in as read only ('r')
'json.load(file)' retrieves the json data from the file and it is return by the function
If the user password file is not found in the try block this will raise and exception
The except block returns None if the passwords are not loaded
"""

def load_passwords(username):
    try:
        with open(f"{username}_passwords.json", 'r') as file:
            return json.load(file)
    except:
        return

"""
Now the program can load the password file, it can also authenticate a user
And return that users key generated from the master password and salt
"""

def login(username, master_password):
    passwords = load_passwords(username)
    hashed_master_password = passwords['user_authentication']['hashed_master_password']
    salt = passwords['user_authentication']['salt']
    input_password_hash = hash_master_password(master_password, salt)
    if hashed_master_password == input_password_hash:
        return master_password_2_key(master_password, salt)
    else:
        return False

"""
The application requires a function to save the passwords
For our file structure to work we need to update the JSON,
sort it and completely write over the original file
"""

def save_passwords(username, passwords):
    new_passwords = {'user_authentication': {'hashed_master_password': passwords['user_authentication']['hashed_master_password'], 'salt': passwords['user_authentication']['salt']}}
    del passwords['user_authentication']
    sorted_passwords = dict(sorted(passwords.items()))
    new_passwords.update(sorted_passwords)
    with open(f'{username}_passwords.json', 'w') as file:
        json.dump(new_passwords, file, indent="")

"""
Before the program saves a username and password for a given account,
the program need to check if it exists so that it is not modified unless the user specifies they want to do that
"""
def check_account(username, account):
    passwords = load_passwords(username)
    if account in passwords:
        return True
    else:
        return False

"""
The program needs a function to add the username and passwords
In order to encrypt the passwords the program requires the key
This can be generated using the login() function previously defined 
"""

def add_password(username, master_password, account, account_username, account_password):
    if not found_user(username):
        return
    
    if check_account(username, account):
        return
    
    key = login(username, master_password)
    if key == False:
        return False
    
    else:
        passwords = load_passwords(username)
        encrypted_account_username = encrypt_data(key, account_username)
        encrypted_account_password = encrypt_data(key, account_password)
        new_password = {account: {'username': encrypted_account_username, 'password':encrypted_account_password}}
        passwords.update(new_password)
        save_passwords(username, passwords)
        return True

"""
A function is required to list accounts stored in the passwords file with out the 'user_authentication' data
"""

def list_accounts(username):
    if not found_user(username):
        return
    passwords = load_passwords(username)
    account_list = list(passwords)
    del account_list[0]
    return account_list

"""
A function is required to get a account from a list by it's index
"""

def get_account(username, num):
    try:
        account_list = list_accounts(username)
        return account_list[num-1]
    except:
        return

"""
A function is now required to retrieve specific passwords by the position in the list of accounts
By default this function will return the username and a hidden version password
This can be changed by adding 'False' as the forth parameter
These inputs should be evaluated using "pwinput.pwinput(prompt='Enter master password:  ', mask='●')"
"""

def retrieve_account_details(username, master_password, num):
    
    if not found_user(username):
        return
    try:
        account = get_account(username, num)
        
        key = login(username, master_password)
        if key == False:
            return False
        
        else:
            
            passwords = load_passwords(username)
            encrypted_username = passwords[account]['username']
            decrypted_username = decrypt_data(key, encrypted_username)
            encrypted_password = passwords[account]['password']
            decrypted_password = decrypt_data(key, encrypted_password)
            return [decrypted_username, decrypted_password]
    except:
        return

"""
A user may also want to delete a username/password combination for a account
Again in the CLI and GUI apps the user should be prompted confirm the master password
before the program can delete a account
"""

def delete_password(username, confirm_password, num):
    if not found_user(username):
        return
    try:
        account = get_account(username, num)
        
        key = login(username, confirm_password)
        if key == False:
            return False
        
        else:
            
            passwords = load_passwords(username)
            del passwords[account]
            save_passwords(username, passwords)
            
    except:
        return

"""
Instead of deleting the account, the user may want to just update it
The function is similar to 'add_password()' except it checks the password already exists
Again in the CLI and GUI apps the user should be prompted confirm the master password
before the program can update a account
"""

def update_password(username, master_password, account, account_username, account_password):
    if not found_user(username):
        return
    
    if not check_account(username, account):
        return
    
    key = login(username, master_password)
    if key == False:
        return False
    
    else:
        passwords = load_passwords(username)
        encrypted_account_username = encrypt_data(key, account_username)
        encrypted_account_password = encrypt_data(key, account_password)
        new_password = {account: {'username': encrypted_account_username, 'password':encrypted_account_password}}
        passwords.update(new_password)
        save_passwords(username, passwords)
        return True

if __name__ == '__main__':
    add_password('george', 'password', 'Amazon', 'updated_username', 'updated_password')