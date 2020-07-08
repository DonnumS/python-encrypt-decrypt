from cryptoFunctions import *
import time
import sys

import itertools
import sys

spin = itertools.cycle(['-', '/', '|', '\\'])


def spinner():
    counter = 0
    while True:
        sys.stdout.write(next(spin))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write('\b')            # erase the last written char
        if counter == 19:
            sys.stdout.write('\b')
            break
        counter += 1
        time.sleep(0.1)


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)


def menu():
    print("\nWelcome to the encryptor/decryptor\n\n")
    print("This program will encrypt or decrypt your message\n")


def performDecode(msg, mode):
    if (mode == 1):
        msg = decodeHex(msg)
    elif (mode == 2):
        msg = decodeB64(msg)
    return msg


def performEncode(msg, mode):
    if (mode == 1):
        msg = encodeHex(msg)
    elif (mode == 2):
        msg = encodeB64(msg)

    return msg


def decryptMessage():
    print("Specify what type of format the message is\n1) hex\n2)base64")
    typeData = int(input("Specify: "))
    message = input("\n\nType in what you want decrypted: ")
    print("\nType in the same key that was used to encrypt")
    k = input("Type in your key: ")

    print("Turning message into bytes")
    spinner()
    # decode the data
    if type(message) == str:
        message = message.encode()
    data = performDecode(message, typeData)

    key = k.encode()
    print("\nGetting xored bytes")
    spinner()

    cipher = repeatingKeyXor(data, key)

    print("\nFinishing xor process")
    spinner()
    return cipher


def encryptMessage():
    print("Specify what type of format you want the enxrypted message in\n1) hex\n2)base64")
    typeData = int(input("Specify: "))
    message = input("\n\nType in what you want encrypted: ")
    print("\nType in the key you want to use for encryption")
    k = input("Type in your key: ")

    if type(message) == str:
        message = message.encode()

    key = k.encode()
    print("\nGetting xored bytes")
    spinner()

    cipher = repeatingKeyXor(message, key)

    print("\nFinishing xor process")
    spinner()

    data = performEncode(cipher, typeData)

    return data


def again():
    ans = input("(y/n) ")

    if(ans == 'y'):
        main()
    elif(ans == 'n'):
        return
    else:
        print("choose y or n")
        again()


def main():
    menu()
    print("Do you want to (1) decrypt or (2) encrypt?")
    action = int(input("Specify 1/2: "))

    if action == 1:
        cipher = decryptMessage()
    elif action == 2:
        cipher = encryptMessage()
    else:
        print("Choose 1 or 2")
        time.sleep(2)
        main()

    print("Ready to return message")
    spinner()
    print("Here is your message encrypted/decrypted:\n")
    print(cipher)
    time.sleep(2)
    print("Do you want to run the program again?")
    again()


if __name__ == "__main__":
    print(decodeHex("54686973206973206120736563726574206d657373616765"))
    main()
