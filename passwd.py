import random
import string
import re

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
        with open(file_path, "w") as file:
            for password in passwords:
                file.write(password + "\n")

        print(f"Passwords saved to {file_path}")
    else:
        print("No passwords generated.")

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    symbol_criteria = any(char in string.punctuation for char in password)
    pattern_criteria = not re.search(r'([a-zA-Z0-9])\1+', password)

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, symbol_criteria, pattern_criteria])

    return strength_score

def get_user_options():
    length = int(input("Enter the password length: "))
    min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
    min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
    min_digits = int(input("Enter the minimum number of digits: "))
    min_symbols = int(input("Enter the minimum number of symbols: "))
    use_ambiguous = input("Include ambiguous characters? (y/n): ").lower() == 'y'
    custom_set = get_custom_character_set()
    file_path = input("Enter the file path to save passwords (press Enter for default 'passwords.txt'): ").strip() or "passwords.txt"

    return length, min_uppercase, min_lowercase, min_digits, min_symbols, use_ambiguous, custom_set, file_path

def main():
    while True:
        print("Choose password generation options:")
        length, min_uppercase, min_lowercase, min_digits, min_symbols, use_ambiguous, custom_set, file_path = get_user_options()
        num_passwords = int(input("Enter the number of passwords to generate: "))

        generate_and_save_passwords(num_passwords, length, min_uppercase, min_lowercase, min_digits, min_symbols, use_ambiguous, custom_set, file_path)

        repeat = input("Do you want to generate passwords again? (y/n): ").lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
