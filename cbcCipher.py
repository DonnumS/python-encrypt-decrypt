
from Crypto.Cipher import AES
from cryptoFunctions import (
    pkcs7_pad_bytes, pkcs7_unpad_bytes, decodeHex, xor_byte_strings)


def decrypt_ecb_cipher(ciphertext, key):
    """Decrypts supplied ciphertext with supplied key using AES
    in ECB mode. Returns the decrypted data after unpadding.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return pkcs7_unpad_bytes(plaintext)


def encrypt_ecb_cipher(data, key):
    """Pads and encrypts supplied data with supplied key using AES
    in ECB mode. Returns the encrypted data.
    """
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pkcs7_pad_bytes(data, AES.block_size))
    return ciphertext


def encryptCBC(data, key, iv):
    """Implements AES CBC encryption.
    """
    ciphertext = b''
    previous_block_input = iv
    key = decodeHex(key)

    # Cycles through the data, one block at a time
    for i in range(0, len(data), AES.block_size):

        # Pads the current block
        plaintext_block = pkcs7_pad_bytes(
            data[i:i + AES.block_size], AES.block_size)

        # XORs the current block with the previous block. If it is
        # the first block it XORs with the iv value.
        xor_input = xor_byte_strings(plaintext_block, previous_block_input)

        # Encrypts the block using AES ECB and builds the ciphertext
        ecb_encrypted_block = encrypt_ecb_cipher(xor_input, key)
        ciphertext += ecb_encrypted_block

        # Sets the block to be XOR'd with for the next block
        previous_block_input = ecb_encrypted_block
    return ciphertext


def decryptCBC(data, key, iv):
    """Implements AES CBC decryption.
    """
    plaintext = b''
    previous_block_input = iv
    key = decodeHex(key)

    # Cycles through the data, one block at a time
    for i in range(0, len(data), AES.block_size):

        # The current encrypted block
        encrypted_block = data[i:i + AES.block_size]

        # Decrypts the block using AES ECB, and builds the plaintext
        decrypted_block = decrypt_ecb_cipher(encrypted_block, key)
        plaintext += xor_byte_strings(previous_block_input, decrypted_block)

        # Sets the block to be XOR'd with for the next block
        previous_block_input = encrypted_block
    return pkcs7_unpad_bytes(plaintext)
