#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
import re
import subprocess
import urllib2


def main(gw, execute=False):
    '''
    fetch url from the url and figure out all IPs
    '''
    url = 'https://forums.aws.amazon.com/ann.jspa?annID=1701'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    if response and response.msg != 'OK':
        print "Could not fetch the url.", url
        return
    lines = response.readlines()
    ips = re.findall( r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}', ''.join(lines) )
    if not ips:
        print "NO Found IPs "
        return

    ips.sort()
    for ip in ips:
        line = "route add -net %s gw %s device ppp0" %(ip, gw)
        print line
        if execute: subprocess.call(line)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print "Need gateway to output the whole command."
        sys.exit(1)
    gw = sys.argv[1]
    execute = sys.argv[2]
    if execute.lower() == 'y' or execute.lower() == 'yes':
        main(gw, True)
    else:
        main(gw)

