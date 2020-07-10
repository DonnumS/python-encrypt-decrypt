from cryptoFunctions import *
from termcolor import colored
from colorama import Fore, Style
import time
import sys
import itertools
import sys

spin = itertools.cycle([f'{Fore.RED}-{Style.RESET_ALL}', f'{Fore.RED}/{Style.RESET_ALL}',
                        f'{Fore.RED}|{Style.RESET_ALL}', f'{Fore.RED}\\{Style.RESET_ALL}'])


def spinner():
    counter = 0
    while True:
        sys.stdout.write(next(spin))   # write the next character
        sys.stdout.flush()                # flush stdout buffer (actual character display)
        sys.stdout.write(f'\b')            # erase the last written char
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
    print(f"\n\t\t\t\t{Fore.GREEN}Welcome to Crypt\n")
    print(
        f"\t\t\t{Fore.CYAN}  A simple encryptor/decryptor{Style.RESET_ALL}\n")


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
    print("Specify what type of format the message is\n1) hex\n2) base64")
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
    print("We will generate a random 16 byte key for you")
    print(f"{Fore.YELLOW}Write it down!!{Fore.WHITE}")
    time.sleep(2)
    spinner()
    key = generateRandomKey()
    print("Key is: ", colored(key, 'yellow'))
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


def banner():
    """
    Looks messy but it prints a cool loking banner with big letters and different color for letter and background
    """
    banner = fr'''
{Fore.CYAN}________{Fore.GREEN}/\\\\\\\\\{Fore.CYAN}_________________________________________________________
 _____{Fore.GREEN}/\\\///////{Fore.CYAN}__________________________________________________________
  ___{Fore.GREEN}/\\\/{Fore.CYAN}____________________________{Fore.GREEN}/\\\{Fore.CYAN}__{Fore.GREEN}/\\\{Fore.CYAN}___{Fore.GREEN}/\\\\\\\\\{Fore.CYAN}______{Fore.GREEN}/\\\{Fore.CYAN}______
   __{Fore.GREEN}/\\\{Fore.CYAN}______________{Fore.GREEN}/\\/\\\\\\\{Fore.CYAN}____{Fore.GREEN}\//\\\/\\\{Fore.CYAN}___{Fore.GREEN}/\\\/////\\\{Fore.CYAN}__{Fore.GREEN}/\\\\\\\\\\\{Fore.CYAN}_
    _{Fore.GREEN}\/\\\{Fore.CYAN}_____________{Fore.GREEN}\/\\\/////\\\{Fore.CYAN}____{Fore.GREEN}\//\\\\\{Fore.CYAN}___{Fore.GREEN}\/\\\\\\\\\\{Fore.CYAN}__{Fore.GREEN}\////\\\////{Fore.CYAN}__
     _{Fore.GREEN}\//\\\{Fore.CYAN}____________{Fore.GREEN}\/\\\{Fore.CYAN}___{Fore.GREEN}\///{Fore.CYAN}______{Fore.GREEN}\//\\\{Fore.CYAN}____{Fore.GREEN}\/\\\//////{Fore.CYAN}______{Fore.GREEN}\/\\\{Fore.CYAN}______
      __{Fore.GREEN}\///\\\{Fore.CYAN}__________{Fore.GREEN}\/\\\{Fore.CYAN}__________{Fore.GREEN}/\\{Fore.CYAN}_{Fore.GREEN}/\\\{Fore.CYAN}_____{Fore.GREEN}\/\\\{Fore.CYAN}____________{Fore.GREEN}\/\\\{Fore.CYAN}_{Fore.GREEN}/\\{Fore.CYAN}__
       ____{Fore.GREEN}\////\\\\\\\\\{Fore.CYAN}_{Fore.GREEN}\/\\\{Fore.CYAN}_________{Fore.GREEN}\//\\\\/{Fore.CYAN}______{Fore.GREEN}\/\\\{Fore.CYAN}____________{Fore.GREEN}\//\\\\\{Fore.CYAN}___
        _______{Fore.GREEN}\/////////{Fore.CYAN}__{Fore.GREEN}\///{Fore.CYAN}___________{Fore.GREEN}\////{Fore.CYAN}________{Fore.GREEN}\///{Fore.CYAN}______________{Fore.GREEN}\/////{Fore.CYAN}____
    '''

    print(colored(banner, 'green'))


def main():
    banner()
    menu()
    spinner()
    print("What type of encryption or decryption do you want to use?\n1) CBC\n2) Repeated XOR")
    ans = int(input("Specify: "))
    if ans == 1:
        print("\nDo you want to (1) decrypt or (2) encrypt?")
        action = int(input("Specify: "))

        if action == 1:
            cipher = decryptWithCBC()
        elif action == 2:
            cipher = encryptWithCBC()

    elif ans == 2:

        print("\nDo you want to (1) decrypt or (2) encrypt?")
        action = int(input("Specify: "))

        while(action > 2 or action < 1):
            print("Try again")
            action = int(input("Specify: "))
        if action == 1:
            cipher = decryptMessage()
        elif action == 2:
            cipher = encryptMessage()
        else:
            print("Choose 1 or 2")
            time.sleep(2)
            main()

    print("\nReady to return message")
    time.sleep(0.5)
    print(f"Here is your message encrypted/decrypted:\n{Fore.GREEN}")
    print(cipher)
    time.sleep(2)
    print(f"{Style.RESET_ALL}\nDo you want to run the program again?")
    again()


if __name__ == "__main__":
    main()
