__author__ = 'hackoff'

import string
class Parser:
    def __init__(self):
        try:
            file=open('input', 'r')
        except:
            print 'file not found'
        listLine=[]
        listSpace=[]
        for line in file:
            LineNoSpace='<'+string.lstrip(line).replace('\n','')+'>'
            listLine.append(LineNoSpace)
            listSpace.append(len(line)-len(LineNoSpace)+1)
        try:
            fileW=open('out','w')
        except:
            print 'pizdez'
        before=''
        after=''
        insertedTag=False
        insertedTagNo=False
        space=' '
        while len(listLine):
            spaceCountBefore=listSpace[len(listSpace)-2]
            spaceCount=listSpace.pop()
            lineTag=listLine.pop()
            lineTagClose=lineTag.replace('<','</')
            insertedTagNo=False
            if spaceCount<spaceCountBefore:
                insertedTagNo=True
            if insertedTag:
                if insertedTagNo:
                    before=space*spaceCount+lineTagClose+'\n'+before+after+space*spaceCount+lineTag+'\n'
                    after=''
                else:
                    if after=='':
                        after=before
                        before=''
                    before=before+space*spaceCount+lineTagClose+'\n'+after+space*spaceCount+lineTag+'\n'
                    after=''
            else:
                after=after+space*spaceCount+lineTagClose+'\n'+space*spaceCount+lineTag+'\n'

            insertedTag=False
            if spaceCount>spaceCountBefore:
                insertedTag=True
        fileW.write('\n'.join(before.split('\n')[::-1]))


objectParser= Parser()