
# Password Generator

A flexible and customizable password generator written in Python. This script allows you to generate strong passwords with various options to specify the characteristics of the passwords.

## Features

- Generate multiple passwords at once
- Customize the length of passwords
- Specify minimum numbers of uppercase letters, lowercase letters, digits, and symbols
- Optionally exclude ambiguous characters
- Optionally use a custom character set
- Save generated passwords to a file

## Requirements

- Python 3.x

## Usage

You can run the script using command-line arguments or interactively.

### Command-Line Arguments

The script accepts the following command-line arguments:

- `-n`, `--number`: Number of passwords to generate
- `-l`, `--length`: Length of the passwords
- `-u`, `--uppercase`: Minimum number of uppercase letters
- `-w`, `--lowercase`: Minimum number of lowercase letters
- `-d`, `--digits`: Minimum number of digits
- `-s`, `--symbols`: Minimum number of symbols
- `-c`, `--custom`: Use custom character set
- `-a`, `--ambiguous`: Include ambiguous characters
- `-f`, `--file`: File path to save passwords

#### Examples

Generate 5 passwords of length 12 with at least 2 uppercase letters, 2 lowercase letters, 2 digits, and 2 symbols, excluding ambiguous characters:

```sh
python passGen.py -n 5 -l 12 -u 2 -w 2 -d 2 -s 2
```

Generate 3 passwords of length 16, including ambiguous characters, and save to `my_passwords.txt`:

```sh
python passGen.py -n 3 -l 16 -a -f my_passwords.txt
```

Generate 2 passwords of length 10 using a custom character set:

```sh
python passGen.py -n 2 -l 10 -c
# You will be prompted to enter the custom character set interactively
```

### Interactive Mode

If no command-line arguments are provided, the script will run in interactive mode, prompting you for input:

```sh
python passGen.py
```

You will be prompted to enter the following:

1. Password length (minimum 8 characters)
2. Minimum number of uppercase letters
3. Minimum number of lowercase letters
4. Minimum number of digits
5. Minimum number of symbols
6. Whether to include ambiguous characters (y/n)
7. Custom character set (optional)
8. Whether to save passwords to a file (y/n)
9. Number of passwords to generate

### Help

To display the help message with all available options:

```sh
python passGen.py -h
```

## License

This project is licensed under the MIT License.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or new features.

## Acknowledgements

ASCII art in the banner is generated using [patorjk.com](http://patorjk.com/software/taag/).
```

This `README.md` file provides an overview of the script, details on how to use it with examples, and additional sections for license and contributing guidelines.