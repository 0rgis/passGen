<!DOCTYPE html>
<html lang="en">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8L64ZBYXXW"></script>
<script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            /* background-color: #f4f4f4; */
            background-image: url('/assets/img/bg-3.png');
	        overflow: hidden;
	        background-size: cover;
	        background-repeat: no-repeat;
            background-attachment: fixed;
	        background-position: center;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            height: 100vh;
            margin: 0;
            padding-top: 100px;
        }

        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
            color: #333;
        }

        .alert {
            color: red;
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            margin-bottom: 15px;
            width: 48%;
        }

        label {
            margin-bottom: 5px;
            color: #555;
            font-size: 14px;
        }

        input[type="number"],
        input[type="text"],
        input[type="checkbox"] {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
        }

        .full-width {
            width: 100%;
        }

        button {
            padding: 10px 20px;
            background-color: #5cb85c;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s;
            width: 100%;
        }

        button:hover {
            background-color: #4cae4c;
        }

        ul {
            list-style-type: none;
            padding: 0;
            margin-top: 20px;
            width: 100%;
            text-align: left;
        }

        li {
            background-color: #f9f9f9;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            word-wrap: break-word;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Uncle Rat's Password Generator</h1>
        <form method="post">
            <div class="form-group">
                <label for="num_passwords">Number of Passwords:</label>
                <input type="number" id="num_passwords" name="num_passwords" value="1" min="1" required>
            </div>

            <div class="form-group">
                <label for="length">Length:</label>
                <input type="number" id="length" name="length" value="12" min="8" required>
            </div>

            <div class="form-group">
                <label for="min_uppercase">Minimum Uppercase Letters:</label>
                <input type="number" id="min_uppercase" name="min_uppercase" value="1" min="0" required>
            </div>

            <div class="form-group">
                <label for="min_lowercase">Minimum Lowercase Letters:</label>
                <input type="number" id="min_lowercase" name="min_lowercase" value="1" min="0" required>
            </div>

            <div class="form-group">
                <label for="min_digits">Minimum Digits:</label>
                <input type="number" id="min_digits" name="min_digits" value="1" min="0" required>
            </div>

            <div class="form-group">
                <label for="min_symbols">Minimum Symbols:</label>
                <input type="number" id="min_symbols" name="min_symbols" value="1" min="0" required>
            </div>

            <div class="form-group full-width">
                <label for="use_ambiguous">Include Ambiguous Characters:</label>
                <input type="checkbox" id="use_ambiguous" name="use_ambiguous">
            </div>

            <div class="form-group full-width">
                <label for="custom_set">Custom Character Set:</label>
                <input type="text" id="custom_set" name="custom_set">
            </div>

            <button type="submit">Generate Passwords</button>
        </form>

        <?php
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            function sanitize_input($data) {
                return htmlspecialchars(stripslashes(trim($data)));
            }

            function generate_password($length, $characters) {
                $password = '';
                $characters_length = strlen($characters);
                for ($i = 0; $i < $length; $i++) {
                    $password .= $characters[rand(0, $characters_length - 1)];
                }
                return $password;
            }

            function generate_passwords($num_passwords, $length, $min_uppercase, $min_lowercase, $min_digits, $min_symbols, $use_ambiguous, $custom_set) {
                $passwords = [];
                $characters = '';

                if ($min_uppercase > 0) {
                    $characters .= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
                }
                if ($min_lowercase > 0) {
                    $characters .= 'abcdefghijklmnopqrstuvwxyz';
                }
                if ($min_digits > 0) {
                    $characters .= '0123456789';
                }
                if ($min_symbols > 0) {
                    $characters .= '!@#$%^&*()-_=+[]{}|;:,.<>?';
                }

                if (!$use_ambiguous) {
                    $characters = str_replace(['l', 'I', 'O', '0', '1'], '', $characters);
                }

                if ($custom_set) {
                    $characters .= $custom_set;
                }

                for ($i = 0; $i < $num_passwords; $i++) {
                    $password = '';
                    $password .= generate_password($min_uppercase, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ');
                    $password .= generate_password($min_lowercase, 'abcdefghijklmnopqrstuvwxyz');
                    $password .= generate_password($min_digits, '0123456789');
                    $password .= generate_password($min_symbols, '!@#$%^&*()-_=+[]{}|;:,.<>?');
                    $remaining_length = $length - strlen($password);
                    $password .= generate_password($remaining_length, $characters);
                    $password = str_shuffle($password);
                    $passwords[] = $password;
                }

                return $passwords;
            }

            $num_passwords = sanitize_input($_POST['num_passwords']);
            $length = sanitize_input($_POST['length']);
            $min_uppercase = sanitize_input($_POST['min_uppercase']);
            $min_lowercase = sanitize_input($_POST['min_lowercase']);
            $min_digits = sanitize_input($_POST['min_digits']);
            $min_symbols = sanitize_input($_POST['min_symbols']);
            $use_ambiguous = isset($_POST['use_ambiguous']);
            $custom_set = sanitize_input($_POST['custom_set']);

            if ($length < 8) {
                echo '<div class="alert">Password length must be at least 8 characters.</div>';
            } else if ($min_uppercase < 0 || $min_lowercase < 0 || $min_digits < 0 || $min_symbols < 0) {
                echo '<div class="alert">Minimum values cannot be negative.</div>';
            } else if ($min_uppercase + $min_lowercase + $min_digits + $min_symbols > $length) {
                echo '<div class="alert">Sum of minimum character types exceeds password length.</div>';
            } else {
                $passwords = generate_passwords($num_passwords, $length, $min_uppercase, $min_lowercase, $min_digits, $min_symbols, $use_ambiguous, $custom_set);

                echo '<h2>Generated Passwords</h2>';
                echo '<ul>';
                foreach ($passwords as $password) {
                    echo '<li>' . htmlspecialchars($password) . '</li>';
                }
                echo '</ul>';
            }
        }
        ?>
    </div>
</body>
</html>
