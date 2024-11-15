"""
Import os and json modules
'*' imports all functions from encryption.py and console_styling.py
"""
import os, json
from encryption import *
from console_styling import *

"""
The password manager requires data to persist between runs of the application
Create a new user with their own password file and encryption key
The first step is checking if the user exists
If a user exists the function will stop and return 'False'
The user does not exist the program continues to create a key and save it for the new user
To create the passwords file it is opened in write mode ('w') as file
Opening as file ensures it is closed after the operation
'json.dump()' adds empty dictionary we have passed to the file as an argument
The dictionary is formatted to list service with the username/email and password 
The second argument is the file the dictionary is being sent to
The console prints a statement and the function returns true
"""

def create_user(username, password):
    if os.path.exists(f'{username}_passwords.json'):
        print(RED + f'Error: User, {username}, already exists.' + RESET)
        return False
    
    key = generate_key()
    
    save_key(username, key)
    
    encrypted_master_password = encrypt_data(key, password)
    
    with open(f'{username}_passwords.json', 'w') as file:
        json.dump({'master_password': {'username/email': None, 'password': encrypted_master_password}}, file, indent="")
    
    print(GREEN + f'User, {username}, created successfully.' + RESET)
    return True

"""
For the persistent passwords to be used the password manager requires a function to load them
The file is opened in as read only ('r')
'json.load(file)' retrieves the json data from the file and it is return by the function
If the user password file is not found in the try block this will raise and exception
The except block prints the error to the console and the function returns none
"""

def load_passwords(username):
    try:
        with open(f"{username}_passwords.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(RED + f'Error: User, {username}, does not exists.' + RESET)
        return None

if __name__ == '__main__':
    data = load_passwords('george')
    print(data)
    print('still running')
