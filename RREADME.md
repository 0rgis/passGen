<!-- <img src="https://github.com/0rgis/passGen/assets/31127560/a5e323f5-c0a4-454f-842c-bca583050cbe" width="200"/><br> -->
<!-- ![oie_jpg](https://github.com/0rgis/passGen/assets/31127560/009d9573-c958-4908-953d-86a9e4276f67" ) -->
<img src="https://github.com/0rgis/passGen/assets/31127560/009d9573-c958-4908-953d-86a9e4276f67" width="200"/><br>

# passGen

This Python script generates random passwords based on user-defined criteria, providing a flexible and interactive way to create secure passwords for various purposes.

## Features

- **Password Length Customization:** Choose the desired length of the generated passwords.
- **Character Set Control:** Control the inclusion of uppercase letters, lowercase letters, digits, and symbols in the passwords.
- **Exclusion of Ambiguous Characters:** Improve readability by excluding ambiguous characters.
- **Password Saving:** Save generated passwords to a file for easy access.
- **Password Strength Checking:** Check password strength based on length, character types, and repeating patterns.
- **Interactive User Prompts:** Easily customize password generation options through interactive prompts.
- **Argument User Prompts:** Easily customize password generation options through interactive prompts.
- **Custom Character Set:** Now you can provide a custom character set to be included in password generation.

## Table of Contents

- [passGen](#passgen)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Interactive Mode](#interactive-mode)
    - [Command-Line Arguments](#command-line-arguments)

## Installation

To use the Password Generator, you'll need to have Python installed on your system. Download and install Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/0rgis/passGen.git
   ```

2. Change into the project directory:

   ```bash
   cd passGen
   ```

3. Run the script:

   ```bash
   python passGen.py
   ```

You can also choose to run the script within a virtual environment to manage dependencies and ensure isolation from your system's Python installation.

### Installing and Running in a Virtual Environment

1. Create a new directory for your project:

   ```bash
   mkdir passGen_project
   cd passGen_project
   ```

2. Create a virtual environment within the project directory:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   Your terminal prompt should now indicate that you are working within the virtual environment.

4. Clone the PassGen repository into the project directory:

   ```bash
   git clone https://github.com/0rgis/passGen.git
   ```

5. Change into the PassGen directory:

   ```bash
   cd passGen
   ```

6. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

7. You can now run the PassGen script as usual:

   ```bash
   python passGen.py
   ```

8. When you're finished using PassGen, you can deactivate the virtual environment:

   ```bash
   deactivate
   ```

This setup allows you to keep PassGen and its dependencies isolated from other projects on your system.

## Usage

### Interactive Mode

The Password Generator script offers an interactive command-line interface. Follow these steps to use the script:

1. Open a terminal or command prompt.

2. Navigate to the directory where you cloned the repository:

   ```bash
   cd path/to/passGen
   ```

3. Run the script:

   ```bash
   python3 passGen.py
   ```

4. Enter options for password generation, such as length, minimum uppercase letters, minimum lowercase letters, minimum digits, minimum symbols, whether to include ambiguous characters, and optionally provide a custom character set.

5. The script will generate the specified number of passwords and save them to a file (default: `passwords.txt`), no need for a file extension either.

6. If you choose to repeat the password generation, the script will prompt you to enter the number of passwords for each run.

7. The generated passwords will be appended to the specified file.

8. Example

![ghubMD](https://github.com/0rgis/passGen/assets/31127560/5b5f6c09-58bc-4e14-ab7b-4147238ec3dd)

### Command-Line Arguments

Alternatively, you can use command-line arguments to customize password generation without the need for interactive prompts. Here's the list of available arguments:

- `--length`: Specify the length of the generated passwords.
- `--min_uppercase`: Specify the minimum number of uppercase letters.
- `--min_lowercase`: Specify the minimum number of lowercase letters.
- `--min_digits`: Specify the minimum number of digits.
- `--min_symbols`: Specify the minimum number of symbols.
- `--ambiguous`: Include ambiguous characters (use 'y' for yes, 'n' for no).
- `--custom_set`: Provide a custom character set for password generation.
- `--num_passwords`: Specify the number of passwords to generate.
- `--file_path`: Specify the file path to save passwords (default: `passwords.txt`).

Example usage:

```bash
python3 passGen.py --length 12 --min_uppercase 2 --min_lowercase 2 --min_digits 2 --min_symbols 2 --ambiguous y --custom_set "!@#$%" --num_passwords 5 --file_path my_passwords.txt
```

This command will generate 5 passwords of length 12 with at least 2 uppercase letters, 2 lowercase letters, 2 digits, and 2 symbols (including ambiguous characters) using the custom set "!@#$%", and save them to the file `my_passwords.txt`.
