
from colorama import Fore, Back, Style


def informationCBC():
    print('''
    CBC (cipher block chaining) is a mode of operation for a block cipher. 
    CBC uses in addition to the encryption key, an iv (initialization vector).

    A key characterisitc of CBC is its chaining mechanism. The decryption of 
    each block, depends on all the previous blocks. Therefore, a single 
    error in one of the blocks, causes the decryption of all the remaining 
    blocks to fail. The first block has no preceeding block, and that is
    why we need the iv
    ''')


def informationXOR():
    print('''
    The repeated XOR cipher is an extension of single-byte xor cipher.
    When it comes to single-byte xoring, it needs a 1 byte key.
    Lets say this key is "a". When encrypting ro decrypting,
    each letter of the plaintext is xored with this 1 byte key
    producing the result. 

    Repeated xor works in the same way, but we now use a longer
    key. This key can be "python". If we want to xor a plaintext 
    "Hello there" with this key. We first xor H and p, then e and 
    y then l and t and so on. When we have looped over the key, 
    we start a new loop over it. 

    All operations are performed on raw bytes, but in this program 
    we encode/decode using hex or base64.
    ''')


def informationSub():
    print('''
    Substitution cipher is a rather simple way of encrypting a message.
    The cipher encrypts or decrypts messages with the help of an alphabet
    key. The alphabet key is a key where all the letters in the alphabet
    is shuffled around. Say the key starts with ehi, that means that
    a is turned into e, b is turned into h and c is turned into i in the 
    ciphertext. In addition to small letters, we can also include upper 
    case letters and symbols to the key.

    If we only use lower case letters we get a key 26 unique letters. 
    Basically a shuffled alphabet. This gives 67,108,863 possible keys
    and you might think that implies a great cipher. But it is note the
    case. The fact that this is a simple substitution, means that letter
    combinations and frequencies can easily be discovered. For example 
    the word "the" is often easy to identify.  
    ''')


def informationCC():
    print('''
    A caesar cipher (CC) is a form of substitution cipher.
    The key in this cryptographic algorithm is an offset
    of the engliosh alphabet. 

    If the key is 10, the alphabet is shifted 10 places
    and used as a key when encrypting or decrypting. 
    The "Hi" becomes "Xy" since H and X share the same 
    index and i and y share the same index

    This is not a strong cipher, because it can easily
    be brute force solved

    Below you can see the example

    1  2  3  4  5  6  7  8  9  10 11 12 13 
    a  b  c  d  e  f  g  h  i  j  k  l  m  
    q  r  s  t  u  v  w  x y   z  a  b  c  
    --------------------------------------
    14 15 16 17 18 19 20 21 22 23 24 25 26
    n  o  p  q  r  s  t  u  v  w  x  y  z
    d  e  f  g  h  i  j  k  l  m  n  o  p
    ''')
