import argparse
import os
import random
import re
import string
import sys

def print_banner():
    banner = """
                     _____            
                    |  __ \           
 _ __   __ _ ___ ___| |  \/ ___ _ __  
| '_ \ / _` / __/ __| | __ / _ \ '_ \ 
| |_) | (_| \__ \__ \ |_\ \  __/ | | |
| .__/ \__,_|___/___/\____/\___|_| |_|
| |                                   
|_|                                   
    """
    print(banner)

def get_custom_character_set():
    custom_set = input("Enter your custom character set (leave blank to use the default set): ").strip()
    return custom_set if custom_set else None

def generate_password(length, characters):
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords(num_passwords, length, min_uppercase=1, min_lowercase=1, min_digits=1, min_symbols=1, use_ambiguous=False, custom_set=None):
    characters = ''

    if min_uppercase > 0:
        characters += string.ascii_uppercase
    if min_lowercase > 0:
        characters += string.ascii_lowercase
    if min_digits > 0:
        characters += string.digits
    if min_symbols > 0:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected.")
        return None

    if not use_ambiguous:
        # Exclude ambiguous characters
        ambiguous_characters = "lIO01"
        characters = ''.join(char for char in characters if char not in ambiguous_characters)

    # Include the custom character set if provided
    if custom_set:
        characters += custom_set

    passwords = []

    for _ in range(num_passwords):
        password = (
            ''.join(random.choice(string.ascii_uppercase) for _ in range(min_uppercase)) +
            ''.join(random.choice(string.ascii_lowercase) for _ in range(min_lowercase)) +
            ''.join(random.choice(string.digits) for _ in range(min_digits)) +
            ''.join(random.choice(string.punctuation) for _ in range(min_symbols)) +
            ''.join(random.choice(characters) for _ in range(length - min_uppercase - min_lowercase - min_digits - min_symbols))
        )

        # Shuffle the password characters to randomize their order
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        passwords.append(password)

    return passwords

def generate_and_save_passwords(num_passwords, length, min_uppercase=1, min_lowercase=1, min_digits=1, min_symbols=1, use_ambiguous=False, custom_set=None, file_path="passwords.txt"):
    passwords = generate_passwords(num_passwords, length, min_uppercase, min_lowercase, min_digits, min_symbols, use_ambiguous, custom_set)

    if passwords:
        if file_path:
            with open(file_path, "w") as file:
                for password in passwords:
                    file.write(password + "\n")

            print(f"Passwords saved to {file_path}")
        else:
            print("Passwords were not saved.")
    else:
        print("No passwords generated.")

def main():
    print_banner()

    parser = argparse.ArgumentParser(description='Generate passwords.')
    parser.add_argument('-n', '--number', type=int, help='Number of passwords to generate')
    parser.add_argument('-l', '--length', type=int, help='Length of the passwords')
    parser.add_argument('-u', '--uppercase', type=int, help='Minimum number of uppercase letters')
    parser.add_argument('-w', '--lowercase', type=int, help='Minimum number of lowercase letters')
    parser.add_argument('-d', '--digits', type=int, help='Minimum number of digits')
    parser.add_argument('-s', '--symbols', type=int, help='Minimum number of symbols')
    parser.add_argument('-c', '--custom', action='store_true', help='Use custom character set')
    parser.add_argument('-a', '--ambiguous', action='store_true', help='Include ambiguous characters')
    parser.add_argument('-f', '--file', help='File path to save passwords')
    args = parser.parse_args()

    save_to_file = False
    file_path = None
    custom_set = None  # Initialize custom_set

    if any(vars(args).values()):
        num_passwords = args.number or 1
        length = args.length or 12
        min_uppercase = args.uppercase or 1
        min_lowercase = args.lowercase or 1
        min_digits = args.digits or 1
        min_symbols = args.symbols or 1
        use_custom = args.custom
        use_ambiguous = args.ambiguous
        file_path = args.file or "passwords.txt"
        save_to_file = True
    else:
        while True:
            print("Choose password generation options:")
            length = int(input("Enter the password length (minimum 8 characters): "))
            if length >= 8:
                break
            else:
                print("Error: Password length must be at least 8 characters.")

        min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
        min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
        min_digits = int(input("Enter the minimum number of digits: "))
        min_symbols = int(input("Enter the minimum number of symbols: "))
        use_ambiguous = input("Include ambiguous characters? (y/n): ").lower() == 'y'
        custom_set = get_custom_character_set()

        save_passwords = input("Do you want to save the generated passwords to a file? (y/n): ").lower()
        if save_passwords == 'y' or save_passwords == 'yes':
            file_path = input("Enter the file path to save passwords (press Enter for default 'passwords.txt'): ").strip() or "passwords.txt"
            save_to_file = True

        num_passwords = int(input("Enter the number of passwords to generate: "))

    generate_and_save_passwords(num_passwords, length, min_uppercase, min_lowercase, min_digits, min_symbols, use_ambiguous, custom_set, file_path)

    if not save_to_file:
        repeat = input("Do you want to generate passwords again? (y/n): ").lower()
        if repeat == 'y':
            main()

if __name__ == "__main__":
    main()