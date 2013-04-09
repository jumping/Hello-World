#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# File: eventlet_httpd.py
# Date: 2009-08-07
# Author: gashero

"""
一个使用eventlet作为底层的http服务器，测试一下性能
"""

from eventlet import api

def httpd(writer,reader):
    req=''
    while True:
        chunk=reader.readline()
        if not chunk:
            break
        req+=chunk
        if chunk=='\r\n':
            break
    data='Hello world!\r\n'
    writer.write('HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s'%(len(data),data))
    writer.close()
    reader.close()
    return

def main():
    try:
        server=api.tcp_listener(('0.0.0.0',3000))
        print 'Server started!'
        while True:
            conn,addr=server.accept()
            #print 'client %s connected!'%repr(addr)
            writer=conn.makefile('w')
            api.spawn(httpd,writer,conn.makefile('r'))
    except KeyboardInterrupt:
        pass
    return

if __name__=='__main__':
    main()


