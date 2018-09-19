#!/usr/bin/python3.6
# ==================================Info about the program==================================

__author__ = "Mr.BlackPY"
__product__ = "Gladiator IG"
__version__ = "2.0"

# FREE_SOFTWARE
# FREEDOM
# GNU/LINUX

"""
GLADIATOR INFO GRABBER
"""

# ==================================Import Modules==================================

try:
    import socket
    import requests
    import time
    import subprocess
    import datetime as dt

except ImportError as b:
    exit("""[!] WARNING: Install the prerequisites before running this program

[1] socket 
[2] requests 
[3] time 
[4] subprocess 
[5] datetime

[*] How to install them? (pip install module)
Example: sudo pip install requests
---------------------------------------------\n{}\n
""".format(b))

# ==================================Create required Variables==================================

Logo = """
  ____ ___ ____ 
 / ___|_ _/ ___|
| |  _ | | |  _ 
| |_| || | |_| | 
 \____|___\____|     v2.0       
"""

start_menu = """
----------------------------------------------------------
=======	Welcome To GLADIATOR IG	                         |           
=======	Developed By: Mr.BlackPY                         |
=======	Sep 16 2018      			                           |
======= For More Information See the file FAQ.pdf        |
----------------------------------------------------------
"""

msg = """
We’re having trouble finding that site
If that address is correct, here are 2 other things you can try:
[1] Try again later.
[2] Check your network connection.
"""

Help = "Example: https://www.Google.com\n"

ld = "-----------------------------------------------------------"

Ctrl_C = "\n[!] You pressed Ctrl+C"

errmsg = msg.upper()

# ==================================Global Variables==================================

global var

global Target

global url

global sock

global dic_file

global IP

global whois

# ==================================Clear the Screen==================================

subprocess.call('clear', shell=True)
# also you can use: import os; os.system('clear')
# For windows OS: import os; os.system('cls')

# ==================================Main Method==================================


def main():
    print(Logo, start_menu)


main()

# ==================================Print current time==================================

print("[*] Starting at {}\n".format(time.strftime("%X")))

print(Help)

try:
    Target = input("[?] Please Enter Target name:")

except KeyboardInterrupt:
    exit(Ctrl_C)

if len(Target) == 0:
    exit("[!] Please Enter Something Next Time.")
else:
    var = Target.strip() and Target.rstrip('/')

try:
    IP = socket.gethostbyname(var)

except socket.gaierror:
    exit(errmsg)

except socket.error:
    exit(errmsg)

print("[*] Please Wait it may take a few minutes...\n[*] Target IP: {}\n".format(IP))

if 'https://' and 'http://' not in var:
    var = 'http://' + var

# ==================================PORT SCANNER==================================
# Reference: https://www.pythonforbeginners.com/port-scanner-in-python

socket.setdefaulttimeout(1)

try:
    for port in range(0, 1080):  # You can change port number | Example: range(0, 655351) [All Ports]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP, port))

        if result == 0:
            print("[+] Port {}".format(port))

except KeyboardInterrupt:
    exit(Ctrl_C)

except socket.gaierror:
    exit(errmsg)

except socket.error:
    exit(errmsg)

print(ld)

# ==================================Whois==================================

try:

    def whois(ip):
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
        print(response.decode())

except socket.gaierror:
    exit(errmsg)

except socket.error:
    exit(errmsg)

except KeyboardInterrupt:
    exit(Ctrl_C)

except Exception:
    exit(errmsg)

whois(IP)

print(ld)

# ==================================ADMIN PAGE FINDER==================================

try:
    dic_file = open("dictionary.txt", "r", encoding="utf-8")  # open & read dictionary.txt

except FileNotFoundError as h:
    exit("[!] There was an error reading file!\n{}".format(h))

for aline in dic_file.readlines():
    url = var + '/' + aline

try:
    req = requests.head(url)
    if req.status_code == 200:
        print("[+]", url)
        print(ld)
    else:
        print('Admin Page Not Found!')
        print(ld)

except Exception:
    exit(errmsg)

except KeyboardInterrupt:
    exit(Ctrl_C)

# ==================================Sign==================================

print("\n[+] Information Collected By: GLADIATOR INFO GRABBER")

print("\n[*] Ended in {}\n".format(time.strftime("%X")))

# ==================================Exit==================================

dic_file.close()
sock.close()
exit(0)

# ==================================THE END==================================

if __name__ == "__main__":
    main()


