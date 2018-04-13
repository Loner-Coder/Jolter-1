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
from http_dos import * 
from time import sleep

def httpmain(web):
    http_dos(web)
