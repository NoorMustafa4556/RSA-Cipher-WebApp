# [cite: 5]
import math
from random import randint, randrange
from typing import Tuple

def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean Algorithm. Returns (gcd, x, y) such that ax + by = gcd.""" # [cite: 5]
    if a == 0: # [cite: 5]
        return (b, 0, 1) # [cite: 5]
    else:
        g, x, y = egcd(b % a, a) # [cite: 5, 6]
        return (g, y - (b // a) * x, x) # [cite: 6]

def modinv(e: int, phi: int) -> int:
    """Calculates the modular multiplicative inverse of e modulo phi.""" # [cite: 6]
    g, x, _ = egcd(e, phi) # [cite: 6]
    if g != 1: # [cite: 6]
        # The inverse exists only if e and phi are coprime # [cite: 6]
        raise Exception("Modular inverse does not exist") # [cite: 6]
    # The inverse is x mod phi # [cite: 6]
    return x % phi # [cite: 6]

def is_probable_prime(n: int, k: int = 5) -> bool:
    """Miller-Rabin Primality Test to check if n is probably prime.""" # [cite: 6]
    if n < 2: # [cite: 6]
        return False # [cite: 7]
    # Check divisibility by small primes first for quick elimination # [cite: 7]
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]: # [cite: 7]
        if n % p == 0: # [cite: 7]
            return n == p # [cite: 7]
    
    # Miller-Rabin specific part
    s = 0 # [cite: 7]
    r = n - 1 # [cite: 7]
    while r % 2 == 0: # [cite: 7]
        r //= 2 # [cite: 7]
        s += 1 # [cite: 7]
    
    for _ in range(k): # Perform k iterations for higher certainty # [cite: 7]
        a = randint(2, n - 2) # Choose a random base a # [cite: 8]
        x = pow(a, r, n) # Calculate x = a^r mod n # [cite: 8]
        if x == 1 or x == n - 1: # [cite: 8]
            continue # Probably prime for this base, try next # [cite: 8]
        for _ in range(s - 1): # [cite: 8]
            x = pow(x, 2, n) # Square x # [cite: 8]
            if x == n - 1: # [cite: 8]
                break # Probably prime for this base, try next outer loop # [cite: 9]
        else:
             # If loop completes without break, n is composite # [cite: 9]
            return False # [cite: 9]
    return True # Passed k tests, probably prime # [cite: 9]

def generate_large_prime(bit_length: int = 18) -> int:
    """Generates a prime number with the specified bit length.""" # [cite: 9]
    # Using 18 bits ensures n = p*q is large enough for ord(char) < n # [cite: 10, 11]
    while True: # [cite: 11]
        # Generate a random number within the bit range # [cite: 11]
        candidate = randrange(2**(bit_length - 1), 2**bit_length) # [cite: 11]
        # Ensure it's odd # [cite: 11]
        if candidate % 2 == 0: # [cite: 11]
            candidate += 1 # [cite: 11]
        # Test for primality # [cite: 11]
        if is_probable_prime(candidate): # [cite: 11]
            return candidate # [cite: 11]

def generate_keys() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Generates an RSA key pair (public_key, private_key).""" # [cite: 11]
    bit_length = 18 # Using 18-bit primes [cite: 12]
    p = generate_large_prime(bit_length) # [cite: 12]
    q = generate_large_prime(bit_length) # [cite: 12]
    # Ensure p and q are different primes # [cite: 12]
    while q == p: # [cite: 12]
        q = generate_large_prime(bit_length) # [cite: 12]
    
    n = p * q # Calculate the modulus # [cite: 12]
    phi = (p - 1) * (q - 1) # Calculate Euler's totient function # [cite: 12]

    # Choose a public exponent 'e' from a predefined list
    # Using a small, fixed list simplifies the process and is common practice
    possible_es = [3, 5, 7, 11, 13, 17] # [cite: 12]
    e = -1 # Initialize e
    for candidate_e in possible_es: # [cite: 12]
        if math.gcd(candidate_e, phi) == 1: # e must be coprime to phi # [cite: 12, 13]
            e = candidate_e # [cite: 13]
            break # Found a suitable e # [cite: 13]
    else:
        # This should rarely happen with the chosen bit length and possible_es # [cite: 13]
        raise Exception("Failed to find a suitable public exponent (e).") # [cite: 13]

    # Calculate the private exponent 'd', the modular inverse of e mod phi # [cite: 13]
    d = modinv(e, phi) # [cite: 13]
    
    # Return public key (e, n) and private key (d, n) # [cite: 13]
    return ((e, n), (d, n)) # [cite: 13]

def encrypt(plaintext: str, public_key: Tuple[int, int]) -> str:
    """Encrypts a plaintext string using the public key (e, n).""" # [cite: 13]
    e, n = public_key # [cite: 15]
    ciphertext_parts = [] # [cite: 15]
    # Encrypt character by character # [cite: 14]
    for char in plaintext: # [cite: 15]
        m = ord(char) # Convert character to its ASCII/Unicode integer value # [cite: 15]
        # Ensure the numeric value of the character is less than n # [cite: 15]
        if m >= n: # [cite: 15]
            # This can happen if keys are too small or message contains unusual characters # [cite: 15]
            raise ValueError("Message character value is too large for the current key size (n). Please generate new, larger keys.") # [cite: 15]
        # RSA encryption formula: c = m^e mod n # [cite: 15]
        c = pow(m, e, n) # [cite: 15]
        ciphertext_parts.append(str(c)) # [cite: 15]
    # Join the encrypted numbers with commas for easy splitting during decryption # [cite: 15]
    return ",".join(ciphertext_parts) # [cite: 15]

def decrypt(ciphertext: str, private_key: Tuple[int, int]) -> str:
    """Decrypts a ciphertext string using the private key (d, n).""" # [cite: 15]
    d, n = private_key # [cite: 16]
    plaintext = "" # [cite: 16]
    # Split the comma-separated ciphertext back into individual numbers # [cite: 16]
    parts = ciphertext.split(",") # [cite: 16]
    for part in parts: # [cite: 16]
        part = part.strip() # Remove potential whitespace # [cite: 16]
        if not part: # Skip empty parts if they exist (e.g., trailing comma) # [cite: 16]
            continue # [cite: 16]
        try:
            c = int(part) # Convert the part back to an integer # [cite: 16]
        except ValueError:
            raise ValueError(f"Invalid ciphertext component: '{part}'. Ciphertext must be comma-separated numbers.")
        # RSA decryption formula: m = c^d mod n # [cite: 16]
        m = pow(c, d, n) # [cite: 16]
        try:
            plaintext += chr(m) # Convert the decrypted number back to a character # [cite: 16]
        except ValueError:
             # This could happen if decryption results in a value outside valid character range
            raise ValueError(f"Decrypted value {m} is not a valid character code.")
    return plaintext # [cite: 16]