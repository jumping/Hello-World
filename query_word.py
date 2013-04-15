#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
import sys
import BeautifulSoup
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')


def query(word):
    """
    step 1: fetching the url
    """
    theurl = "http://dict.youdao.com/search?le=eng&q=%s&keyfrom=dict.index" % word
    page = urllib2.urlopen(theurl, timeout=10)
    soup = BeautifulSoup.BeautifulSoup(page.read())
    page.close()
    """
    step 2: get the phonounce and meanings
    """
    target = soup.findAll('div', attrs={'id':'phrsListTab','class':'trans-wrapper clearfix'})[0]
    phons = target.findAll('span', attrs={'class':'pronounce'})
    phons_cont =  [ x.getText().decode('utf-8') for x in phons ]
    phonounce = " ".join(phons_cont)
    cont = target.find('div', attrs={'class':'trans-container'}).ul.getText()
    print "%s   %s" %(phonounce, cont)


if __name__ == '__main__':

    if len(sys.argv) != 2:
       
        print """
a world need and only

Ex: %s  apply
        """ %(sys.argv[0])
        
        sys.exit(0)
        
    query(sys.argv[1])


