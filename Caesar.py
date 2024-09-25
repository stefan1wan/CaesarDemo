#!/usr/bin/env python3

def caesar_encrypt(plaintext, shift):
    result = ""
    
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters are not encrypted

    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)  # Decrypt by reversing the shift

plaintext = "welcometomytalk"
password = 10

ciphertext = caesar_encrypt(plaintext, password)
print(f"Encrypted: {ciphertext}")  # Output: KHOOR

decrypted_text = caesar_decrypt(ciphertext, password)
print(f"Decrypted: {decrypted_text}")  # Output: HELLO
