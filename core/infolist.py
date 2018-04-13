#!/usr/bin/env python2

#:-:-:-:-:-:-#
#   Jolter   #
#:-:-:-:-:-:-#

#This module is a part of Jolter
#https://github.com/code-sploit/jolter 

from colors import *
import time

def infolist():

	print '' + O + '\n  Choose the method which you want to use in the Fl00D Attack:-\n'
	time.sleep(0.1)
	print '' + C + " +==============================================================+\n"                    
	print ''
	print "" + C + "    [1] \033[94mHTTP Fl00D <- \033[1;37mThis method will flood the website"
	print '' +GR + "           with 1000's of HTTP requests, keeping the"
	print "" +GR + "   website's resources busy while making it totally unavailable.\n"
	time.sleep(0.1)

	print "" + C + "    [2] \033[94mSYN Fl00D <- \033[1;37mThis method will try to accomplish as"
	print ''+ GR + '     many as SYN-ACK handshakes with spoofed IPs and thereby '
	print ''+ GR + '                 depriving it of all resources.\n'
	time.sleep(0.1)

	print "" + C + "    [3] \033[94mUDP Fl00D <- \033[1;37mThis method will randomly bombard "
	print '' + GR +"        the website with specific crafted UDP packets on"
	print '' + GR +"                          random ports."
	print '' + C + '\n +==============================================================+'
	time.sleep(0.4)
