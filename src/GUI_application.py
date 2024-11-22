from password_manager import *
import tkinter as tk
from tkinter import messagebox, Label
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

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)
        
        self.login_frame_title = tk.Label(self.login_frame, text="Password", font=("Arial", 24)).pack(pady=1)
        self.login_frame_title = tk.Label(self.login_frame, text="Manager", font=("Arial", 24)).pack(pady=1)
        self.login_frame_title = tk.Label(self.login_frame, text="Login", font=("Arial", 18)).pack(pady=10)

        self.username_label = tk.Label(self.login_frame, text="Username", font=("Arial", 10)).pack(pady=2)
        self.username_entry = tk.Entry(self.login_frame, justify='center', font=("Arial", 10), width=25)
        self.username_entry.pack(pady=2)
        
        self.master_password_label = tk.Label(self.login_frame, text="Password", font=("Arial", 10)).pack(pady=2)
        self.master_password_entry = tk.Entry(self.login_frame, justify='center', font=("Arial", 10), width=25, show="●")
        self.master_password_entry.pack(pady=2)

        self.error_label = tk.Label(self.login_frame, text="", font=("Arial", 10, 'bold'), fg="red")
        self.error_label.pack(pady=2)

        self.login_button = tk.Button(self.login_frame, text='Login', font=("Arial", 10), pady=2, width=15, command=self.login)
        self.login_button.pack(pady=3)
        self.create_user_button = tk.Button(self.login_frame, text="Create New User", font=("Arial", 10), pady=2, width=15, command=self.create_register_user_frame)
        self.create_user_button.pack(pady=3)

    def login(self):
        username = self.username_entry.get().strip()
        master_password = self.master_password_entry.get().strip()

        if not found_user(username):
            self.error_label.config(text="User Not Found")
            self.username_entry.delete(0, 'end')
            self.master_password_entry.delete(0, 'end')
            return

        if login(username, master_password):
            self.create_user_frame()
        else:
            self.error_label.config(text="Incorect Password")
            self.username_entry.delete(0, 'end')
            self.master_password_entry.delete(0, 'end')

    def create_register_user_frame(self):
        self.clear_frame()

        self.register_user_frame = tk.Frame(self.root)
        self.register_user_frame.pack(pady=20)

        self.login_frame_title = tk.Label(self.register_user_frame, text="Register New User", font=("Arial", 18))
        self.login_frame_title.pack(pady=10)

        self.error_label = tk.Label(self.register_user_frame, text="", font=("Arial", 10, 'bold'), fg="red")
        self.error_label.pack(pady=2)

        self.username_label = tk.Label(self.register_user_frame, text="Username", font=("Arial", 10))
        self.username_label.pack(pady=2)
        self.username_entry = tk.Entry(self.register_user_frame, justify='center', font=("Arial", 10), width=25)
        self.username_entry.pack(pady=2)

        self.master_password_label = tk.Label(self.register_user_frame, text="Password", font=("Arial", 10))
        self.master_password_label.pack(pady=2)
        self.master_password_entry = tk.Entry(self.register_user_frame, justify='center', font=("Arial", 10), width=25, show="●")
        self.master_password_entry.pack(pady=2)

        self.confirm_master_password_label = tk.Label(self.register_user_frame, text="Confirm Password", font=("Arial", 10))
        self.confirm_master_password_label.pack(pady=2)
        self.confirm_master_password_entry = tk.Entry(self.register_user_frame, justify='center', font=("Arial", 10), width=25, show="●")
        self.confirm_master_password_entry.pack(pady=2)

        self.create_user_button = tk.Button(self.register_user_frame, text="Create New User", font=("Arial", 10), pady=2, width=15, command=self.create_user)
        self.create_user_button.pack(pady=3)

        self.back_button = tk.Button(self.register_user_frame, text="Back", font=("Arial", 10), pady=2, width=15, command=self.create_login_frame)
        self.back_button.pack(pady=3)

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
            self.username_entry.delete(0, 'end')
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
    
    def create_user_frame(self):
        self.clear_frame()

        self.user_frame = tk.Frame(self.root)
        self.user_frame.pack(pady=20)

        self.back_button = tk.Button(self.user_frame, text="Back", font=("Arial", 10), pady=2, width=15, command=self.create_login_frame)
        self.back_button.pack(pady=3)
    
    def clear_frame(self):
        """Clear the current frame."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    PasswordManagerApp(root)
    root.mainloop()
