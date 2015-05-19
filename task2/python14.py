__author__ = 'hackoff'
#lab1.4
def twokort():
    #2b
    d=dict([(1,2),('g','s'),('m','n')])
    print d

def twhospisoksosisok():
    #2a
    a=['a','b','c']
    b=['1','2','3']
    d=dict(zip(a,b))
    print d

def poiskpozn(stroka,sl):
    #3
    for el in sl:
        if stroka==sl[el]:
           sl[el]=None
    print sl

def twhoslremoveduplicat(a,b):
    #4
    print a,b
    for el in b.keys():
        if el in a.keys():
            del a[el]
            del b[el]
    a.update(b)
    print a


def calculate(operand,a,b):
    #5
    oper={'add':a+b, 'mult':a*b}
    print oper[operand]

def kruchyverchy(a):
    return dict(zip(a.values(),a.keys()))


twokort()
twhospisoksosisok()
twhoslremoveduplicat({'one':1,'g':22,'t':77}, {'l':2,'g':2,'ttt':'df'})
calculate('mult',2,4)
print kruchyverchy({'one':1,'g':22,'t':77})
poiskpozn('df',  {'l':2,'g':2,'ttt':'df'})