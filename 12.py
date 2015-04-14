#!/usr/bin/env python
import random
def letters(bigstring):
    UpText= ''
    for i in bigstring:
        if i.isupper():
            UpText=UpText+i
    return UpText

def palindrome(pali):   
    if  pali==pali[::-1]:
        return 'palindrome:yes'
    else:
        return 'palindrome:no'
        
def find_letter(where, letter):
    t= where.split()
    p=[]
    for i in t:
        if i[0].lower()==letter:
            p.append(i)
    return p
def mix_words(just_string):
    t=just_string.split()
    mix=''
    while len(t)>1:
        rnd = random.randint(0, len(t)-1)
        mix=mix+' '+t[rnd] 
        del t[rnd]
    return mix+' '+t[0]
    
    
print letters("Trees Are So Kind")  
print palindrome("avid diva")
print find_letter("Bears are the best animals ever", 'b')
print mix_words("Bears are the best animals ever")
