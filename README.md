# Affine Cipher

The Affine Cipher is a type of monoalphabetic substitution cipher. Unlike a simple shift cipher, it uses a mathematical function to map each letter to its new position by multiplying and adding to the letter's numerical value. 

## Algorithm Steps

It uses two secret keys, **a** and **b**. Key **a** must be "coprime" with 26 (meaning they share no common mathematical factors other than 1; valid keys include 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, and 25).

### Encryption
1. Convert each letter of the plaintext into a number from 0 to 25 (A=0, B=1... Z=25).
2. Apply the encryption formula: E(x) = (ax + b) mod 26.
3. Convert the resulting number back into a letter.
4. Leave non-letter characters unchanged.

### Decryption
1. Find the modular multiplicative inverse of key **a** (often denoted as a⁻¹).
2. Convert each encrypted letter into a number from 0 to 25.
3. Apply the decryption formula: D(x) = a⁻¹(x - b) mod 26.
4. Convert the resulting number back into a letter.
5. Leave non-letter characters unchanged.

## Code Explanation
The Python implementation translates the mathematical formulas directly into code to encrypt and decrypt the text:

* **Key Validation (`math.gcd(a, 26) != 1`):** The code first checks the Greatest Common Divisor of key **a** and 26. If it is not exactly 1, the script raises an error because the math will break, causing multiple letters to encrypt to the same character.
* **The Encryption Loop `(a * x + b) % 26`:** We scale the letters to a 0-25 range (represented by `x`). We multiply by key **a**, add key **b**, and use `% 26` to safely wrap the result around the 26-letter alphabet. 
* **The Decryption Loop `pow(a, -1, 26)`:** This built-in Python math function calculates the modular multiplicative inverse of key **a**. We then apply it to the reversed formula `(a_inv * (y - b)) % 26` to walk the math backward and reveal the original letter.
