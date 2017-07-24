#!/usr/bin/python
import os, sys
from time import sleep

if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

header = """
  ------------------
< \033[1;36mEmailo Installer!!\033[1;36m >
  ------------------
                          ____ _  _ ____         __
                          |___ |\/| |__| | |    |  | 
                          |___ |  | |  | | |___ |__| 
                                                     
                                                      ParrotSec.org
                                                     
"""

print header
print "\033[1;36mOperating Systems Available:\033[1;36m "
print "\n--------------------------"
print "(1) Parrot Sec(x86/x64)"
print "--------------------------\n"

option = input("\033[0m[>] Select Operating System: \033[0m")

if option == 1:
    print "\033[1;33m[*] Loading...\033[0m"
    os.system('apt-get install python-pip')
    os.system('easy_install pip')
    import pip
    os.system('sudo apt-get install libjpeg-dev libfreetype6 zlib1g-dev')
    os.system('pip install google')
    os.system('pip install requests')
    os.system('pip install pythonwhois')
    os.system('pip install pillow')
    os.system('pip install qrcode')
    os.system('pip install requests[security]')
    os.system('pip install http://effbot.org/downloads/Imaging-1.1.6.tar.gz')
    install = os.system("apt-get update && apt-get install -y build-essential git")
    install2 = os.system("cp -R emailo/ /opt/ && cp emailo.py /opt/emailo && cp run.sh /opt/emailo && cp run.sh /usr/bin/emailo && chmod +x /usr/bin/emailo")
    os.system('apt-get install sendemail')
    os.system('apt-get install libncurses5')
    pip.main(["install", "scapy", "SpoofMAC", "pythonwhois", "BeautifulSoup", "requests", "mechanize", "google", "qrcode"])
    print "\033[1;32m[!] Finished Installing! Run 'emailo' to run program [!]\033[0m"
    sys.exit()
else:
    print "Whoops! Something went wrong!"
