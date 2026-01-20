import random
import string

print("----- PASSWORD GENERATOR & STRENGTH CHECKER -----")

# Take password length
length = int(input("Enter password length: "))

# User choices
upper = input("Include uppercase letters? (y/n): ")
lower = input("Include lowercase letters? (y/n): ")
digits = input("Include numbers? (y/n): ")
symbols = input("Include special characters? (y/n): ")

characters = ""

if upper == 'y':
    characters += string.ascii_uppercase
if lower == 'y':
    characters += string.ascii_lowercase
if digits == 'y':
    characters += string.digits
if symbols == 'y':
    characters += string.punctuation

# Validation
if characters == "":
    print("Error: You must select at least one character type!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    # -------- Strength Checker --------
    strength = 0

    if length >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    print("\nPassword Strength:")

    if strength <= 2:
        print("Weak Password ❌")
    elif strength == 3 or strength == 4:
        print("Medium Password ⚠️")
    else:
        print("Strong Password ✅")
