def caesar_cipher_decrypt(encrypted_text, key):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - 65 - key) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 - key) % 26 + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def xor_cipher_decrypt(encrypted_text, key):
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_text += chr(ord(char) ^ key)
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
