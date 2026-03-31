import math

def affine_encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    encrypted_message = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            x = ord(char) - start
            shifted = (a * x + b) % 26
            encrypted_message += chr(shifted + start)
        else:
            encrypted_message += char
    return encrypted_message

def affine_decrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
        
    decrypted_message = ""
    # pow(a, -1, 26) automatically finds the modular inverse of 'a'
    a_inv = pow(a, -1, 26) 
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            y = ord(char) - start
            shifted = (a_inv * (y - b)) % 26
            decrypted_message += chr(shifted + start)
        else:
            decrypted_message += char
    return decrypted_message

if __name__ == "__main__":
    original_message = "Affine Cipher Test!"
    # Using key a=5, b=8
    
    encrypted = affine_encrypt(original_message, 5, 8)
    decrypted = affine_decrypt(encrypted, 5, 8)
    
    print("Original: ", original_message)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
