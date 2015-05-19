#!/usr/bin/env python
import argparse, datetime, getpass, sys, os



def excep(a,b):
    try:
       return a+b
    except TypeError:
        return 'TypeError'
        #sys.exit()
    else:
        print'vseOk'
    finally:
        print 'sysexit'
    return c

def parser():
    m=argparse.ArgumentParser()
    m.add_argument('--time','-t', action='store_true')
    m.add_argument('--date','-d', action='store_true')
    m.add_argument('--uname','-u', action='store_true')
    m.add_argument('-v','--version', action='store_true')
    m.add_argument('--tree', action='store_true')
    arg= m.parse_args()
    if arg.time: print datetime.datetime.now().strftime("%H:%M")
    if arg.date: print datetime.datetime.today().strftime("%d-%m-%Y")
    if arg.uname: print getpass.getuser()
    if arg.version: print sys.version
    if arg.tree: print os.listdir(os.curdir)





print excep('d',3)
parser()
