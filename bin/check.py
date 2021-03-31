from bin import functions

from colorama import *
import os
import sys


class CHECK:
    def __init__(self):
        self.token = functions.read_file('user', 'token')

    def ctoken(self):
        if (functions.read_file('user', 'token') == ''):
        	print('------------------------------------------------------------------------------')
        	print(Style.BRIGHT + Fore.RED + '[ERROR] ' + Style.RESET_ALL + Style.BRIGHT + 'Er is geen token gevonden, vul je token éénmalig in!')
        	token = input()

        	functions.update_file('user', 'token', token)
        	os.system('cls')

    def ctarget(self):
        if (functions.read_file('constants', 'target') == ''):
            print('------------------------------------------------------------------------------')
            print(Style.BRIGHT + Fore.RED + ' - ' + Style.RESET_ALL + Style.BRIGHT + 'Vul target in!')
            token = input(' > ')
            functions.update_file('constants', 'target', token)
            os.system('cls')

            print('------------------------------------------------------------------------------')
            print(Style.BRIGHT + Fore.WHITE + ' - ' + Style.RESET_ALL + Style.BRIGHT + functions.read_file('constants', 'target'))
            print()
            print(Style.BRIGHT + Fore.GREEN + ' - ' + Style.RESET_ALL + Style.BRIGHT + ' Y = Yes | N = No')
            print()

            accep = input(' > ')

            if (accep == 'y'):
                pass
            else:
                sys.exit()

            os.system('cls')

    def cbullets(self):
        if (functions.read_file('constants', 'bullets') == ''):
            print('------------------------------------------------------------------------------')
            print(Style.BRIGHT + Fore.RED + ' - ' + Style.RESET_ALL + Style.BRIGHT + 'Vul aantal kogels in!')
            token2 = input(' > ')
            functions.update_file('constants', 'bullets', token2)

            os.system('cls')

            print('------------------------------------------------------------------------------')
            print(Style.BRIGHT + Fore.WHITE + ' - ' + Style.RESET_ALL + Style.BRIGHT + functions.format(int(functions.read_file('constants', 'bullets'))) + " kogels")
            print()
            print(Style.BRIGHT + Fore.GREEN + ' - ' + Style.RESET_ALL + Style.BRIGHT + ' Y = Yes | N = No')
            print()

            accep = input('> ')

            if (accep == 'y'):
                pass
            else:
                sys.exit()

            os.system('cls')

def check(option):
    c = CHECK()

    if (option == "token"):
         c.ctoken()
    elif (option == "target"):
         c.ctarget()
    elif (option == "bullets"):
         c.cbullets()
