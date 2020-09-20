#! /usr/bin/python3

import os
import sys
import datetime

ip = sys.argv[1]
name = sys.argv[2]

filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
hostname = "well01" #example
file = name +"." + filename
f = open (file,'w')

response = os.system("ping -c 2 " + ip)

#and then check the response...
if response == 0:
  print ("%s %s is up" %(ip,hostname))
  txt = "%s %s is up\n" %(ip,hostname)
  f.write( txt)
else:
  print ("%s %s is down " %(ip,hostname))
  txt = "%s %s is down\n" %(ip,hostname)
  f.write( tx
