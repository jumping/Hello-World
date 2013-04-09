#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
import time
import MySQLdb
import eventlet.db_pool as db_pool

conn_kwargs = {'host':'127.0.0.1', 'user':'root', 'passwd':'', 'db':'test', }
sql = """select count(*) from test"""
pooled = db_pool.ConnectionPool(MySQLdb, **conn_kwargs)

def print_now():
    return time.time()

def query(conn):
    cur = conn.cursor()
    cur.execute(sql%(random.randint(1,1000)))
    data=cur.fetchall()
    return cur

def test(times):
    start = print_now()
    for i in range(0,times):
        conn = pooled.get()
        try:
            query(conn)
        finally:
            pooled.put(conn)
    end = print_now()
    print "Total: %d s" % (end - start)

def main():
    '''
    '''
    test(5)

    print 'main'


if __name__ == '__main__':
    main()


