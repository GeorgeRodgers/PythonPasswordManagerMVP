# Password Manager

A secure and simple password manager that allows users to manage their credentials effectively. The application provides features for user authentication, account management, and secure encryption of sensitive data.

---

## Features

### 1. User Management
- **Create New User**: Register with a unique username and a master password.
- **Login**: Authenticate using the master password to access stored credentials.

### 2. Account Management
- **Add Accounts**: Store account credentials securely.
- **View Accounts**: List all saved accounts and view account details (username/password).
- **Update Accounts**: Modify stored account usernames or passwords.
- **Delete Accounts**: Remove stored account credentials.

### 3. Security
- **Password Hashing**: Master passwords are hashed and salted for secure storage.
- **Encryption**: Account credentials are encrypted using `cryptography.fernet`.
- **Clipboard Support**: Quickly copy account usernames or passwords to the clipboard.

---

## Installation

### Requirements
- Python 3.8 or later
- Required Python modules:
  - `cryptography`
  - `pwinput`
  - `pyperclip`

### Setup
1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Install the dependencies:
```bash
pip install cryptography pwinput pyperclip
```

---

## Usage

### Running the Application
Execute the main script:
```bash
python CLI_application.py
```

### Main Menu Options
1. **Login**: Access your saved accounts.
2. **Create New User**: Register as a new user.
3. **Exit Password Manager**: Quit the application.

---

## File Structure

### 1. `CLI_application.py`
- Implements the command-line interface for the application.
- Provides user interaction through menus for login, user creation, and account management.

### 2. `encryption.py`
- Handles password hashing, salting, and encryption/decryption of sensitive data.
- Key Functions:
  - `generate_salt()`: Generates a unique salt.
  - `hash_master_password()`: Hashes the master password.
  - `master_password_2_key()`: Generates a encryption key using the master password and salt.
  - `encrypt_data()` / `decrypt_data()`: Encrypts and decrypts account credentials.

### 3. `password_manager.py`
- Provides backend logic for user authentication and account management.
- Key Functions:
  - `found_user()`: Checks if a user exists.
  - `create_user()`: Registers a new user with a hashed master password.
  - `login()`: Retrieves the hashed master password and salt for the user, the hashed input password is compared with the hashed master. If they match the master password and salt are used to generate a key for the encryption and decryption. 
  - `add_password()` / `update_password()` / `delete_password()`: Manage account credentials.
  - `list_accounts()` / `retrieve_account_details()`: Retrieve stored account information.

---

## Security Features
- **Master Password Hashing**: Uses SHA3-512 hashing with a unique salt for secure storage.
- **Data Encryption**: Encrypts all account credentials with a key derived from the master password.
- **Access Control**: Requires re-authentication (master password) for sensitive operations.

---

## Example Workflow

1. **Create a New User**:
   - Enter a unique username and master password.
   - Confirm the master password to complete registration.

2. **Login**:
   - Enter your username and master password to authenticate.

3. **Manage Accounts**:
   - List, add, view, update, or delete stored account credentials.
   - Copy account details to the clipboard for quick access.

---
