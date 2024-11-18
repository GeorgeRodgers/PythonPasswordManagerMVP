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
        print(RED + f'\nError: User, {username}, already exists.' + RESET)
        return False
    
    key = generate_key()
    
    save_key(username, key)
    
    encrypted_master_password = encrypt_data(key, password)
    
    with open(f'{username}_passwords.json', 'w') as file:
        json.dump({'master_password': encrypted_master_password}, file, indent="")
    
    print(GREEN + f'\nUser, {username}, created successfully.' + RESET)
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


"""
The application requires a function to save the passwords
For our file structure to work we need to update the JSON and completely
write over the original file
"""

def save_passwords(username, passwords):
    with open(f'{username}_passwords.json', 'w') as file:
        json.dump(passwords, file, indent="")
"""
A function is required to authenticate the user if we are saving or retrieving the passwords
"""

def login(username, password):
    key = load_key(username)
    passwords = load_passwords(username)
    master_password = passwords['master_password']
    if decrypt_data(key, master_password) == password:
        print(GREEN + f'User authenticated' + RESET)
        return True
    else:
        print(RED + f'User not authenticated' + RESET)
        return False

"""
The is a little more logic to adding the passwords as they need to encrypted
So an extra function is required for this
"""

def add_password(username, password, service, service_username, service_password):
    if not login(username, password):
        return
    
    if service == 'q':
        return
    
    key = load_key(username)
    if not key:
        print(RED + f'Error: User, {username}, encryption key not found.' + RESET)
        return
    
    encrypted_service_username = encrypt_data(key, service_username)
    encrypted_service_password = encrypt_data(key, service_password)
    
    passwords = load_passwords(username)
    
    if passwords is None:
        print(RED + f'Error: User, {username}, password list not found.' + RESET)
        return
    
    if service in passwords:
        print(RED + f'Error: Password for {service} already exists' + RESET)
        service = input('Please enter an alternative name for this password, or "q" to exit:\n')
        return add_password(username, password, service, service_username, service_password)
    
    passwords.update({service: {'Username': encrypted_service_username, 'Password': encrypted_service_password}})
    save_passwords(username, passwords)
    
    print(GREEN + f'Username and password successfully added for {service}.' + RESET)

"""
A function is now required to retrieve specific passwords
"""

def retrieve_passwords(username, password):
    if not login(username, password):
        return
    
    key = load_key(username)
    if not key:
        print(RED + f'Error: User, {username}, encryption key not found.' + RESET)
        return
    
    passwords = load_passwords(username)
    
    if passwords is None:
        print(RED + f'Error: User, {username}, password list not found.' + RESET)
        return
    
    service_list = list(passwords)
    
    for num in range(len(service_list)):
        if num == 0:
            pass
        else:
            print(f'{num}. {service_list[num]}')
    
    user_choice = int(input('Enter the number of the service you would like to retrieve:  '))
    
    try:
        service = service_list[user_choice]
        encrypted_username = passwords[service]['Username']
        decrypted_username = decrypt_data(key, encrypted_username)
        encrypted_password = passwords[service]['Password']
        decrypted_password = decrypt_data(key, encrypted_password)
        print(f'\n  {service}\n\n    Username: {decrypted_username}\n    Password: {decrypted_password}')
    except:
        print(RED + f'Error: Username/Password combination not found for selected service.' + RESET)

if __name__ == '__main__':
    retrieve_passwords('George', 'password')