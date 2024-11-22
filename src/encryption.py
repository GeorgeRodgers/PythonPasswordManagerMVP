from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib, os, pyperclip, sys, base64

"""
A function is required to hash the master password for storage
If the master password is openly stored it is very easy break the encryption
It is extremely difficult (near impossible) to unhash the master password,
but it would be possible to hash an input and compare this with the stored hashed master password
Because if two user use the same password it sensible to add a random salt to the master password
This can be openly stored
"""

def generate_salt():
    return os.urandom(16).hex()

def hash_master_password(master_password, salt):
    slated_master_password = salt + master_password
    sha3_512 = hashlib.sha3_512()
    sha3_512.update(slated_master_password.encode())
    return sha3_512.hexdigest()

"""
A function is required to convert a master_password into a key using a hashing function
SHA-3 hasn't been broken yet and is unlikely to be broken anytime soon
"""
def master_password_2_key(master_password, salt):
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA3_512(),
    length=32,
    salt = salt.encode(),
    iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

"""
User Passwords can now be encrypted/decrypted using key generated from the master password and a salt
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
    salt1 = generate_salt()
    salt2 = generate_salt()
    print(hash_master_password('P4$$w0rD', salt1))
    print(hash_master_password('password', salt1))
    print(hash_master_password('password', salt2))
    print(hash_master_password('password', salt2))
    key = master_password_2_key('password', salt1)
    data = 'this is a secret message'
    encrypted_data = encrypt_data(key, data)
    print(encrypted_data)
    decrypted_data = decrypt_data(key, encrypted_data) 
    print(decrypted_data)
    print(salt1)