from colorama import *
from win10toast import ToastNotifier

import os
import json
import time
import random


from bin import functions as func
from bin import check

import threading

if (func.read_file('settings', 'local')):
    website = func.read_file('website', 'local')
    api = func.read_file('api', 'local')
else:
    website = func.read_file('website', 'live')
    api = func.read_file('api', 'live')



start_time = time.time()
toast = ToastNotifier()

stop = []

class Run:
    def __init__(self):
        if (func.read_file('settings', 'local')):
            self.token = func.read_file('user', 'tokenLocal')
        else:
            self.token = func.read_file('user', 'token')

        self.website = website
        self.api = api
        self.health = func.read_file('info', 'health')
        self.cash = func.read_file('info', 'cash')
        self.bank = func.read_file('info', 'bank')
        self.captcha = func.read_file('info', 'captcha')


    def info(self):
        try:
            II = func.url('get', self.api, 'me?token=' + self.token, '').json()

            microTime = round(time.time() * 1000)
            bunkerTime = str(II['bunkerAt'])
            total = round((int(bunkerTime) - microTime) / 1000)

            func.update_file('info', 'bunker', str(total))
            func.update_file('info', 'health', str(II['health']))
            func.update_file('info', 'cash', str(II['cash']))
            func.update_file('info', 'bank', str(II['bank']))
            func.update_file('info', 'captcha', str(II['needCaptcha']))

        except Exception as e:
            func.log('error', e)

    def check(self):
        try:
            if (int(self.health) <= 0):
                stop.append('true')
                func.log('check', "Health - Je bent vermoord - System stopted")
                toast.show_toast("Mastercrimez - Health","Je bent vermoord! Stopping bot", duration=10)

            if (int(self.cash) <= 1000000):
                if (int(self.bank) >= 1000000):
                    if (int(self.bank) <= 20000000):
                        self.banker(False, int(self.bank))
                    else:
                        self.banker(False, 20000000)
                else:
                    stop.append('true')
                    func.log('check', "Cash - Je hebt teweinig geld op bank. - System stopted")
                    toast.show_toast("Mastercrimez - Banker","Je hebt teweinig geld op bank", duration=10)




        except Exception as e:
            func.log('error', e)

    def bunker(self):
        try:
            data = {
                "token": str(self.token),
                "option": 3,
                "captcha":""
            }

            II = func.url('post', self.api, 'bunker', data).json()
            response = II['response']

            if (self.captcha == 'True'):
                stop.append('true')
                func.log('bunker', "Captcha - system stopted")
                toast.show_toast("Mastercrimez - captcha","Captcha! Failed stopping bot", duration=10)
            else:
                func.log('bunker', 'Je bent ondergedoken voor 900 seconden.')

        except Exception as e:
            func.log('error', e)

    def banker(self, stort, amount):
        try:
            if (stort):
                data = {
                    "amount": str(amount),
                    "deposit": "true",
                    "token": str(self.token)
                }
            else:
                data = {
                    "amount": str(amount),
                    "token": str(self.token)
                }

            II = func.url('post', self.api, 'bank', data).json()
            response = II['response']

            if 'Je hebt niet zoveel' in response:
                stop.append('true')
                func.log('banker', "Banker - Je hebt teweinig geld op bank. - System stopted")
                toast.show_toast("Mastercrimez - Banker","Je hebt teweinig geld op bank", duration=10)
            else:
                func.log('banker', str(response))

        except Exception as e:
            func.log('error', e)





def run(option):
    r = Run()

    if (option == 'check'):
        r.check()
    elif (option == 'info'):
        r.info()
    elif (option == 'banker'):
        r.banker()
    elif (option == 'bunker'):
        r.bunker()



def main():
    run('info')

    try:
        if (stop):
            print('stop')
            exit()
        else:
            if (stop):
                print('stop')
                exit()
            elif (int(func.read_file('info', 'bunker')) > 0):
                func.log('idle', f"Al in bunker moet nog {func.read_file('info', 'bunker')} seconden wachten.")
                t = threading.Timer(int(func.read_file('info', 'bunker')), main).start()
            else:
                run('check')
                run('bunker')
                run('info')
                func.log('idle', f"Moet {func.read_file('info', 'bunker')} seconden wachten.")

                t = threading.Timer(int(func.read_file('info', 'bunker')) + 2, main).start()

    except Exception as e:
        exit()

if __name__ == '__main__':
    os.system('cls')
    init()
    check.check("token")
    run('info')
    main()
