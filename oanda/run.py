#!/usr/bin/python
import daemon
import time

def logit():
    fp = open('test.log','a')
    fp.write('Hello\n')
    fp.close()

daemon.createDaemon()
while 1:
        time.sleep(5)
        logit()