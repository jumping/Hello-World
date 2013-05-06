#!/usr/bin/env python
#-*- coding: utf-8 -*-
#

import re
import sys
import urllib2
import json

ipRex = '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'
#ipRex = '(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$'

class IpS():

    def __init__(self):
        self.apiUrlTaobao = 'http://ip.taobao.com/service/getIpInfo.php?ip='

    def searchByTaobao(self,ip):
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')
        opener = urllib2.build_opener()
        opener.addheaders = [headers]
        data = opener.open(self.apiUrlTaobao+ip).read()
        data = data.decode('utf8')
        return data

def query(ip):
    tmp = re.findall(re.compile(ipRex),ip)
    if not tmp:
        print "Wrong format of IP"
        sys.exit(1)

    ips = IpS()
    reponse = ips.searchByTaobao(ip)
    data = json.loads(reponse)
    if data['code'] != 0:
        print "No Found"

    d = data['data']
    for k,v in d.items():
        if v:
            print k.capitalize(), v


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Only accept a IP"
        sys.exit(0)

    ip = sys.argv[1]
    query(ip)

