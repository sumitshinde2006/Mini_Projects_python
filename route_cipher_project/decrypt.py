"""Core decryption logic for route cipher"""

def decrypt_route_cipher(cipher_text, routes):
    """
    Decrypt a route cipher using columnar transposition.
    
    Args:
        cipher_text (str): The encrypted text
        routes (list): Column order for decryption (e.g., [1, 4, 2, 5, 3, 6])
    
    Returns:
        str: The decrypted text
    """
    # Remove spaces and convert to uppercase
    cipher_text = cipher_text.replace(" ", "").upper()
    
    num_cols = len(routes)
    num_rows = (len(cipher_text) + num_cols - 1) // num_cols
    
    # Create grid with indices based on route order
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Fill grid column by column in route order
    idx = 0
    sorted_routes = sorted(enumerate(routes), key=lambda x: x[1])
    
    for _, route_val in sorted_routes:
        col = routes.index(route_val)
        for row in range(num_rows):
            if idx < len(cipher_text):
                grid[row][col] = cipher_text[idx]
                idx += 1
    
    # Read grid row by row to get original text
    decrypted = ""
    for row in grid:
        decrypted += ''.join(row)
    
    return decrypted.strip()
