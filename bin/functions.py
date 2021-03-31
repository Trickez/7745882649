from colorama import *
import time
import locale



import configparser
import ctypes

import requests
import os

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
}


locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')


class file:
    def __init__(self, section, option):
        self.section = section
        self.option = option

        self.filelocation = 'data/database.ini'
        self.Ospath = os.path.exists(self.filelocation)
        self.config = configparser.ConfigParser()

    def check(self):
        if not self.Ospath:
            return False

    def read(self):
        if self.check() == False:
            log('critical', 'critical', 'No file in directory')
        else:
            try:
                self.config.read(self.filelocation)
                if self.config.has_option(self.section, self.option):
                    return self.config.get(self.section, self.option)
                else:
                    return 'section + option doesnt exists'
            except Exception as e:
                log('critical', 'critical', str(e))

    def update(self, new):
        if self.check() == False:
            log('critical', 'critical', 'No file in directory')
        else:
            try:
                self.config.read(self.filelocation)

                if self.config.has_option(self.section, self.option):

                    self.file = open(self.filelocation, 'w')
                    self.config.set(self.section, self.option, new)
                    self.config.write(self.file)
                    self.file.close()

                    return 'Update done!'
                else:
                    return 'section + option doesnt exists'
            except Exception as e:
                log('critical', 'critical', str(e))


def read_file(section, option):
    l = file(section, option)
    return l.read()


def update_file(section, option, new):
    l = file(section, option)
    return l.update(new)




def getTime():
	return time.strftime("%H:%M:%S")


class Log:
    def __init__(self, sort, message):
        self.sort = sort
        self.time = getTime()
        self.message = message

    def add(self):
        if (self.sort == '>'):
            print(f"- [{self.time}] {Style.BRIGHT}{Fore.LIGHTGREEN_EX}> {Style.RESET_ALL}{Style.BRIGHT} {self.message}{Style.RESET_ALL}")
        elif (self.sort == 'bank'):
            print(f"- [{self.time}] {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}[BANK]{Style.RESET_ALL}{Style.BRIGHT} {self.message}{Style.RESET_ALL}")
        elif (self.sort == 'check'):
            print(f"- [{self.time}] {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}[CHECK]{Style.RESET_ALL}{Style.BRIGHT} {self.message}{Style.RESET_ALL}")
        elif (self.sort == 'idle'):
            print(f"- [{self.time}] {Style.BRIGHT}[IDLE]{Style.RESET_ALL}{Style.BRIGHT} {self.message}{Style.RESET_ALL}")
        elif (self.sort == 'error'):
            print(f"- [{self.time}] {Style.BRIGHT}{Fore.LIGHTRED_EX}[ERROR]{Style.RESET_ALL}{Style.BRIGHT} {self.message}{Style.RESET_ALL}")
        elif (self.sort == 'bunker'):
            print(f"- [{self.time}] {Style.BRIGHT}{Fore.LIGHTBLUE_EX}[Bunker]{Style.RESET_ALL}{Style.BRIGHT} {self.message}{Style.RESET_ALL}")



def log(sort, message):
    l = Log(sort, message)
    l.add()



class URL:
    def __init__(self, base, path, data):
        self.headers = headers
        self.url = base
        self.session = requests.Session()
        #### input ####
        self.path = path
        self.data = data


    def post(self, path, data):
        self.post = self.session.post(self.url + self.path, data = self.data, headers = self.headers)
        return self.post

    def get(self, path):
        self.get = self.session.get(self.url + self.path, headers = self.headers)
        return self.get

def url (sort, base, path, data):
    url = URL(base, path, data)

    if (sort == "post"):
        return url.post(path, data)

    elif (sort == "get"):
        return url.get(path)

    else:
        print('error!')
        exit()


def format(value):
    return locale.format('%d', value, 1)
