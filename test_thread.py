#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#http://blog.csdn.net/lazy_tiger/article/details/3861844#

import time
import thread

def timer(no, interval):
    cnt = 0
    while cnt<10:
        print 'Thread:(%d) Time:%s/n'%(no, time.ctime())
        time.sleep(interval)
        cnt+=1
    thread.exit_thread()
   
 
def test(): 
    '''
    Use thread.start_new_thread() to create 2 new threads
    '''
    thread.start_new_thread(timer, (1,1))
    thread.start_new_thread(timer, (2,2))
 
if __name__=='__main__':
    test()

