# Assignment 2 - Text Encryption and Decryption

## Group Members
- Subha Sitaula
- Diksha
- Pawan Acharya
- Esha 

## Description
This program takes text from a file (raw_text.txt), then encrypts the text using two-user supplied shifts (shift1 and shift2) and saves the resulting text in encrypted_text.txt

It then decrypts the text and saves it in decrypted_text.txt, then crosschecks it with the original file.

This indicates that the processed text during encryption and the processed text during decryption is unchanged and therefore the encryption and decryption process is accurate.

## Encryption Rules
The program uses the following rules for letter shifts:

**Lowercase letters:**

a-m = shift forward by shift1 * shift2

n-z = shift backward by shift1 + shift2

**Uppercase letters:**

A-M = shift backward by shift1

N-Z = shift forward by shift2^2

**Other characters:**

Spaces, numbers, tabs and punctuation are unchanged.

## Program Behavior

1) When the program is executed:

2) The user asked for shift1 and shift2

3) The program reads raw_text.txt.

4) An encrypted version is saved as encrypted_text.txt.

5) A decrypted version is saved as decrypted_text.txt.

6) The program indicates whether, and how many, the original text and decrypted text differences.

## Screenshot of Program Output
![Q1_Output](image.png)
[Encrypted Text](encrypted_text.txt)
[Decrypted Text](decrypted_text.txt)

