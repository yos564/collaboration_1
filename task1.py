#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inputSTR = input()
inputLIST = list(inputSTR)

sub = extractSubject(inputLIST)
print("sub is", sub)
obj = extractObject(inputLIST)
print("obj is", obj)
verb = extractVerb(inputLIST)
print("verb is", verb)

def caseparse(inputLIST):
    li = [0, 0, 0]
    for i in range(len(inputLIST)):
        if inputLIST[i] == 'が':
            li[0] = i
        if inputLIST[i] == 'を':
            li[1] = i
        if inputLIST[i] == 'ま':
            li[2] = i
    return li
    
def extractSubject(inputLIST):
    li0 = inputLIST
    li = caseparse(li0)
    li2 = list()
    for i in range(li[0]):
        li2.append(inputLIST[i])
    return''.join(li2)

def extractObject(inputLIST):
    li0 = inputLIST
    li = caseparse(li0)
    li2 = list()
    i = li[0] + 1
    while i < li[1]:
        li2.append(inputLIST[i])
        i+=1
    return''.join(li2)

def extractVerb(inputLIST):
    li0 = inputLIST
    li = caseparse(li0)
    li2 = list()
    i = li[1] + 1
    while i < li[2]:
        li2.append(inputLIST[i])
        i+=1
    return''.join(li2)