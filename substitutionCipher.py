import random


def makeKey():
    alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)


def encryptSub(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)


def decryptSub(cipher, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

