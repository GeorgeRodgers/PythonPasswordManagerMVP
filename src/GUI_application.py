from password_manager import *
import tkinter as tk
from tkinter.ttk import Treeview, Button, Label, Entry, Scrollbar, Style
import os, time, pwinput, pyperclip

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("350x400")
        self.root.minsize(350, 400) 
        self.username = None
        self.create_login_frame()

    def create_login_frame(self):
        """Create the login screen for the application."""
        self.clear_frame()

        
        Label(self.root, text="Password\nManager", font=("Arial", 24), justify=tk.CENTER).pack(pady=5)
        Label(self.root, text="Login", font=("Arial", 18)).pack(pady=25)

        Label(self.root, text="Username", font=("Arial", 10)).pack(pady=2)
        self.username_entry = Entry(self.root, justify='center', font=("Arial", 10), width=25)
        self.username_entry.pack(pady=2)
        
        Label(self.root, text="Password", font=("Arial", 10)).pack(pady=2)
        self.master_password_entry = Entry(self.root, justify='center', font=("Arial", 10), width=25, show="●")
        self.master_password_entry.pack(pady=2)

        self.error_label = Label(self.root, text="", font=("Arial", 8, 'bold'), foreground="red")
        self.error_label.pack(pady=2)
        
        self.root.bind('<Return>', lambda: self.login())

        login_button = Button(self.root, text='Login', width=25, command=lambda: self.login()).pack(pady=2)
        Button(self.root, text="Create New User", width=25, command=self.create_register_user_frame).pack(pady=2)

    def login(self):
        username = self.username_entry.get().strip()
        master_password = self.master_password_entry.get().strip()
            
        if not found_user(username):
            self.error_label.config(text="User Not Found")
            self.username_entry.delete(0, 'end')
            self.master_password_entry.delete(0, 'end')
            return

        if login(username, master_password):
            self.create_user_frame(username, master_password)
        else:
            self.error_label.config(text="Incorrect Password")
            self.master_password_entry.delete(0, 'end')

    def create_register_user_frame(self):
        self.clear_frame()
        
        Label(self.root, text="Register New User", font=("Arial", 18)).pack(pady=25)
        
        Label(self.root, text="Username", font=("Arial", 10)).pack(pady=2)
        self.username_entry = Entry(self.root, justify='center', font=("Arial", 10), width=25)
        self.username_entry.pack(pady=2)
        
        Label(self.root, text="Password", font=("Arial", 10)).pack(pady=2)
        self.master_password_entry = Entry(self.root, justify='center', font=("Arial", 10), width=25, show="●")
        self.master_password_entry.pack(pady=2)
        
        Label(self.root, text="Confirm Password", font=("Arial", 10)).pack(pady=2)
        self.confirm_master_password_entry = Entry(self.root, justify='center', font=("Arial", 10), width=25, show="●")
        self.confirm_master_password_entry.pack(pady=2)
        
        self.error_label = Label(self.root, text="", font=("Arial", 8, 'bold'), foreground="red")
        self.error_label.pack(pady=2)
        
        self.root.bind('<Return>', self.create_user)
        
        Button(self.root, text='Register User', width=25, command=(lambda: self.create_user())).pack(pady=5)
        Button(self.root, text='Back', width=25, command=self.create_login_frame).pack(pady=5)
    
    def create_user(self):
        """Create a new user."""
        username = self.username_entry.get().strip()
        master_password = self.master_password_entry.get().strip()
        confirm_master_password = self.confirm_master_password_entry.get().strip()
        
        if username == "":
            self.error_label.config(text="Username cannot be empty.")
            self.master_password_entry.delete(0, 'end')
            self.confirm_master_password_entry.delete(0, 'end')
            return
        
        if master_password != confirm_master_password:
            self.error_label.config(text="Passwords do not match.")
            self.master_password_entry.delete(0, 'end')
            self.confirm_master_password_entry.delete(0, 'end')
            return
        
        if not found_user(username):
            create_user(username, master_password)
            self.create_login_frame()
        else:
            self.error_label.config(text="Username already in use")
            self.username_entry.delete(0, 'end')
            self.master_password_entry.delete(0, 'end')
            self.confirm_master_password_entry.delete(0, 'end')
    
    def create_user_frame(self, username, master_password):
        self.clear_frame()
        
        Label(self.root, text=f"Welcome {username}", font=("Arial", 16)).pack(pady=10)
        
        accounts = list_accounts(username)
        
        tree = Treeview(self.root, columns=("Accounts"), show="headings", height="6")
        tree.heading('Accounts', text='Accounts')
        tree.column(column=('Accounts') , anchor='center', width=100)
        
        for i in range(len(accounts)):
            tree.insert("", "end", values=f'{get_account(username, i+1)}', tags=i+1)
        tree.pack(pady=10)
        
        def get_account_num():
            try: 
                selected_item = tree.item(tree.selection())['tags'][0]
                return selected_item
            except:
                self.error_label.config(text="No Account Selected")
                
        self.error_label = Label(self.root, text="", font=("Arial", 8, 'bold'), foreground="red")
        self.error_label.pack(pady=2)
        
        Button(self.root, text="View Account", width=25, command=(lambda : self.create_account_frame(username, master_password, get_account_num()))).pack(pady=2)
        Button(self.root, text="Add Account", width=25).pack(pady=2)
        Button(self.root, text="Password Generator", width=25).pack(pady=2)
        Button(self.root, text="Logout", width=25, command=self.create_login_frame).pack(pady=2)
    
    def create_account_frame(self, username, master_password, account_num):
        
        self.clear_frame()
        
        account = get_account(username, account_num)
        
        account_details = retrieve_account_details(username, master_password, account_num)
        
        Label(self.root, text=f"Details for {account}", font=("Arial", 18)).pack(pady=25)
        
        Label(self.root, text=f"Username: {username}", font=("Arial", 10)).pack(pady=2)
        
        Label(self.root, text=f"Password: {'●'*len(username)}", font=("Arial", 10)).pack(pady=2)
        
        Button(self.root, text='Back', width=25, command=lambda: self.create_user_frame(username, master_password)).pack(pady=5)
    
    def clear_frame(self):
        """Clear the current frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    PasswordManagerApp(root)
    root.mainloop()
