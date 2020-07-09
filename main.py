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
    print("Specify what type of format you want the enxrypted message in\n1) hex\n2) base64")
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


def decryptWithCBC():
    time.sleep(0.5)
    message = input("\n\nType in what you want decrypted: ")
    message = decodeHex(message)
    if type(message) == str:
        message = message.encode()

    key = input("Type in key used for the encryption: ")

    iv = b'\x00' * AES.block_size
    decrypted = decryptCBC(message, key, iv)
    return(decrypted)


def encryptWithCBC():
    time.sleep(0.5)
    print("We will generate a random 16 byte key for you\nWrite it down!")
    time.sleep(2)
    spinner()
    key = generateRandomKey()
    print("Key is: {}".format(key))
    iv = b'\x00' * AES.block_size
    time.sleep(1)
    message = input("\n\nType in what you want encrypted: ")
    if type(message) == str:
        message = message.encode()

    encrypted = encryptCBC(message, key, iv)
    return(encodeHex(encrypted))


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
    print("What type of encryption/decryptino do you want to use?\n1)CBC\n2)Repeated XOR")
    ans = int(input("Specify 1 or 2: "))
    if ans == 1:
        print("Do you want to (1) decrypt or (2) encrypt?")
        action = int(input("Specify 1 2: "))

        if action == 1:
            cipher = decryptWithCBC()
        elif action == 2:
            cipher = encryptWithCBC()

    elif ans == 2:

        print("Do you want to (1) decrypt or (2) encrypt?")
        action = int(input("Specify 1 2: "))

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


"""
be0b7244cf593987839c02a90153c90b
67af251f50f3a8b9781ff70f08642a436cc7df293752485b74aa9fccc80da810093e3182fe5a938d1084e8fa65b2b22f

2362ed5c7511c7a1306cd0901ae278b4

c8dfef83f07a223cf6c28b9adaff33ff848892fbd272b8d190c2c5ddaeea04d09c3e5c62f0c6c7606b106c7db418d545975011bd7d9d559afd11b03c258a9d21c0c77b7b04a18042b8869898b11490f14083467d762946f0965dde097f32e69904c77f6ee2fa79bc1899ebb6ff3921de56d974963e87ce7f00381536cab9446f4731ec0d8231e802249d6ddda38b6fb800bc4d0f8788e80014139977f8fe6a79

"""
