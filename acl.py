#! /usr/bin/python

import sys
import os
import pdb
import re

fname = sys.argv[1]
found = 0
foundbgp = 0
aclname =[]
name = []

# pdb.set_trace()

##########################
# Open file and read in the access lists as a python list
###########################

f = open(fname)
look = f.readlines()
for entry in look:
 if "ip access-list" in entry:
  # Get the name and save to list
  name = entry.split()
  aclname.append(name[3])
#  print "the entry is %s" % (name).close()

###############################
# Open the file again .. and compare the ACL names previous captured to the line of config
# If there is a match mark as found
# At the end if we dont find a match and exclusing its own entry, then we know the ACL is not tied to anything
##############################

found = 0
f = open(fname)
lookagain = f.readlines()
for entry_acl in aclname:
 found = 0
 f = open(fname)
 lookagain = f.readlines()

 print "acl is %s" %(entry_acl)
 for thing_line in lookagain:
  if entry_acl in thing_line:
    if "ip access-list" in thing_line:
       continue
    entry=entry.strip("\n")
    print " file %s --> match found %s" % (fname,entry)
    found = 1

 if (found == 0):
    print " file %s --> NOT FOUND %s" % (fname,entry_acl)
    found = 0
f.close()
