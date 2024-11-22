import random
import os
import pickle
import time
import pyfiglet

def display_ascii_art():
    ascii_art = """
 _____ ______   ___  ______  _   __ _      _____  _____ 
/  ___|| ___ \ / _ \ | ___ \| | / /| |    |  ___||  ___|
\ `--. | |_/ // /_\ \| |_/ /| |/ / | |    | |__  | |__  
 `--. \|  __/ |  _  ||    / |    \ | |    |  __| |  __| 
/\__/ /| |    | | | || |\ \ | |\  \| |____| |___ | |___ 
\____/ \_|    \_| |_/\_| \_|\_| \_/\_____/\____/ \____/ 

    """
    print(ascii_art)

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

def generate_encryption_map(unique_chars):
    """Generate a mapping of unique characters to special characters."""
    special_chars = list("~!@#$%^&*()_+|{}:<>?,./;'[]\\=")
    if len(unique_chars) > len(special_chars):
        raise ValueError("Not enough special characters for encryption.")
    random.shuffle(special_chars)  # Shuffle to ensure randomness
    return {char: special_chars[i] for i, char in enumerate(unique_chars)}

def encrypt_string(input_string, encryption_map):
    """Encrypt the input string using the encryption map."""
    encrypted = []
    for char in input_string:
        if char == " ":
            encrypted.append(" ")  # Preserve spaces
        else:
            encrypted.append(encryption_map.get(char, char))  # Encrypt character
    return "".join(encrypted)

def decrypt_string(encrypted_string, decryption_map):
    """Decrypt the string using the decryption map."""
    decrypted = []
    for char in encrypted_string:
        if char == " ":
            decrypted.append(" ")  # Preserve spaces
        else:
            decrypted.append(decryption_map.get(char, char))  # Decrypt character
    return "".join(decrypted)

def save_map(encryption_map, filename):
    """Save the encryption map to a file using pickle."""
    with open(filename, 'wb') as file:
        pickle.dump(encryption_map, file)

def load_map(filename):
    """Load the decryption map from a file."""
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    else:
        return {}

def main():
    display_ascii_art()  # Display ASCII art when the program starts

    print("Select an option:")
    print("1. Encrypt a string")
    print("2. Decrypt a string")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        # Encrypt mode
        input_string = input("Enter a sentence or word to encrypt: ")

        # Generate ASCII art for the string
        ascii_art = generate_ascii_art(input_string)
        print(f"\nGenerated ASCII Art for '{input_string}':\n")
        print(ascii_art)

        unique_chars = list(set(input_string.replace(" ", "")))  # Get unique characters
        encryption_map = generate_encryption_map(unique_chars)  # Generate encryption map
        encrypted_string = encrypt_string(input_string, encryption_map)

        # Create a unique filename for the map (based on timestamp)
        timestamp = int(time.time())  # Using the current timestamp as a unique ID
        map_filename = f'encryption_map_{timestamp}.pkl'

        # Save the encryption map for later decryption
        save_map(encryption_map, map_filename)

        print(f"\nEncryption Map saved to '{map_filename}'.")
        print(f"\nEncrypted String: {encrypted_string}")

    elif choice == "2":
        # Decrypt mode
        print("Available encryption maps:")
        # List all map files in the current directory
        map_files = [f for f in os.listdir() if f.startswith('encryption_map_') and f.endswith('.pkl')]

        if not map_files:
            print("No saved encryption maps found. Please encrypt a string first.")
            return

        # Display available map files
        for idx, map_file in enumerate(map_files, start=1):
            print(f"{idx}. {map_file}")

        map_choice = int(input("\nSelect the map to use for decryption (1/2/...): ").strip()) - 1

        if map_choice < 0 or map_choice >= len(map_files):
            print("Invalid choice. Please select a valid map.")
            return

        selected_map_filename = map_files[map_choice]
        decryption_map = load_map(selected_map_filename)

        # Reverse the encryption map to create the decryption map
        reversed_decryption_map = {v: k for k, v in decryption_map.items()}

        encrypted_string = input("Enter the encrypted string to decrypt: ")
        decrypted_string = decrypt_string(encrypted_string, reversed_decryption_map)
        print(f"\nDecrypted String: {decrypted_string}")

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
