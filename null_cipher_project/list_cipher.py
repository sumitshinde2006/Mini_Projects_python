"""List Cipher - Creates hidden messages using word list vocabulary"""

import load_dictionary
import random


def create_list_cipher(hidden_message, word_list):
    """
    Create a list cipher by encoding message in word order.
    
    Each word in the word list whose first letter matches the hidden message
    character is selected. This creates a seemingly normal text that hides
    the actual message in the first letters of selected words.
    
    Args:
        hidden_message (str): Message to hide
        word_list (list): Available words to use
    
    Returns:
        str: Encoded list cipher
    """
    encoded = []
    
    for char in hidden_message.upper():
        # Find words starting with this character
        matching_words = [w for w in word_list if w[0].upper() == char]
        
        if matching_words:
            # Select random word starting with this character
            word = random.choice(matching_words)
            encoded.append(word)
        else:
            # If no word found, skip or use placeholder
            encoded.append(f"[{char}]")
    
    return " ".join(encoded)


def extract_list_cipher(encoded_text):
    """
    Extract hidden message from list cipher.
    
    Args:
        encoded_text (str): List cipher text
    
    Returns:
        str: Hidden message
    """
    words = encoded_text.split()
    message = ""
    
    for word in words:
        if word and word[0].isalpha():
            message += word[0]
    
    return message


def generate_sample_cipher():
    """Generate sample list cipher with dictionary."""
    # Load dictionary
    word_list = load_dictionary.load('2of4brif.txt')
    
    # Message to hide
    hidden_message = "HELLO"
    
    # Create cipher
    encoded = create_list_cipher(hidden_message, word_list)
    
    return hidden_message, encoded


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("List Cipher - Vocabulary-based Hidden Message Encoder")
    print("=" * 60)
    
    try:
        hidden, encoded = generate_sample_cipher()
        
        print(f"\nOriginal Message: {hidden}")
        print(f"\nEncoded Cipher: {encoded}")
        print(f"\nExtracted Message: {extract_list_cipher(encoded)}")
        
        print(f"\nHow it works:")
        print(f"- Each letter is represented by a word from the dictionary")
        print(f"- First letters spell out: {extract_list_cipher(encoded)}")
        
    except Exception as e:
        print(f"Error: {e}")
