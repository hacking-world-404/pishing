#------------- IMPORT ------------#
from os import system as c
import time
import random

#---------------- COLOUR ----------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#---------------- LOGO ----------------#
def logo():
    c('clear')
    print(f"""{C}
 ▄▄▄▄▄  ▄▄▄▄▄  ▄▄▄▄▄ 
▐█   █▌▐█   █▌▐█    
▐█▀▀▀  ▐█▀▀▀  ▐█▀▀▀ 
▐█     ▐█     ▐█▄▄▄ 

{P}██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║ ██╔╝██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
█████╔╝ ███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██╗██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
{Y}       >>> HACKING WORLD - PHISHING VIP TOOL <<<
""")

#---------------- MAIN MENU ----------------#
def menu():
    logo()
    print(f"{A}[1] GENERATE  PHISHING LINK")
    print(f"{A}[0] EXIT TOOL")
    print(f"{A}---------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        phish_link()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        menu()

#---------------- PHISHING LINK GENERATOR (FAKE) ----------------#
def phish_link():
    logo()
    c('espeak "Generating phishing link"')
    site_name = input(f"{C}ENTER TARGET WEBSITE NAME (e.g. Facebook, FreeFire, PUBG): ")
    print(f"\n{Y}[+] Preparing phishing link for: {site_name}")
    time.sleep(3)
    print(f"{B}[+] Connecting to phishing server...")
    time.sleep(2)
    print(f"{G}[✓] Server Connected!")
    time.sleep(2)
    print(f"{Y}[+] Generating unique link...")
    time.sleep(3)

    fake_link = f"https://secure-{site_name.lower()}-login.vip2025.com"
    print(f"\n{G}[✓] PHISHING LINK GENERATED: {G}{fake_link}")
    print(f"{Y}Send this link to the victim carefully!")

    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#---------------- START TOOL ----------------#
menu()