#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
def main(line):
    '''
    '''
    tmp = []
    l = line.replace(')','').split('*')
    for d in l:
        tmp.append('('+d+')')
    return '*'.join(tmp)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        express = sys.argv[1]
    else:
        print "Error"
        sys.exit(0)
    d = main(express)
    print "Converted: %s" %d
    print "Result: %d" % eval(d)


