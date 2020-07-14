from colorama import Style, Fore, Back


def welcome():
    print(f"\n\t\t\t\t{Fore.GREEN}Welcome to Crypt\n")
    print(
        f"\t\t\t{Fore.CYAN}  A simple encryptor/decryptor{Style.RESET_ALL}\n")
    #print(f"\n{Back.RED}Disclaimer!!!\nThis program should never be used to encrypt sensitive information. It's only purpose is for me to learn cryptographic algorithms{Style.RESET_ALL}")


def banner():
    """
    Looks messy but it prints a cool loking banner with big letters and different color for letter and background
    """
    banner = fr'''
{Fore.CYAN}________{Fore.GREEN}/\\\\\\\\\{Fore.CYAN}_________________________________________________________
 _____{Fore.GREEN}/\\\///////{Fore.CYAN}___________________________________________________________
  ___{Fore.GREEN}/\\\/{Fore.CYAN}____________________________{Fore.GREEN}/\\\{Fore.CYAN}__{Fore.GREEN}/\\\{Fore.CYAN}___{Fore.GREEN}/\\\\\\\\\{Fore.CYAN}______{Fore.GREEN}/\\\{Fore.CYAN}______
   __{Fore.GREEN}/\\\{Fore.CYAN}______________{Fore.GREEN}/\\/\\\\\\\{Fore.CYAN}____{Fore.GREEN}\//\\\/\\\{Fore.CYAN}___{Fore.GREEN}/\\\/////\\\{Fore.CYAN}__{Fore.GREEN}/\\\\\\\\\\\{Fore.CYAN}_
    _{Fore.GREEN}\/\\\{Fore.CYAN}_____________{Fore.GREEN}\/\\\/////\\\{Fore.CYAN}____{Fore.GREEN}\//\\\\\{Fore.CYAN}___{Fore.GREEN}\/\\\\\\\\\\{Fore.CYAN}__{Fore.GREEN}\////\\\////{Fore.CYAN}__
     _{Fore.GREEN}\//\\\{Fore.CYAN}____________{Fore.GREEN}\/\\\{Fore.CYAN}___{Fore.GREEN}\///{Fore.CYAN}______{Fore.GREEN}\//\\\{Fore.CYAN}____{Fore.GREEN}\/\\\//////{Fore.CYAN}______{Fore.GREEN}\/\\\{Fore.CYAN}______
      __{Fore.GREEN}\///\\\{Fore.CYAN}__________{Fore.GREEN}\/\\\{Fore.CYAN}__________{Fore.GREEN}/\\{Fore.CYAN}_{Fore.GREEN}/\\\{Fore.CYAN}_____{Fore.GREEN}\/\\\{Fore.CYAN}____________{Fore.GREEN}\/\\\{Fore.CYAN}_{Fore.GREEN}/\\{Fore.CYAN}__
       ____{Fore.GREEN}\////\\\\\\\\\{Fore.CYAN}_{Fore.GREEN}\/\\\{Fore.CYAN}_________{Fore.GREEN}\//\\\\/{Fore.CYAN}______{Fore.GREEN}\/\\\{Fore.CYAN}____________{Fore.GREEN}\//\\\\\{Fore.CYAN}___
        _______{Fore.GREEN}\/////////{Fore.CYAN}__{Fore.GREEN}\///{Fore.CYAN}___________{Fore.GREEN}\////{Fore.CYAN}________{Fore.GREEN}\///{Fore.CYAN}______________{Fore.GREEN}\/////{Fore.CYAN}____
    '''

    print(banner)
