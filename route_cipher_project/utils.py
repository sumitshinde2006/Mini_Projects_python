"""Helper functions for validation and key parsing"""

def validate_input(cipher_text, key_routes):
    """
    Validate cipher text and key routes.
    
    Args:
        cipher_text (str): The text to validate
        key_routes (str/list): The routes to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(cipher_text, str) or not cipher_text:
        print("Error: Cipher text must be a non-empty string")
        return False
    
    if not key_routes:
        print("Error: Key routes cannot be empty")
        return False
    
    return True


def parse_routes(key_routes):
    """
    Parse key routes from various formats.
    
    Args:
        key_routes (str or list): Routes in string or list format
                                 Example: "1,2,3,4" or [1,2,3,4]
    
    Returns:
        list: Parsed routes as a list
    """
    if isinstance(key_routes, str):
        # Parse comma-separated string
        try:
            routes = [int(x.strip()) for x in key_routes.split(",")]
        except ValueError:
            print("Error: Could not parse routes as integers")
            return []
    elif isinstance(key_routes, (list, tuple)):
        routes = list(key_routes)
    else:
        print("Error: Key routes must be string or list")
        return []
    
    return routes


def format_output(text, width=80):
    """
    Format output text for display.
    
    Args:
        text (str): Text to format
        width (int): Maximum line width
    
    Returns:
        str: Formatted text
    """
    lines = []
    for i in range(0, len(text), width):
        lines.append(text[i:i+width])
    return "\n".join(lines)
