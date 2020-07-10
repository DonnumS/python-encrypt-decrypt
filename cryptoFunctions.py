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


def generateRandomKey():
    key = get_random_bytes(16)
    return encodeHex(key)
