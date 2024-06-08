from flask import Flask, render_template, request, redirect, url_for, flash
import random
import string
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

def is_valid_input(data):
    try:
        num_passwords = int(data['num_passwords'])
        length = int(data['length'])
        min_uppercase = int(data['min_uppercase'])
        min_lowercase = int(data['min_lowercase'])
        min_digits = int(data['min_digits'])
        min_symbols = int(data['min_symbols'])

        if num_passwords <= 0 or length < 8 or min_uppercase < 0 or min_lowercase < 0 or min_digits < 0 or min_symbols < 0:
            return False, "Invalid input values."

        if min_uppercase + min_lowercase + min_digits + min_symbols > length:
            return False, "Sum of minimum character types exceeds password length."

        return True, None
    except ValueError:
        return False, "Invalid input values."

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
        return None

    if not use_ambiguous:
        ambiguous_characters = "lIO01"
        characters = ''.join(char for char in characters if char not in ambiguous_characters)

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

        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        passwords.append(password)

    return passwords

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form
        is_valid, error_message = is_valid_input(form_data)
        
        if not is_valid:
            flash(error_message)
            return render_template('index.html', form_data=form_data, passwords=None)

        num_passwords = int(form_data['num_passwords'])
        length = int(form_data['length'])
        min_uppercase = int(form_data['min_uppercase'])
        min_lowercase = int(form_data['min_lowercase'])
        min_digits = int(form_data['min_digits'])
        min_symbols = int(form_data['min_symbols'])
        use_ambiguous = 'use_ambiguous' in form_data
        custom_set = form_data['custom_set'] if form_data['custom_set'] else None

        passwords = generate_passwords(num_passwords, length, min_uppercase, min_lowercase, min_digits, min_symbols, use_ambiguous, custom_set)
        
        return render_template('index.html', form_data={}, passwords=passwords)

    return render_template('index.html', form_data={}, passwords=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8107)