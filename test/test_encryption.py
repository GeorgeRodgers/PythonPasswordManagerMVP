import pytest
from src.encryption import *
from cryptography.fernet import InvalidToken


def test_generate_salt():
    # Ensure salt is generated and is 32 characters (hex of 16 bytes)
    salt = generate_salt()
    assert len(salt) == 32
    assert isinstance(salt, str)


def test_hash_master_password():
    # Test hashing with consistent output for same input
    master_password = "test_password"
    salt = generate_salt()
    hashed1 = hash_master_password(master_password, salt)
    hashed2 = hash_master_password(master_password, salt)
    assert hashed1 == hashed2  # Consistent hash for same input
    assert len(hashed1) > 0
    assert hashed1 != hash_master_password("different_password", salt)  # Different hash for different input


def test_master_password_2_key():
    # Ensure derived keys are consistent for the same password and salt
    master_password = "test_password"
    salt = generate_salt()
    key1 = master_password_2_key(master_password, salt)
    key2 = master_password_2_key(master_password, salt)
    assert key1 == key2  # Consistent key for same input
    assert key1 != master_password_2_key("different_password", salt)  # Different keys for different input


def test_encrypt_data_decrypt_data():
    # Ensure encryption and decryption works correctly
    master_password = "test_password"
    salt = generate_salt()
    key = master_password_2_key(master_password, salt)
    
    data = "This is a test message."
    encrypted_data = encrypt_data(key, data)
    
    assert encrypted_data != data  # Encrypted data should not match plaintext
    decrypted_data = decrypt_data(key, encrypted_data)
    assert decrypted_data == data  # Decrypted data should match original

    # Ensure decryption fails with wrong key
    wrong_key = master_password_2_key("wrong_password", salt)
    with pytest.raises(InvalidToken):
        decrypt_data(wrong_key, encrypted_data)


def test_key_salt_dependency():
    # Ensure keys are dependent on salt
    master_password = "test_password"
    salt1 = generate_salt()
    salt2 = generate_salt()
    key1 = master_password_2_key(master_password, salt1)
    key2 = master_password_2_key(master_password, salt2)
    assert key1 != key2  # Keys should differ for different salts
