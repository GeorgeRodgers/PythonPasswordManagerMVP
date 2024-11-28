import pytest
import os
import json
from src.password_manager import *

# Utility function to clean up test files
def cleanup_user_files(username):
    if os.path.exists(f"{username}_passwords.json"):
        os.remove(f"{username}_passwords.json")

@pytest.fixture
def setup_user():
    # Setup for user creation
    username = "testuser"
    master_password = "testmaster"
    cleanup_user_files(username)
    create_user(username, master_password)
    yield username, master_password
    cleanup_user_files(username)

def test_found_user(setup_user):
    username, _ = setup_user
    assert found_user(username) is True
    assert found_user("nonexistent_user") is False

def test_create_user():
    username = "newuser"
    master_password = "newpassword"
    cleanup_user_files(username)
    assert create_user(username, master_password) is True
    assert found_user(username) is True
    # Check duplicate user creation
    assert create_user(username, master_password) is False
    cleanup_user_files(username)

def test_load_passwords(setup_user):
    username, _ = setup_user
    passwords = load_passwords(username)
    assert passwords is not None
    assert "user_authentication" in passwords

def test_login(setup_user):
    username, master_password = setup_user
    assert login(username, master_password) is not False
    assert login(username, "wrongpassword") is False

def test_add_password(setup_user):
    username, master_password = setup_user
    account = "test_account"
    account_username = "test_user"
    account_password = "test_password"
    assert add_password(username, master_password, account, account_username, account_password) is True
    # Check duplicate account addition
    assert add_password(username, master_password, account, account_username, account_password) is None

def test_list_accounts(setup_user):
    username, master_password = setup_user
    account = "test_account"
    add_password(username, master_password, account, "test_user", "test_password")
    accounts = list_accounts(username)
    assert accounts == [account]

def test_get_account(setup_user):
    username, master_password = setup_user
    account = "test_account"
    add_password(username, master_password, account, "test_user", "test_password")
    assert get_account(username, 1) == account
    assert get_account(username, 2) is None  # Out of bounds

def test_retrieve_account_details(setup_user):
    username, master_password = setup_user
    account = "test_account"
    account_username = "test_user"
    account_password = "test_password"
    add_password(username, master_password, account, account_username, account_password)
    details = retrieve_account_details(username, master_password, 1)
    assert details == [account_username, account_password]
    assert retrieve_account_details(username, "wrongpassword", 1) is False

def test_delete_password(setup_user):
    username, master_password = setup_user
    account = "test_account"
    add_password(username, master_password, account, "test_user", "test_password")
    delete_password(username, master_password, 1)
    accounts = list_accounts(username)
    assert len(accounts) == 0

def test_update_password(setup_user):
    username, master_password = setup_user
    account = "test_account"
    add_password(username, master_password, account, "test_user", "test_password")
    new_account_password = "new_password"
    assert update_password(username, master_password, account, "test_user", new_account_password) is True
    details = retrieve_account_details(username, master_password, 1)
    assert details[1] == new_account_password

def test_delete_user(setup_user):
    username, _ = setup_user
    assert delete_user(username) is True
    assert found_user(username) is False

def test_generate_password():
    password = generate_password(16, True, True, True, True, True, True)
    assert len(password) == 16
    assert any(char.isupper() for char in password)
    assert any(char.isdigit() for char in password)
    assert any(char in string.punctuation for char in password)
