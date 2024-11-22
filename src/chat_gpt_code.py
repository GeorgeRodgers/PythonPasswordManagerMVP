import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.ttk import Treeview, Button, Label, Entry
import pyperclip


# Mock functions to replace actual backend functionality for demonstration
# Replace these with the actual functions from your backend
def found_user(username):
    return username in ["user1", "user2"]


def login(username, password):
    return username == "user1" and password == "password123"


def create_user(username, password):
    return True


def list_accounts(username):
    return ["Account1", "Account2"]


def get_account(username, index):
    accounts = list_accounts(username)
    return accounts[index - 1] if 0 <= index - 1 < len(accounts) else None


def retrieve_account_details(username, master_password, index):
    return ("example_user", "example_pass")


def add_password(username, master_password, account, account_username, account_password):
    return True


def update_password(username, master_password, account, new_username, new_password):
    return True


def delete_password(username, master_password, index):
    return True


def delete_user(username):
    return True


# Tkinter GUI implementation
class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.username = None
        self.master_password = None

        self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()
        Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        Label(self.root, text="Username").pack()
        username_entry = Entry(self.root)
        username_entry.pack()

        Label(self.root, text="Password").pack()
        password_entry = Entry(self.root, show="●")
        password_entry.pack()

        def attempt_login():
            username = username_entry.get()
            password = password_entry.get()

            if found_user(username) and login(username, password):
                self.username = username
                self.master_password = password
                self.main_menu()
            else:
                messagebox.showerror("Error", "Invalid credentials")

        Button(self.root, text="Login", command=attempt_login).pack(pady=5)
        Button(self.root, text="Create New User", command=self.create_user_screen).pack(pady=5)

    def create_user_screen(self):
        self.clear_screen()
        Label(self.root, text="Create New User", font=("Arial", 16)).pack(pady=10)

        Label(self.root, text="Username").pack()
        username_entry = Entry(self.root)
        username_entry.pack()

        Label(self.root, text="Password").pack()
        password_entry = Entry(self.root, show="●")
        password_entry.pack()

        def create_user_action():
            username = username_entry.get()
            password = password_entry.get()

            if create_user(username, password):
                messagebox.showinfo("Success", "User created successfully!")
                self.login_screen()
            else:
                messagebox.showerror("Error", "Failed to create user")

        Button(self.root, text="Create User", command=create_user_action).pack(pady=5)
        Button(self.root, text="Back to Login", command=self.login_screen).pack(pady=5)

    def main_menu(self):
        self.clear_screen()
        Label(self.root, text=f"Welcome {self.username}", font=("Arial", 16)).pack(pady=10)

        accounts = list_accounts(self.username)

        tree = Treeview(self.root, columns=("Account"), show="headings")
        tree.heading("Account", text="Account")
        for account in accounts:
            tree.insert("", "end", values=(account,))
        tree.pack(pady=10)

        def view_account():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No account selected")
                return

            index = tree.index(selected_item[0]) + 1
            self.account_details_screen(index)

        Button(self.root, text="View Account", command=view_account).pack(pady=5)
        Button(self.root, text="Add Account", command=self.add_account_screen).pack(pady=5)
        Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)

    def account_details_screen(self, index):
        self.clear_screen()

        account = get_account(self.username, index)
        account_details = retrieve_account_details(self.username, self.master_password, index)

        Label(self.root, text=f"Details for {account}", font=("Arial", 16)).pack(pady=10)
        Label(self.root, text=f"Username: {account_details[0]}").pack()
        Label(self.root, text=f"Password: {'●' * len(account_details[1])}").pack()

        def copy_username():
            pyperclip.copy(account_details[0])
            messagebox.showinfo("Info", "Username copied to clipboard")

        def copy_password():
            pyperclip.copy(account_details[1])
            messagebox.showinfo("Info", "Password copied to clipboard")

        Button(self.root, text="Copy Username", command=copy_username).pack(pady=5)
        Button(self.root, text="Copy Password", command=copy_password).pack(pady=5)
        Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=5)

    def add_account_screen(self):
        self.clear_screen()
        Label(self.root, text="Add New Account", font=("Arial", 16)).pack(pady=10)

        Label(self.root, text="Account Name").pack()
        account_entry = Entry(self.root)
        account_entry.pack()

        Label(self.root, text="Username").pack()
        username_entry = Entry(self.root)
        username_entry.pack()

        Label(self.root, text="Password").pack()
        password_entry = Entry(self.root, show="●")
        password_entry.pack()

        def add_account_action():
            account = account_entry.get()
            username = username_entry.get()
            password = password_entry.get()

            if add_password(self.username, self.master_password, account, username, password):
                messagebox.showinfo("Success", "Account added successfully!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "Failed to add account")

        Button(self.root, text="Add Account", command=add_account_action).pack(pady=5)
        Button(self.root, text="Back to Main Menu", command=self.main_menu).pack(pady=5)


# Run the application
root = tk.Tk()
app = PasswordManagerApp(root)
root.mainloop()
