#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# ==================================Info about the program==================================

__author__ = "Mr.BlackPY"
__product__ = "Gladiator IG"
__version__ = "2.8"

# FREE_SOFTWARE
# FREEDOM
# GNU/LINUX

"""
GLADIATOR INFO GRABBER
"""
# ==================================Colors==================================


class bcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREAN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


# ==================================Import Modules==================================

try:
    import socket
    import requests
    import time
    import subprocess
    import datetime as dt
    import random

except ImportError as b:
    exit(bcolor.WARNING + """[!] WARNING: Install the prerequisites before running this program

[1] socket
[2] requests
[3] time
[4] subprocess
[5] datetime
[6] random

[*] How to install them? (pip install module)
Example: sudo pip install requests
---------------------------------------------\n{}\n
""".format(b) + bcolor.ENDC)

# ==================================Create required Variables==================================

Logo = bcolor.HEADER + """
  ____ ___ ____ 
 / ___|_ _/ ___|
| |  _ | | |  _ 
| |_| || | |_| |
 \____|___\____|    Version: 2.8
    """ + bcolor.ENDC

start_menu = bcolor.BOLD + """
----------------------------------------------------------
======= Welcome To GLADIATOR IG	                         |
======= Developed By: Mr.BlackPY                         |
======= For More Information See the file FAQ.pdf        |
----------------------------------------------------------
    """ + bcolor.ENDC

Help = bcolor.OKBLUE + "Example: Google.com\n" + bcolor.ENDC

ld = "-----------------------------------------------------------"

Ctrl_C = "\n[!] You pressed Ctrl+C"

# ==================================Global Variables==================================

global Target

global IP

global Minimum

global Maximum

# ==================================Clear the Screen==================================

subprocess.call('clear', shell=True)
# also you can use: import os; os.system('clear')
# For windows OS: import os; os.system('cls')

# ==================================Main Method==================================


def main():
    print(Logo, start_menu)


main()

# ==================================Print current time==================================

print(bcolor.OKBLUE + "[*] Starting at {}\n".format(time.strftime("%X") + bcolor.ENDC))

print(Help)

# ==================================Get input from user==================================

try:
    Target = str(input(bcolor.OKBLUE + "[?] Please Enter Your Target: " + bcolor.ENDC))
    Minimum = int(input(bcolor.OKBLUE + "Minimum port range for scan: " + bcolor.ENDC))
    Maximum = int(input(bcolor.OKBLUE + "Maximum port range for scan: " + bcolor.ENDC))

except KeyboardInterrupt:
    exit(Ctrl_C)

except ValueError as VE:
    exit(VE)

Maximum += 1

# ==================================check input==================================


def check_input(user_target):
    """
    check the input it's valid or not
    """
    global check

    invalid = ["/", "*", "+", "\\", "|", "=", ")", "(", "&", "^", "%", "$", "#", "@", "!",
               "~", "`", "<", ">", "?", "[", "]", "{", "}", ",", "_", "\'", "\"", ";", ":"]

    user_target = user_target.strip() and user_target.rstrip('/')

    for i in invalid:
        a = user_target.find(i)
        if a != -1:
            print(bcolor.FAIL + "[-] Invalid input" + bcolor.ENDC)
            exit(0)

    return

# ====================================================================


check_input(Target)

IP = socket.gethostbyname(Target)

message = "[*] Please Wait it may take a few minutes...\n[*] {}\'s IP: {}\n".format(Target, IP)
print(bcolor.OKGREAN + message + bcolor.ENDC)

if 'https://' and 'http://' not in Target:
    Target = 'http://' + Target

# ==================================Sign==================================


def sing():
    print(bcolor.BOLD + "\n[*] Please report bugs to: Gladiator.IG.dev@gmail.com" + bcolor.ENDC)
    print(bcolor.BOLD + "\n[+] Information Collected By: GLADIATOR INFO GRABBER" + bcolor.ENDC)
    print(bcolor.BOLD + "\n[*] Ended in {}\n".format(time.strftime("%X")) + bcolor.ENDC)
    print(ld)

# ===============================wait==================================


def wait():
    m = bcolor.OKGREAN + "Wait....\n" + bcolor.ENDC
    for i in m:
        print(i, end='', flush=True)
        time.sleep(0.5)

    print(ld)

    return

# ==================================PORT SCANNER==================================
# Reference: https://www.pythonforbeginners.com/port-scanner-in-python


def port_scanner(IP, Min=1, Max=1081):
    global sock
    global err

    socket.setdefaulttimeout(1)

    err = "Minimum port range can\'t be bigger then Maximum port range "

    if Min > Max:
        print(bcolor.WARNING + err + bcolor.ENDC)
        exit(0)

    try:
        for port in range(Min, Max):  # You can change port number | Example: range(0, 655351) [All Ports]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((IP, port))

            if result == 0:
                print(bcolor.OKGREAN + "[+] Port {}".format(port) + bcolor.ENDC)

        sock.close()

    except ConnectionError as CE:
        exit(bcolor.FAIL + str(CE) + bcolor.ENDC)

    except KeyboardInterrupt:
        exit(Ctrl_C)

    print(ld)
    return


# ==================================Whois==================================
# Reference: https://www.stackoverflow.com/questions/python-whois-library-return-nothing-for-active-domain-names


def whois(ip):
        global response
        global s

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("whois.arin.net", 43))
            s.send(('n ' + ip + '\r\n').encode())

            response = b''

            startTime = time.mktime(dt.datetime.now().timetuple())
            timelimit = 3

            while True:
                elapsedTime = time.mktime(dt.datetime.now().timetuple()) - startTime
                data = s.recv(4096)
                response += data
                if not data or elapsedTime >= timelimit:
                    break

        except socket.gaierror:
            print(bcolor.FAIL + "Hostname could not be resolved. Exiting" + bcolor.ENDC)
            exit(0)

        except socket.error:
            print(bcolor.FAIL + "Could't connect to server" + bcolor.ENDC)
            exit(0)

            s.close()
            print(bcolor.OKGREAN + response.decode() + bcolor.ENDC)
            print(ld)

            return

# ==================================ADMIN PAGE FINDER==================================


def apf(target, proxy, user_agent):
    global dic_file
    global url

    headers = {'User-Agent': user_agent}

    try:
        dic_file = open("dictionary.txt", "r", encoding="utf_8")

    except FileNotFoundError as h:
        exit(bcolor.FAIL + "[!] There was an error reading file!\n{}".format(h) + bcolor.ENDC)

    for aline in dic_file.readlines():
        url = target + '/' + aline

    try:
        req = requests.head(url, headers=headers, proxies=proxy)

        if req.status_code == 200:
            print(bcolor.OKGREAN + "[+]" + url + bcolor.ENDC)
            print(ld)
        else:
            print(bcolor.FAIL + 'Admin Page Not Found!' + bcolor.ENDC)
            print(ld)

        dic_file.close()

    except requests.ConnectTimeout:
        print(bcolor.FAIL + "[*] Website Don\'t Response" + bcolor.ENDC)
        print(ld)

    except KeyboardInterrupt:
        print(Ctrl_C)
        exit(ld)

    return

# ==================================Web server==================================


def web_server(Target, proxy, user_agent):

    headers = {'User-Agent': user_agent}

    try:
        r = requests.head(Target, headers=headers, proxies=proxy)
        re = r.headers['server']
        print(bcolor.OKGREAN + "WebServer: " + re + bcolor.ENDC)
        print(ld)
    except KeyError as k:
        exit(k)

# ==================================Get Free Proxy==================================


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20120306 Firefox/56.0'}

proxy = requests.get('https://api.getproxylist.com/proxy', headers=headers).json()

ip = str(proxy['ip'])
port = str(proxy['port'])

free_proxy = {'http': ip + ':' + port}

# ==================================User-Agent Generator==================================

version = [5.0, 4.0]

system_information = ['(X11; Linux x86_64; rv:45.0)', '(Macintosh; Intel Mac OS X 10.10; rv:48.0)']

platform = ['Gecko/20100101', 'Gecko/20120306', 'Gecko/20090824']

platform_details = ['Firefox/56.0', 'Firefox/45.0', 'Firefox/3.6.28', 'Firefox/48.0']

user_agent = "Mozilla/{} {} {} {}".format(random.choice(version), random.choice(system_information),
                                          random.choice(platform), random.choice(platform_details))

# ==================================Function call==================================


try:
    print(bcolor.OKBLUE + "Scanning Ports ...\n" + bcolor.ENDC)
    port_scanner(IP, Minimum, Maximum)
    wait()
    # ---------------------------------------------------------------------
    print(bcolor.OKBLUE + "Whois {}\n".format(Target) + bcolor.ENDC)
    whois(IP)
    wait()
    # ---------------------------------------------------------------------
    print(bcolor.OKBLUE + "Finding the admin page...\n" + bcolor.ENDC)
    apf(Target, free_proxy, user_agent)
    # ---------------------------------------------------------------------
    print(bcolor.OKBLUE + "Finding type of webserver...\n" + bcolor.ENDC)
    web_server(Target, free_proxy, user_agent)

except KeyboardInterrupt:
    exit(Ctrl_C)

sing()
# ==================================Exit==================================

exit(0)

# ==================================THE END==================================

if __name__ == "__main__":
    main()

