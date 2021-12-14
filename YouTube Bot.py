import requests
import webbrowser
import time
import os
import colorama
import sys
import ctypes


def yt(colour='\033[31m'):
    colorama.init(convert=True)
    print('\033[31m')
    ctypes.windll.kernel32.SetConsoleTitleW("YouTube Views | Test Only")
    print('''
    
 /$$     /$$               /$$$$$$$$        /$$                      
|  $$   /$$/              |__  $$__/       | $$                      
 \  $$ /$$//$$$$$$  /$$   /$$| $$ /$$   /$$| $$$$$$$   /$$$$$$       
  \  $$$$//$$__  $$| $$  | $$| $$| $$  | $$| $$__  $$ /$$__  $$      
   \  $$/| $$  \ $$| $$  | $$| $$| $$  | $$| $$  \ $$| $$$$$$$$      
    | $$ | $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$_____/      
    | $$ |  $$$$$$/|  $$$$$$/| $$|  $$$$$$/| $$$$$$$/|  $$$$$$$      
    |__/  \______/  \______/ |__/ \______/ |_______/  \_______/      
                                                                     
                                                                     
                                                                     

    ''')
    url = input("Paste your youtube video in here: ")
    threads = int(input("How many threads would you like (Be careful with these): "))
    long = int(input("How long is the video in seconds(Account for buffering time): "))
    ask = input("Do you want to use proxies (y/n): ").lower()


    if ask == 'y':
        file = input("What is the name of the file containing the proxies (They will have to be really good proxies): ")
        proxylist = []
        with open(file,'r') as f:
            for line in f:
                line = line.replace('\n','')
                tmp = line.split(':')
                proxies = {
                    'http':'http://'+tmp[0]+'/',
                    'https':'http://'+tmp[0]+'/'
                }
                proxylist.append(proxies)
                for proxy in proxylist:
                    session = requests.session()
                    r = session.get(url,proxies=proxy)
        try:
            requests.get(url, proxies = proxy,timeout=3)
        except:
            print("Proxies Timed Out")
            pass
        try:
            webbrowser.open('chrome')

            for x in range(threads):
                webbrowser.open(url)
            time.sleep(long)
            os.system("taskkill /im chromium.exe /f")
        except:
            pass

    elif ask == 'n':
        webbrowser.open('chrome')
        time.sleep(5)

        for x in range(threads):
            webbrowser.open(url)
        time.sleep(long)
        os.system("taskkill /im chromium.exe /f")



yt()
askagain = input("Do you want to start again (y/n): ").lower()
if askagain == 'y':
    yt()
    os.systen("cls")
else:
    quit()

    
