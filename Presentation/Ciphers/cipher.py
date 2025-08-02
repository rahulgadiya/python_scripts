def caesar_cipher_encrypt(plaintext, key):
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 + key) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def xor_cipher_encrypt(plaintext, key):
    encrypted_text = ''
    for char in plaintext:
        encrypted_text += chr(ord(char) ^ key)
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
