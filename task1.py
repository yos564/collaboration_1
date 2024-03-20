#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inputSTR = input()
inputLIST = list(inputSTR)

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
    li = caseparse(inputLIST)
    for i in range(li[0]):
        return inputLIST[i]
    
def extractObject(inputLIST):
    li = caseparse(inputLIST)
    i = li[0] + 1
    for i in range(li[1]):
        return inputLIST[i]
    
def extractVerb (inputLIST):
    li = caseparse(inputLIST)
    i = li[1] + 1
    for i in range(li[2]):
        return inputLIST[i]


Subject=extractSubject(inputLIST)
Object=extractObject(inputLIST)
Verb=extractVerb (inputLIST)

