#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
import urllib

def get(line):

    line_spliteds = urllib.unquote(line).split('|')
    for line_splited in line_spliteds:
        if "de=" in line_splited:
            found = line_splited
            found_splited = found.split('=')
            if len(found_splited) == 2:
                return found_splited[1]
            else:
                print "Null"
                return
    return


def main(filename):
    '''
    '''
    file_in = open(filename, 'rb')
    lines = file_in.readlines()
    results = []
    for line in lines:
        line_res = get(line)
        if line_res and line_res not in results:
            results.append(line_res)

    print 
    print "The Number is :\033[01;41m %d\033[1;m" % len(results)
    print 
    #print "\033[1;31m All items are : \033[1;m" 
    print "All items are :" 
    print 
    for result in results:
        print "\033[1;32m\t %s\033[1;m" % result
    print 


if __name__ == '__main__':
    import os, sys
    from optparse import OptionParser    

    parser = OptionParser(usage="%prog [options]")
    parser.add_option("-n", "--name", help="The name of file", dest="filename")
    (options, args) = parser.parse_args()
    if not options.filename:
        print "Please check the input"
        sys.exit(1)    

    if not os.path.exists(options.filename):
        print "Please check the file exists!"


    main(options.filename)

