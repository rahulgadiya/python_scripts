	import os

def block_cipher_aes_decrypt(key):
    os.system(f'openssl enc -d -aes-256-cbc -in encrypted_aes.bin -out decrypted_aes.txt -pass pass:{key}')

def stream_cipher_rc4_decrypt(key):
    os.system(f'openssl enc -d -rc4 -in encrypted_rc4.bin -out decrypted_rc4.txt -pass pass:{key}')

def asymmetric_decryption_rsa():
    os.system('openssl rsautl -decrypt -inkey private.pem -in encrypted_rsa.bin -out decrypted_rsa.txt')

def main():
    key = input("Enter the key for decryption: ")

    # Perform decryption using block cipher (AES)
    block_cipher_aes_decrypt(key)

    # Perform decryption using stream cipher (RC4)
    stream_cipher_rc4_decrypt(key)

    # Perform asymmetric decryption (RSA)
    asymmetric_decryption_rsa()

if __name__ == "__main__":
    main()
		
