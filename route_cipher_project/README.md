# Route Cipher Decryption Project

A Python project for decrypting text that has been encrypted using route cipher techniques.

## Project Structure

```
route_cipher_project/
├── main.py              # Entry point - runs the decryption program
├── decrypt.py           # Core decryption logic
├── utils.py             # Helper functions for validation and parsing
├── config.py            # User configuration (cipher text and keys)
└── README.md            # This file
```

## How to Use

1. **Edit `config.py`** - Add your cipher text and key routes:
   ```python
   CIPHER_TEXT = "your_encrypted_text_here"
   KEY_ROUTES = "1,2,3,4,5,6"  # or [1, 2, 3, 4, 5, 6]
   ```

2. **Run the program**:
   ```bash
   python main.py
   ```

3. **View output** - The decrypted text will be displayed in the console

## File Descriptions

- **main.py** - Entry point that orchestrates the decryption process
- **decrypt.py** - Contains the route cipher decryption algorithm
- **utils.py** - Utility functions for input validation and key parsing
- **config.py** - User-editable configuration section

## Example

```
Input (Cipher Text): HEIOLTL
Key Routes: 1,4,2,5,3,6
Output (Decrypted): HELIOABC
```

## Requirements

- Python 3.6+

## Author

Created for learning route cipher cryptography concepts.
