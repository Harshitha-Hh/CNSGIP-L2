def create_cipher_dict(key):
    """Create a dictionary for substitution cipher based on the provided key."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    return dict(zip(alphabet, key))

def create_inverse_cipher_dict(key):
    """Create the inverse of the substitution cipher dictionary for decryption."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    return dict(zip(key, alphabet))

def encrypt(plaintext, key):
    """Encrypt the plaintext using the substitution cipher."""
    cipher_dict = create_cipher_dict(key)
    plaintext = plaintext.lower()
    ciphertext = ''.join(cipher_dict.get(char, char) for char in plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the substitution cipher."""
    inverse_cipher_dict = create_inverse_cipher_dict(key)
    ciphertext = ciphertext.lower()
    plaintext = ''.join(inverse_cipher_dict.get(char, char) for char in ciphertext)
    return plaintext

# Example usage:
if __name__ == "__main__":
    key = "phqgiumeaylnofdxjkrcvstzwb"  # Example key (26 characters long)
    plaintext = "hello world"
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)
    
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted text: {decrypted_text}")
