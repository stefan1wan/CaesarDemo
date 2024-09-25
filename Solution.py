def caesar_decrypt(ciphertext, shift):
    result = ""
    
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters are not decrypted

    return result


def crack_caesar_cipher(ciphertext):
    possible_decryptions = []
    print("Attempting to break the Caesar cipher...")
    
    # Try all possible shifts from 1 to 25
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        possible_decryptions.append(f"Shift {shift}: {decrypted_text}")
    
    return possible_decryptions


# Example usage
ciphertext = "govmywodywidkvu"
results = crack_caesar_cipher(ciphertext)

# Print all the possible shifts and their corresponding decryption
for result in results:
    print(result)
