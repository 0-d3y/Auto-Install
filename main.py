# Coded By Mr.SaMi
# Using Python3.11.0 
# Attack in website of israel (Fuck israel)
# طوفان الاقصى

import os
try:os.system('pkg update -y‍')
except:pass
try:os.system('pkg upgrade -y‍')
except:pass
try:import platform
except:os.system('pkg install lib-platform')
try:import pyfiglet
except:os.system('pkg install pyfiglet')
try:import webbrowser
except:
    os.system('pip install pycopy-webbrowser')
    os.system('pip install webbrowser')
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def banner():
    sami = pyfiglet.Figlet(font="slant")
    banner = sami.renderText("Auto Install")
    print(f"""{red}{banner}{green}
[1] Install the basics‍
[2] About the programmer‍
[0] Exit
""")


def sami_logo():
    sami = pyfiglet.Figlet(font="slant")
    banner = sami.renderText("Mr.SaMi")
    print(f"""{red}{banner}{green}""")

def sami():
    clear()
    sami_logo()
    print(f"""
{red}[+]{green} This tool was developed to meet your needs and install the basics in a correct and problem-free way‍
‍
{cyan}[#]{green} Follow me :‍
[1] Telegram Channel
[2] Instagram
[3] Call Me
[4] Back Home
[0] Exit
""")
    dev_ = input("\033[31m╔═══[\033[32mChoose A Number‍\033[31m]\n\033[31m╚══》 \033[32m‍")
    if dev_ =="1":
        webbrowser.open("https://t.me/TYG_TEAM")
        sami()
    elif dev_ =="2":
        webbrowser.open("https://instagram.com/cyber_77k")
        sami()
    elif dev_ =="3":
        webbrowser.open("https://t.me/TYG_YE_BOT")
        sami()
    elif dev_ =="4":
        main()
    elif dev_=="0":
        os.system("exit")
    else:
        main()

def _install_():
    try:os.system('pkg update -y‍')
    except:pass
    try:os.system('termux-setup-storage‍')
    except:pass
    try:os.system('termux-change-repo‍')
    except:pass
    try:os.system('pkg install texinfo -y && info > commands.txt && cat commands.txt‍')
    except:pass
    try:os.system('pkg --check-mirror update‍')
    except:pass
    try:os.system('pkg install git -y‍')
    except:pass
    try:os.system('pkg install fish -y‍')
    except:pass
    # Install Python 
    try:os.system('apt install python -y‍')
    except:pass
    # install python2
    try:os.system('apt install python2 -y‍')
    except:pass
    try:os.system('apt install ruby -y‍')
    except:pass
    try:os.system('apt install python -y‍')
    except:pass
    dev = input(f"{red}[+]{green} Termux Basics has been successfully downloaded. Do not forget to subscribe to the developer channel. Do you want to view the developer channel [y/n]:‍")
    if dev =="y" or 'Y':
        sami()
    elif dev =="n" or 'N':
        main()


def main():
    clear()
    banner() 
    main_choose = input(f'\033[31m╔═══[\033[32mChoose your Destination‍\033[31m]\n\033[31m╚══》 \033[32m‍')
    if main_choose =='1':
        _install_()
    elif main_choose =="2":
        sami()
if __name__ == "__main__":
    main()
