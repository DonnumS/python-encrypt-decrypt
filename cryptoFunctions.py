import base64
import urllib.parse
import os
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encodeHex(input_bytes):
    """Returns a hex encoded byte string"""
    if type(input_bytes) == str:
        input_bytes = input_bytes.encode()
    return input_bytes.hex().encode()


def encodeB64(input_bytes):
    """Performs Base64 encoding"""
    if type(input_bytes) == str:
        input_bytes = input_bytes.encode()
    return base64.b64encode(input_bytes)


def decodeHex(input_string):
    """Returns a hex decoded byte string"""
    if type(input_string) == bytes:
        input_string = input_string.decode()
    return bytes.fromhex(input_string)


def decodeB64(input_bytes):
    """Performs Base64 decoding"""
    if type(input_bytes) == str:
        input_bytes = input_bytes.encode()
    return base64.b64decode(input_bytes)


def repeatingKeyXor(message_bytes, key):
    """Returns message XOR'd with a key. If the message, is longer
    than the key, the key will repeat.
    """
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


def pkcs7_pad_bytes(input_bytes, block_size):
    """Returns the input bytes padded to the block size using pkcs7 
    padding.
    """
    if len(input_bytes) == block_size:
        return input_bytes
    padding_length = block_size - len(input_bytes) % block_size
    padding = bytes([padding_length] * padding_length)
    return input_bytes + padding


def pkcs7_unpad_bytes(input_bytes):
    """Returns the input_bytes with pkcs7 padding removed.
    """
    # Strips off what is expected to be the bytes by
    padding = input_bytes[-input_bytes[-1]:]
    if not all(padding[byte] == len(padding) for byte in range(0, len(padding))):
        return input_bytes
    return input_bytes[:-input_bytes[-1]]


def xor_byte_strings(input_bytes_1, input_bytes_2):
    """XOR two byte strings together.
    """
    return bytes([b1 ^ b2 for b1, b2 in zip(input_bytes_1, input_bytes_2)])


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


def generateRandomKey():
    key = get_random_bytes(16)
    return encodeHex(key)


key = generateRandomKey()
print("This is the key: {}".format(key))
