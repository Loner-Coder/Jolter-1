#!/usr/bin/env python2

#:-:-:-:-:-:-#
#   Jolter   #
#:-:-:-:-:-:-#

#This module is a part of Jolter
#https://github.com/code-sploit/jolter 

import time
import random
from random import randint
from colors import *

def action(web):

	from impo import *
	e = raw_input( '' + O + '\n  [#] \033[1;4mTID\033[0m :> '+G+'')

	if e == '1':
	    httpban()
	    httpmain(web)

	elif e == '2':
	    synban()
	    syn(web)

	elif e == '3':
	    udpban()
	    udp(web)

	else:
	    dope = ['You high dude?','Hey there! Enter a valid option','Whoops! Thats not an option','Sorry fam! You just typed shit']
	    print dope[randint(0,3)]
	    time.sleep(0.8)
	    os.system('clear')
	    infolist()
	    action(web)
