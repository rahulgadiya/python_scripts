def caesar_cipher_encrypt(plaintext, key):
    encrypted_text = ''
    for char in plaintext:
        encrypted_char = char
        if char.isprintable():
            char_code = ord(char)
            if 32 <= char_code <= 126:  # Printable ASCII range
                if char.isupper():
                    shifted_char = chr((char_code - 32 + key) % 95 + 32)
                else:
                    shifted_char = chr((char_code - 32 + key) % 95 + 32)
                encrypted_char = shifted_char
        encrypted_text += encrypted_char
    return encrypted_text

def xor_cipher_encrypt(plaintext, key):
    encrypted_text = ''
    for char in plaintext:
        encrypted_char = char
        char_code = ord(char)  # Get the ASCII code of the character
        encrypted_char = chr(char_code ^ key)  # Perform XOR operation
        encrypted_text += encrypted_char
    return encrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    
    # Get block cipher key (Caesar cipher)
    while True:
        block_key_input = input("Enter the key for the Caesar cipher (integer): ")
        try:
            block_key = int(block_key_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Get stream cipher key (XOR cipher)
    while True:
        stream_key_input = input("Enter the key for the XOR cipher (integer): ")
        try:
            stream_key = int(stream_key_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Perform encryption using Caesar cipher (Block Cipher)
    encrypted_caesar = caesar_cipher_encrypt(plaintext, block_key)
    print(f"Encrypted text using Caesar cipher (Block Cipher): {encrypted_caesar}")

    # Perform encryption using XOR cipher (Stream Cipher)
    encrypted_xor = xor_cipher_encrypt(plaintext, stream_key)
    print(f"Encrypted text using XOR cipher (Stream Cipher): {encrypted_xor}")

if __name__ == "__main__":
    main()
