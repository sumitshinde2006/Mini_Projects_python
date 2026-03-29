"""Null Cipher Finder - Extracts hidden messages from punctuation"""

def find_null_cipher(text, method='punctuation'):
    """
    Find hidden message in null cipher using punctuation.
    
    Methods:
    - 'punctuation': First letter after punctuation marks
    - 'capitalization': Capital letters spell out message
    - 'word_positions': Hidden word at specific positions
    
    Args:
        text (str): Encoded message text
        method (str): Decryption method to use
    
    Returns:
        str: Hidden message
    """
    hidden_message = ""
    
    if method == 'punctuation':
        # Extract first letter after punctuation marks
        in_message = False
        for i, char in enumerate(text):
            if char in '.,!?;:':
                in_message = True
            elif in_message and char.isalpha():
                hidden_message += char
                in_message = False
    
    elif method == 'capitalization':
        # Extract capital letters
        for char in text:
            if char.isupper() and char.isalpha():
                hidden_message += char
    
    elif method == 'word_positions':
        # Extract specific word positions
        words = text.split()
        # Example: every 2nd word first letter
        for i in range(1, len(words), 2):
            if words[i] and words[i][0].isalpha():
                hidden_message += words[i][0]
    
    return hidden_message


def analyze_cipher_file(filename):
    """
    Analyze a cipher file for hidden messages.
    
    Args:
        filename (str): Path to cipher file
    
    Returns:
        dict: Results from different decryption methods
    """
    try:
        with open(filename, 'r') as f:
            text = f.read()
        
        results = {
            'original': text[:100] + '...' if len(text) > 100 else text,
            'punctuation': find_null_cipher(text, 'punctuation'),
            'capitalization': find_null_cipher(text, 'capitalization'),
            'word_positions': find_null_cipher(text, 'word_positions'),
        }
        return results
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return {}


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Null Cipher Finder - Extract Hidden Messages")
    print("=" * 60)
    
    # Analyze trevanion.txt
    results = analyze_cipher_file('trevanion.txt')
    
    if results:
        print("\nCipher File Analysis:")
        print(f"Original text: {results['original']}")
        print(f"\nPunctuation method: {results['punctuation']}")
        print(f"Capitalization method: {results['capitalization']}")
        print(f"Word position method: {results['word_positions']}")
