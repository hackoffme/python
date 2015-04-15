
__author__ = 'hackoff'
from _bisect import insort
from math import fmod
def listreplase(l):
    l.sort()
    l0=l[0]
    del l[0]
    for i in l:
        if l0==i:
            print i
        l0=i

def listtypereplace(l):
    t=[]
    for i in l:
        t.append(type(i))
    t.sort()
    i=0
    print t
    while len(t)<>i:
        t0=t[i]
        print t0, t.count(t0)
        i=i+t.count(t0)

def sortListEndLeter(l):
    for i in xrange(0,len(l)):
        l[i]=l[i][::-1]
    l.sort()
    for i in xrange(0,len(l)):
        l[i]=l[i][::-1]
    print l

def pasteInSortList(l,i):
    print l
    insort(l,i)
    print l

def twoList(l1,l2,elm):
    l2.insert(l1.index(elm),elm)
    print l1,l2

def removeEven(l):
    ls=l.split()
    lEven=[]
    s=' '
    for i in xrange(0,len(ls)):
        if fmod(len(ls[i]),2)==0:
            lEven.append(ls[i])
    print s.join(lEven)

def sequence(l):
    l.append(0)
    begin=0
    end=0
    lenn=0
    ii=l[0]
    k=0
    b=0
    for i in xrange(1,len(l)):
       if l[i]-l[i-1]==1:
            k=k+1
            end=i
       else:
            if lenn<k:
                print k
                lenn=k
                end=i
                begin=end-lenn-1
                k=0
    print lenn+1,begin, end

listreplase([2,3,4,2,4,8,16,16])
listtypereplace([2,3,4,5,3.0,4.0,['bu'],[22,3],['dfd'],2])
sortListEndLeter(['big','bad','bum','enter','go'])
pasteInSortList(['bad', 'big', 'bum', 'enter', 'go'],'cmn')
twoList(['bad', 'big', 'bum', 'enter', 'go'], [1,2,3,4,5],'bum')
removeEven('qwe qw qwert qwer qw qwert')
sequence([1, 2, 3, 4, 6, 7, 8, 9, 10, 11,13])
