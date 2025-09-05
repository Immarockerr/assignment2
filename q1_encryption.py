"""
Assignment 2 
Question 1: Text Encryption and Decryption with Verification
"""
import string

# Shift a single character
def shift_char(c, shift, forward=True):
    if c.islower():
        alphabet = string.ascii_lowercase
    elif c.isupper():
        alphabet = string.ascii_uppercase
    else:
        return c  # leave non-letters unchanged

    pos = alphabet.index(c)
    if forward:
        new_pos = (pos + shift) % 26
    else:
        new_pos = (pos - shift) % 26
    return alphabet[new_pos]


# Encryption function
def encrypt(text, shift1, shift2):
    result = ""
    for c in text:
        if c.islower():
            # lowercase: shift forward by shift1*shift2
            result += shift_char(c, shift1 * shift2, True)
        elif c.isupper():
            # uppercase: shift forward by shift2*2
            result += shift_char(c, shift2 ** 2, True)
        else:
            result += c
    return result


# Decryption function
def decrypt(text, shift1, shift2):
    result = ""
    for c in text:
        if c.islower():
            # reverse of encryption
            result += shift_char(c, shift1 * shift2, False)
        elif c.isupper():
            result += shift_char(c, shift2 ** 2, False)
        else:
            result += c
    return result


# Verification
def verify(original, decrypted):
    return original == decrypted


# Main program
if __name__ == "__main__":
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    # Read raw text
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    # Encrypt
    encrypted = encrypt(raw, shift1, shift2)
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted)

    # Decrypt
    decrypted = decrypt(encrypted, shift1, shift2)
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted)

    # Verify
    if verify(raw, decrypted):
        print("Decryption successful!!!! ")
    else:
        print("Decryption failed!!!!! ")
