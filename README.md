# Token-Formatter
# Email:Pass:Token to Token Extractor

This script extracts tokens from a list formatted as `email:password:token` and saves the tokens in a structured log folder with a timestamp. It allows you to quickly reformat your token list and store them for future use.

## Features

- **Token Extraction**: Extracts tokens from a `tokens.txt` file where each line is formatted as `email:password:token`.
- **Automatic Directory Creation**: Creates a `Log/` directory and organizes extracted tokens based on the current date.
- **Simple Menu System**: Provides a user-friendly interface to start the token extraction process.
- **Formatted Output**: Saves the tokens to a `tokens.txt` file in the appropriate date-stamped directory.

## Requirements

- Python 3.x
- Required Libraries:
  - `datetime` (included with Python standard library)

## How to Use

1. **Prepare Tokens**:
   - Create a `tokens.txt` file in the same directory as the script.
   - The file should contain one token per line, formatted as `email:password:token`, for example:
     ```text
     user1@example.com:password1:token1
     user2@example.com:password2:token2
     ```

2. **Run the Script**:
   - To execute the script, simply run:
     ```bash
     python main.py
     ```

3. **Menu**:
   - The script will present you with a simple menu:
     ```text
     Email:pass:token to token (y/n)
     ```
   - Choose `y` to start extracting the tokens.

4. **Results**:
   - The script will extract the tokens and save them in the following directory format:
     ```text
     Log/<current_date>/tokens.txt
     ```

## Directory Structure

The tokens are saved in a `Log/` folder, with each session organized by the date it was processed. The folder structure looks like this:
```text
Log/
  └── dd-mm-yyyy/
      └── tokens.txt
```

## Notes

- Ensure that the `tokens.txt` file is formatted correctly (i.e., `email:password:token`), as the script splits the content based on colons.
- The script automatically creates necessary directories if they do not exist.
