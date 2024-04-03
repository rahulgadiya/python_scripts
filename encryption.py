import os
import random

def generate_random_key(keys_file):
    with open(keys_file, 'r') as f:
        keys = f.read().splitlines()
    key = random.choice(keys)
    print(f"Randomly chosen key: {key}")
    return key

def block_cipher_aes(key):
    os.system(f'openssl enc -aes-256-cbc -in plaintext.txt -out encrypted_aes.bin -pass pass:{key}')

def stream_cipher_rc4(key):
    os.system(f'openssl enc -rc4 -in plaintext.txt -out encrypted_rc4.bin -pass pass:{key}')

def asymmetric_encryption_rsa():
    os.system('openssl genrsa -out private.pem 2048')
    os.system('openssl rsa -pubout -in private.pem -out public.pem')
    os.system('openssl rsautl -encrypt -inkey public.pem -pubin -in plaintext.txt -out encrypted_rsa.bin')

def hash_function_sha256():
    os.system('openssl dgst -sha256 -binary plaintext.txt > hash_plaintext.sha256')

def main():
    keys_file = 'keys.txt'
    plaintext_file = 'plaintext.txt'
    
    # Generate random key
    key = generate_random_key(keys_file)

    # Perform encryption using block cipher (AES)
    block_cipher_aes(key)

    # Perform encryption using stream cipher (RC4)
    stream_cipher_rc4(key)

    # Perform asymmetric encryption (RSA)
    asymmetric_encryption_rsa()

    # Perform hash function (SHA-256)
    hash_function_sha256()

if __name__ == "__main__":
    main()
