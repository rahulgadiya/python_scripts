def caesar_cipher_decrypt(encrypted_text, key):
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_char = char
        if char.isprintable():
            char_code = ord(char)
            if 32 <= char_code <= 126:  # Printable ASCII range
                if char.isupper():
                    shifted_char = chr((char_code - 32 - key) % 95 + 32)
                else:
                    shifted_char = chr((char_code - 32 - key) % 95 + 32)
                decrypted_char = shifted_char
        decrypted_text += decrypted_char
    return decrypted_text

def xor_cipher_decrypt(encrypted_text, key):
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_char = char
        char_code = ord(char)  # Get the ASCII code of the character
        decrypted_char = chr(char_code ^ key)  # Perform XOR operation
        decrypted_text += decrypted_char
    return decrypted_text

def main():
    encrypted_caesar = input("Enter the encrypted text using Caesar cipher: ")
    block_key = int(input("Enter the key for the Caesar cipher (integer): "))

    encrypted_xor = input("Enter the encrypted text using XOR cipher: ")
    stream_key = int(input("Enter the key for the XOR cipher (integer): "))

    # Perform decryption using Caesar cipher (Block Cipher)
    decrypted_caesar = caesar_cipher_decrypt(encrypted_caesar, block_key)
    print(f"Decrypted text using Caesar cipher (Block Cipher): {decrypted_caesar}")

    # Perform decryption using XOR cipher (Stream Cipher)
    decrypted_xor = xor_cipher_decrypt(encrypted_xor, stream_key)
    print(f"Decrypted text using XOR cipher (Stream Cipher): {decrypted_xor}")

if __name__ == "__main__":
    main()

