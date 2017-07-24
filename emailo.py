# coding: utf-8
#!/usr/bin/env python
import sys, platform, subprocess, socket, time, os, urllib,  random, string, smtplib, urllib2, getpass, zipfile
from urllib2 import urlopen
from time import sleep
from getpass import getpass
from subprocess import call
sys.path.append('emailo/')
from smtp import *
from info import *


try:
    import scapy
    import pip
    import requests
    import pythonwhois
    import argparse
    import google
except ImportError as e:
    print (color.UNDERLINE + "\033[91m" + "You don't have some modules installed! \nPlease run install.py to install this tool fully! " + color.END)
    print "Error: {}".format(e)
    print "Execute: pip install (module name)"
    if (e) == "DependencyWarning":
	os.system("sudo apt-get update")
	os.system("apt-get remove python-pip")
	os.system("easy_install pip")
	os.system("sudo pip uninstall requests")
	os.system("sudo pip install requests")
    elif (e) == "Unable to locate package lib32ncurses5":
	os.system("sudo apt-get update")
	os.system("sudo apt-get install lib32ncurses5 lib32bz2-1.0")
    else:
	os.system("sudo apt-get update")
    sys.exit()
###############################
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
###############################
os.system('clear')
if str(platform.system()) != "Linux":
	sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "You are not using a Linux Based OS! Linux is a must-have for this script!" + color.END)
if not os.geteuid() == 0:
    sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Must be run as root. :/" + color.END)

os.system('clear')

header = """
  ------------------
< \033[1;36m-----Emailo-----\033[1;36m >
  ------------------
                          ____ _  _ ____         __
                          |___ |\/| |__| | |    |  | 
                          |___ |  | |  | | |___ |__| 
                                                     
                                                      ParrotSec.org
                                                     
"""

print header
def banner1():
    print ""
    print ""+M+"|----- Made by Nemo Roy[recodeking] -----|"
    print color.PURPLE + "\n|------------ Welcome to Emailo ----------|"
	 
banner1()

swear = "fuck", "shit", "nigga", "bitch", "dick", "pussy", "cunt", "nigger", "asshole", "ass"
spell = "helpp", "hellp",  "emial", "HELP", "hwlp",   "Info",  "hlep", "claer"
def emailo():
    while True:
        try:
            main = raw_input(''+G+'' + color.BOLD + color.UNDERLINE + 'Emailo>' + color.END)
            if main in swear:
                print(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Watch your language!" + color.END)
	    elif main in spell:
                print(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Do you know how to spell?!" + color.END)
            
            elif main == "info":
                info()
            elif main == "help":
                print ""+W+"+----------------------------+"
                print ""+C+"help "+W+"- displays this help message"
                print ""+C+"clear "+W+"- clears the screen"
                print ""+C+"exit "+W+"- exits tool"
                print ""+P+"contact "+W+"- contact me"     
                print ""+T+"email "+W+"- bomb an email address"
                print ""+C+"info "+W+"- displays computer and network info"
                print ""+W+"+----------------------------+"
    	    
	    elif main == "email":
	        smtp()
	    
	    elif main == "contact":
	        
	        print(''+T+'' + color.UNDERLINE + 'Email me:'+W+'' + color.BOLD + ' meetwithnemo@gmail.com' + color.END)
	        print(''+T+'' + color.UNDERLINE + 'Twitter:'+W+'' + color.BOLD + ' @recodeking' + color.END)
	   
	        
	       
	           
	   
	    elif main == "clear":
	        os.system('clear')
            elif main == "exit":
	        print (""+G+"[*] " + color.UNDERLINE + "\033[91m" + "Exiting..." + color.END)
	        print (""+G+"[*] " + color.UNDERLINE + "\033[92m" + "GoodBye!" + color.END)
	        time.sleep(0.2)
	        sys.exit()
	    elif main == "":
	        print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Please enter an option!" + color.END)
            else:
	        print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "That is not an option!" + color.END)
        except KeyboardInterrupt:
		print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "\nCtrl-C Pressed! Use 'exit' to close the tool!" + color.END)
		emailo()
emailo()
