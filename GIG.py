#!/usr/bin/python3.6
# ==================================Info about the program==================================

__author__ = "Mr.BlackPY"
__product__ = "Gladiator IG"
__version__ = "2.5"

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
    UNDERLINE = '\033[4m'


# ==================================Import Modules==================================

try:
    import socket
    import requests
    import time
    import subprocess
    import datetime as dt

except ImportError as b:
    exit(bcolor.WARNING + """[!] WARNING: Install the prerequisites before running this program

[1] socket 
[2] requests 
[3] time 
[4] subprocess 
[5] datetime

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
     \____|___\____|     v2.5
       
    """ + bcolor.ENDC

start_menu = bcolor.BOLD + """
    ----------------------------------------------------------
    ======= Welcome To GLADIATOR IG	                         |           
    ======= Developed By: Mr.BlackPY                         |
    ======= Oct 11 2018      			                     |
    ======= For More Information See the file FAQ.pdf        |
    ----------------------------------------------------------
    """ + bcolor.ENDC


errmsg = bcolor.FAIL + """
We’re having trouble finding that site
If that address is correct, here are 2 other things you can try:
[1] Try again later.
[2] Check your network connection.
""" + bcolor.ENDC.upper()

Help = bcolor.OKBLUE + "Example: Google.com\n" + bcolor.ENDC

ld = "-----------------------------------------------------------"

Ctrl_C = "\n[!] You pressed Ctrl+C"

# ==================================Global Variables==================================

global var

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

try:
    Target = str(input(bcolor.OKBLUE + "[?] Please Enter Your Target : ") + bcolor.ENDC)
    Minimum = int(input(bcolor.OKBLUE + "Minimum port for scan: " + bcolor.ENDC))
    Maximum = int(input(bcolor.OKBLUE + "Maximum port for scan: " + bcolor.ENDC))

except KeyboardInterrupt:
    exit(Ctrl_C)

Maximum += 1

var = Target.strip() and Target.rstrip('/')

try:
    IP = socket.gethostbyname(var)

except socket.gaierror:
    exit(errmsg)

except socket.error:
    exit(errmsg)

message = "[*] Please Wait it may take a few minutes...\n[*] Target IP: {}\n".format(IP)
print(bcolor.OKBLUE + message + bcolor.ENDC)

if 'https://' and 'http://' not in var:
    var = 'http://' + var


# ==================================Sign==================================


def sing():
    print(bcolor.BOLD + "\n[*] Please report bugs to: Gladiator.IG.dev@gmail.com" + bcolor.ENDC)
    print(bcolor.BOLD + "\n[+] Information Collected By: GLADIATOR INFO GRABBER" + bcolor.ENDC)
    print(bcolor.BOLD + "\n[*] Ended in {}\n".format(time.strftime("%X")) + bcolor.ENDC)

# ====================================================================


def wait():
    m = bcolor.OKGREAN + "Please Wait....." + bcolor.ENDC
    for i in m:
        print(i, end='', flush=True)
        time.sleep(1)
    return

# ==================================PORT SCANNER==================================
# Reference: https://www.pythonforbeginners.com/port-scanner-in-python


def port_scanner(IP, Min=1, Max=1081):
    global sock
    socket.setdefaulttimeout(1)

    try:
        for port in range(Min, Max):  # You can change port number | Example: range(0, 655351) [All Ports]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((IP, port))

            if result == 0:
                print(bcolor.OKGREAN + "[+] Port {}".format(port) + bcolor.ENDC)

        sock.close()

    except KeyboardInterrupt:
        exit(Ctrl_C)

    except socket.gaierror:
        exit(errmsg)

    except socket.error:
        exit(errmsg)

    print(ld)
    return


# ==================================Whois==================================
# Reference: https://www.stackoverflow.com/questions/python-whois-library-return-nothing-for-active-domain-names


def whois(ip):
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

        s.close()
        print(bcolor.OKGREAN + response.decode() + bcolor.ENDC)
        print(ld)

    except socket.gaierror:
        exit(errmsg)

    except socket.error:
        exit(errmsg)

    except KeyboardInterrupt:
        exit(Ctrl_C)

    except Exception:
        exit(errmsg)
    return


# ==================================Find sub domains==================================

def find_sd(Tar):
    global url

    try:
        file = open('dictsub.txt', 'r', encoding='utf-8')
        for line in file.readlines():
            url = line + Tar
    except FileNotFoundError as f:
        exit(f)

    r = requests.head(url)
    if r.status_code == 200:
         print(bcolor.OKBLUE + '[+]' + url + bcolor.ENDC)
         print(ld)
    return 
# ==================================ADMIN PAGE FINDER==================================


def apf(target):
    global dic_file
    global url

    try:
        dic_file = open("dictionary.txt", "r", encoding="utf_8")

    except FileNotFoundError as h:
        exit(bcolor.FAIL + "[!] There was an error reading file!\n{}".format(h) + bcolor.ENDC)

    for aline in dic_file.readlines():
        url = target + '/' + aline

    try:
        req = requests.head(url)
        if req.status_code == 200:
            print(bcolor.OKGREAN + "[+]" + url + bcolor.ENDC)
            print(ld)
        else:
            print(bcolor.FAIL + 'Admin Page Not Found!' + bcolor.ENDC)
            print(ld)

        dic_file.close()

    except Exception:
        exit(errmsg)

    except KeyboardInterrupt:
        exit(Ctrl_C)
    return


# ==================================Website Info==================================


def wi(target):
    global request

    try:
        request = requests.head(target)
    except ConnectionError as CE:
        print(errmsg, '\n {}'.format(CE))
        exit(0)

    print(bcolor.OKGREAN + "WebServer: " + request.headers['server'] + bcolor.ENDC)
    print(ld)
    return

# ==================================Function call==================================

wait()

port_scanner(IP, Minimum, Maximum)
wait()

whois(IP)
wait()

apf(var)
wait()

find_sd(var)
wait()

wi(var)
wait()

sing()

# ==================================Exit==================================

exit(0)

# ==================================THE END==================================

if __name__ == "__main__":
    main()

