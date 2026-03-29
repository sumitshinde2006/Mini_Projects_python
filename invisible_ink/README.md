# Invisible Ink - Steganography Project

Hide secret encrypted messages inside Word documents using steganography and Vigenère cipher.

## Project Overview

This project combines two cryptographic techniques:
- **Steganography**: Hiding messages inside other data (Word documents)
- **Vigenère Cipher**: Encryption method to protect the hidden message

The hidden text is made invisible by changing its color to white and size to 1pt.

## Project Structure

```
invisible_ink/
├── main.py                  # Main script (entry point)
├── cipher.py                # Vigenère cipher utilities
├── template.docx            # Blank formatted template
├── fakeMessage.docx         # Visible cover message
├── realMessage_Vig.docx     # Encrypted hidden message
└── README.md                # This file
```

## File Descriptions

### 📄 main.py
**Main Python script - Entry point**

Functions:
- `vigenere_encrypt()` - Encrypt message using Vigenère cipher
- `vigenere_decrypt()` - Decrypt encrypted message
- `hide_message_in_docx()` - Hide encrypted message in Word document
- `extract_message_from_docx()` - Extract and decrypt hidden message

**Usage:**
```python
python main.py
```

### 📄 cipher.py
**Vigenère cipher utility class**

Provides:
- `VigenereCipher.encrypt()` - Encryption
- `VigenereCipher.decrypt()` - Decryption
- `VigenereCipher.analyze_frequency()` - Frequency analysis

### 📄 template.docx
**Blank formatted Word template**

Contains:
- Default fonts and styles
- Proper margins and formatting
- Acts as base for hidden message document

### 📄 fakeMessage.docx
**Visible cover message**

Purpose:
- Acts as normal business document
- Contains blank lines where hidden text will be inserted
- Makes the output look legitimate

### 📄 realMessage_Vig.docx
**Encrypted hidden message**

Contains:
- Secret message encrypted with Vigenère cipher
- Inserted into blank lines of fake message
- Converted to invisible white text

## How It Works

### Hiding a Message

1. **Start with templates**
   - Load `template.docx` (formatting)
   - Load `fakeMessage.docx` (cover content)

2. **Encrypt message**
   - Apply Vigenère cipher with secret key
   - Convert plaintext to ciphertext

3. **Insert hidden text**
   - Add encrypted text to document
   - Set text color to white (RGB 255, 255, 255)
   - Set font size to 1pt

4. **Save output**
   - Document looks normal but contains hidden message
   - Only visible when text is selected or highlighted

### Extracting a Message

1. **Load document**
   - Open document containing hidden message

2. **Find white text**
   - Scan all runs for white-colored text

3. **Extract and decrypt**
   - Collect all white text
   - Apply Vigenère decryption with key
   - Reveal original message

## Example Usage

```python
from main import hide_message_in_docx, extract_message_from_docx

# Hide a message
hide_message_in_docx(
    template_path="template.docx",
    fake_message_path="fakeMessage.docx",
    secret_message="MEET AT MIDNIGHT",
    key="SECRETKEY",
    output_path="output.docx"
)

# Extract the message
result = extract_message_from_docx("output.docx", "SECRETKEY")
print(f"Hidden message: {result['decrypted']}")
```

## Vigenère Cipher

### How It Works

The Vigenère cipher uses a repeating key to shift each letter:

```
Plaintext:  A T T A C K A T D A W N
Key:        S E C R E T S E C R E T
Shift:      18 4 2 17 4 19 18 4 2 17 4 19
Ciphertext: S X V R G D S X F R A G
```

### Example

- **Plaintext**: "ATTACK AT DAWN"
- **Key**: "SECRET"
- **Ciphertext**: "SXVRGG SW UOVN"

## Requirements

- Python 3.6+
- `python-docx` library
  ```bash
  pip install python-docx
  ```

## Security Notes

⚠️ **Important:**
- This is for educational purposes
- Vigenère cipher is historically weak
- Frequency analysis can break it
- For real security, use modern encryption (AES, RSA)
- Steganography alone (hiding + white text) is not secure

## Advanced Usage

### Custom Encryption Key
```python
hide_message_in_docx(
    "template.docx",
    "fakeMessage.docx",
    "SECRET MESSAGE",
    key="MYKEY123",  # Use strong key
    output_path="hidden.docx"
)
```

### Frequency Analysis
```python
from cipher import VigenereCipher

cipher = VigenereCipher()
frequencies = cipher.analyze_frequency("SXVRGG SW UOVN")
print(frequencies)
```

## Testing

Run the test in main.py:
```bash
python main.py
```

This will:
1. Create sample documents
2. Hide "ATTACK AT DAWN" with key "SECRET"
3. Extract and display the hidden message

## License

Educational Purpose Only

## Author

Created for learning cryptography and steganography concepts.
