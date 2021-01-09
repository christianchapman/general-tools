#! /usr/bin/python3

import os
import sys
import datetime

ip = sys.argv[1]
name = sys.argv[2]

filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
hostname = name
file = name +"." + filename

response = os.system("ping -c 2 " + ip)

#and then check the response...
if response == 0:
  f = open ("/root/wells/net/rd05/"+file+"-up",'w')
  print ("%s %s is up" %(ip,hostname))
  txt = "%s %s is up\n" %(ip,hostname)
  f.write( txt)
  f.close()
else:
  f = open ("/root/wells/net/rd05/"+file+"-down",'w')
  print ("%s %s is down " %(ip,hostname))
  txt = "%s %s is down\n" %(ip,hostname)
  f.write( txt)
