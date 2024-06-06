from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

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
        num_passwords = int(request.form['num_passwords'])
        length = int(request.form['length'])
        min_uppercase = int(request.form['min_uppercase'])
        min_lowercase = int(request.form['min_lowercase'])
        min_digits = int(request.form['min_digits'])
        min_symbols = int(request.form['min_symbols'])
        use_ambiguous = 'use_ambiguous' in request.form
        custom_set = request.form['custom_set'] or None

        passwords = generate_passwords(num_passwords, length, min_uppercase, min_lowercase, min_digits, min_symbols, use_ambiguous, custom_set)
        
        return render_template('index.html', passwords=passwords)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
