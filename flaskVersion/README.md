# Password Generator Web Application

A web-based password generator built with Python and Flask. This application allows users to generate secure passwords through a web interface with customizable options.

## Features

- Generate multiple passwords at once
- Customize the length of passwords
- Specify minimum numbers of uppercase letters, lowercase letters, digits, and symbols
- Optionally exclude ambiguous characters
- Optionally use a custom character set
- Responsive and user-friendly web interface

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/password-generator-web.git
   cd password-generator-web
   ```

2. **Install the required packages:**
   ```sh
   pip install Flask
   ```

## Usage

1. **Run the Flask application:**
   ```sh
   python app.py
   ```

2. **Access the web application:**

   Open your web browser and navigate to `http://127.0.0.1:8080/` (or the specified host and port).

## Configuration

You can configure the host and port by modifying the `app.py` file:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
```

- `host='0.0.0.0'`: This makes the app accessible on all public IPs.
- `port=8080`: Change `8080` to any other available port number if needed.

## Form Fields

- **Number of Passwords:** Enter the number of passwords to generate.
- **Length:** Enter the desired length of each password (minimum 8 characters).
- **Minimum Uppercase Letters:** Specify the minimum number of uppercase letters.
- **Minimum Lowercase Letters:** Specify the minimum number of lowercase letters.
- **Minimum Digits:** Specify the minimum number of digits.
- **Minimum Symbols:** Specify the minimum number of symbols.
- **Include Ambiguous Characters:** Check this box to include ambiguous characters like `l`, `I`, `O`, `0`, `1`.
- **Custom Character Set:** Enter a custom set of characters to include in the password.

