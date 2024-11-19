from cryptography.fernet import Fernet
import os

"""
Each user needs a unique and complex key for the encryption/decryption functions
This application uses 'Fernet Symmetric Encryption'
So the 'Fernet' module has been imported from the 'cryptography.fernet' library
"""
def generate_key():
    return Fernet.generate_key() # generated a new key each time the function is called

def save_key(username, key): # Create unique path for key based on username
    with open(f'{username}_key.key', 'wb') as key_file: # 'wb' specifies that data written must be bites
        key_file.write(key) # Creates the key file

def load_key(username): # sets the key path based on the user 
    if os.path.exists(f'{username}_key.key'):
        with open(f'{username}_key.key', 'rb') as key_file: # 'rb' specifies that data read must be bites
            return key_file.read() # returns the key
    else:
        return None # If key is not found return none

"""
User Passwords can now be encrypted/decrypted using the created and stored keys
'f = Fernet(key)' Creates instance of the Fernet class that is specific to the key
Calling the '.encrypt()' or '.decrypt()' method on the Fernet instance encrypts/decrypts the data
The data must be in the bytes format for these methods to work
The '.encode()' method is specific to a str data type
The '.decode()' method converts the decrypted data bytes back to string
"""

def encrypt_data(key, data):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    decrypt_data = f.decrypt(encrypted_data.encode()).decode()
    return decrypt_data

if __name__ == '__main__':
    pass