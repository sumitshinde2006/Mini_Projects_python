"""Route Cipher Decryption Program - Main Entry Point"""

from config import CIPHER_TEXT, KEY_ROUTES
from decrypt import decrypt_route_cipher
from utils import validate_input, parse_routes

def main():
    """Run the route cipher decryption program."""
    print("=" * 50)
    print("Route Cipher Decryption Program")
    print("=" * 50)
    
    # Validate input
    if not validate_input(CIPHER_TEXT, KEY_ROUTES):
        print("Error: Invalid configuration in config.py")
        return
    
    # Parse routes
    routes = parse_routes(KEY_ROUTES)
    
    # Decrypt
    try:
        decrypted = decrypt_route_cipher(CIPHER_TEXT, routes)
        print(f"\nCipher Text: {CIPHER_TEXT}")
        print(f"Key Routes: {KEY_ROUTES}")
        print(f"Decrypted Text: {decrypted}")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    main()
