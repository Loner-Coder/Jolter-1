#!/usr/bin/env python2

#:-:-:-:-:-:-#
#   Jolter   #
#:-:-:-:-:-:-#

#This module is a part of Jolter
#https://github.com/code-sploit/jolter 

import sys
import time
import os
sys.path.append('modules/')
from udp_dos import * 
from time import sleep

def udp(web):
    udp_dos(web)
