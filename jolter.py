#!/usr/bin/env python2

#:-:-:-:-:-:-#
#   Jolter   #
#:-:-:-:-:-:-#

#This module is a part of Jolter
#https://github.com/code-sploit/jolter 

import sys
import time
import os
sys.path.append('core/')
from impo import *
from time import sleep

os.system("clear")

def jolter():

    try:
	print ""
	sleep(0.1)
	banner()
	banner1()
	web = raw_input(O+"\n     [#] Target ("+GR+"do not specify "+R+"protocol"+O+") :> "+G+'')

	try:
       	    host_ip = socket.gethostbyname(web)
	except:
	    print R+' [-] No internet connection, or wrong web address...'

	time.sleep(0.5)
	print('' + R + "     [!] Target set ---> %s " % (web))
	print('' + R + " +==============================================================+")
	time.sleep(0.2)
	infolist()
	action(web)

    except KeyboardInterrupt:
	print ''+R+'\n   [!] Aborted [!]\n'
 
jolter()
