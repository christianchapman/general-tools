#! /usr/bin/python3

import os
import sys
import datetime
import subprocess

filename = sys.argv[1]

f = open (filename)
cap_list = f.readlines()
for well in cap_list:
 cmd = "grep -ir "+ well
 cmd = cmd.rstrip()
 cmd2 = cmd + " *"
 cmd3 = cmd2.rstrip()
 print (cmd3)
 output = subprocess.check_output(cmd3, shell=True)
 print (output)
f.close()
