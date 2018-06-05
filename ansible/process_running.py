#!/usr/bin/env python
import os
import sys
process_name= "filebeat" # change this to the name of your process

tmp = os.popen("ps -Af").read()

if process_name not in tmp[:]:
    print "The process is not running."
    sys.exit()
else:
    print "The process is running."
