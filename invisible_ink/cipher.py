"""Vigenère Cipher Utilities for Invisible Ink Project"""


class VigenereCipher:
    """Vigenère cipher for encrypting/decrypting messages."""
    
    @staticmethod
    def encrypt(plaintext, key):
        """
        Encrypt plaintext using Vigenère cipher.
        
        Args:
            plaintext (str): Message to encrypt
            key (str): Encryption key
        
        Returns:
            str: Encrypted message
        """
        ciphertext = []
        key = key.upper()
        key_index = 0
        
        for char in plaintext.upper():
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                ciphertext.append(encrypted_char)
                key_index += 1
            else:
                ciphertext.append(char)
        
        return ''.join(ciphertext)
    
    @staticmethod
    def decrypt(ciphertext, key):
        """
        Decrypt ciphertext using Vigenère cipher.
        
        Args:
            ciphertext (str): Message to decrypt
            key (str): Decryption key
        
        Returns:
            str: Decrypted message
        """
        plaintext = []
        key = key.upper()
        key_index = 0
        
        for char in ciphertext.upper():
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                plaintext.append(decrypted_char)
                key_index += 1
            else:
                plaintext.append(char)
        
        return ''.join(plaintext)
    
    @staticmethod
    def analyze_frequency(text):
        """
        Analyze character frequency in text.
        
        Args:
            text (str): Text to analyze
        
        Returns:
            dict: Character frequencies
        """
        text = text.upper()
        freq = {}
        
        for char in text:
            if char.isalpha():
                freq[char] = freq.get(char, 0) + 1
        
        return sorted(freq.items(), key=lambda x: x[1], reverse=True)


# Test examples
if __name__ == "__main__":
    cipher = VigenereCipher()
    
    # Test encryption/decryption
    plaintext = "ATTACK AT DAWN"
    key = "SECRET"
    
    encrypted = cipher.encrypt(plaintext, key)
    decrypted = cipher.decrypt(encrypted, key)
    
    print(f"Original: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
