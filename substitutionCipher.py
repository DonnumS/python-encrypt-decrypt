import random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ abcdefghijklmnopqrstuvwxyz0123456789æøå \'\"."


def generateKey():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    flipped = {v: k for k, v in key.items()}
    return ''.join(flipped[l] for l in ciphertext)


def show_result(plaintext):
    """Generate a resulting cipher with elements shown"""
    key = generateKey()
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print('Key: %s' % key)
    print('Plaintext: %s' % plaintext)
    print('Encrypted: %s' % encrypted)
    print('Decrypted: %s' % decrypted)


show_result("Hello World. \'This is demo of substitution cipher")
