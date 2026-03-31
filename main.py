dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
         '1': 26, '2': 27, '3': 28, '4': 29, '5': 30, '6': 31}

dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z',
         26: '1', 27: '2', 28: '3', 29: '4', 30: '5', 31: '6'}

def affine_encrypt(text, a, b):
    if a % 2 == 0:
        raise ValueError("Key 'a' must be coprime with 32.")
    
    encrypted_message = ""
    for letter in text.upper():
        if letter in dict1:
            x = dict1[letter]
            shifted = ((a * x) % 32) ^ b
            encrypted_message += dict2[shifted]
        else:
            encrypted_message += letter
    return encrypted_message

def affine_decrypt(text, a, b):
    if a % 2 == 0:
        raise ValueError("Key 'a' must be coprime with 32.")
        
    decrypted_message = ""
    a_inv = pow(a, -1, 32) 
    
    for letter in text.upper():
        if letter in dict1:
            y = dict1[letter]
            shifted = (a_inv * (y ^ b)) % 32
            decrypted_message += dict2[shifted]
        else:
            decrypted_message += letter
    return decrypted_message

if __name__ == '__main__':
    original_message = "HELLO WORLD 123"
    
    affine_encrypted = affine_encrypt(original_message, 5, 8)
    affine_decrypted = affine_decrypt(affine_encrypted, 5, 8)
    
    print("Original Message:  ", original_message)
    print("Affine Encrypted:  ", affine_encrypted)
    print("Affine Decrypted:  ", affine_decrypted)
