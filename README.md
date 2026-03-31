# XOR Affine Cipher

The XOR Affine Cipher is an advanced substitution cipher that combines modular arithmetic with bitwise logical operations. It maps characters using an expanded 32-character dictionary (A-Z and 1-6) to ensure the mathematical transformations stay perfectly within bounds.

## Algorithm Steps

This cipher utilizes two keys: **a** (which must be coprime with the dictionary size, 32) and **b**.

### Encryption
1. Read the input message character by character and convert it to uppercase.
2. If the character exists in the dictionary, retrieve its numerical index (let's call it `x`).
3. Multiply `x` by key **a**, and apply the modulo 32 operator to keep the value within the dictionary limits.
4. Apply the bitwise XOR operator (`^`) between that result and key **b**.
5. Retrieve the new ciphertext character corresponding to the final index.
6. Retain all unsupported characters unchanged.

### Decryption
1. Calculate the modular multiplicative inverse of key **a** (let's call it `a_inv`) over modulo 32.
2. Read the ciphertext message character by character.
3. Retrieve the numerical index of the dictionary character (let's call it `y`).
4. Apply the bitwise XOR operator (`^`) between `y` and key **b**.
5. Multiply the result by `a_inv` and apply the modulo 32 operator.
6. Retrieve the original plaintext character corresponding to the final index.
7. Retain all unsupported characters unchanged.

## Hash Function Used

In this cipher, the **bitwise XOR operator (`^`)** acts as the secondary hashing mechanism, integrated directly into the Affine equation to replace traditional mathematical addition. 

By using XOR to hash the intermediate values, the cipher alters the data at the binary level. During encryption, the algorithm first maps the character using modular multiplication, and then hashes that intermediate result by XORing it against key **b** to produce the final ciphertext index. 

During decryption, because the XOR operation is its own mathematical inverse, the algorithm simply applies the exact same XOR transformation against key **b** first to un-hash the binary bits. This safely restores the intermediate value, allowing the modular arithmetic to correctly reverse the rest of the cipher.
