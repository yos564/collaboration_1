#!/usr/bin/env python
# coding: utf-8

# In[ ]:

f = open("inputSTR.txt", "r")
inputSTR = f.read().replace('\n'," ")
whole_list = inputSTR.split('。 ')

def caseparse(inputLIST):
    index_list = [0, 0, 0]
    index_list[0] = inputLIST.index('が') if 'が' in inputLIST else 0
    index_list[1] = inputLIST.index('を') if 'を' in inputLIST else 0
    index_list[2] = inputLIST.index('ま') if 'ま' in inputLIST else 0
    return index_list
    
def extractSubject(inputLIST):
    index_list = caseparse(inputLIST)
    sub = inputLIST[0:index_list[0]]
    return''.join(sub)

def extractObject(inputLIST):
    index_list = caseparse(inputLIST)
    obj = inputLIST[index_list[0]+1:index_list[1]]
    return''.join(obj)

def extractVerb(inputLIST):
    index_list = caseparse(inputLIST)
    if index_list[1] != 0:
        verb = inputLIST[index_list[1]+1:index_list[2]]
    else:
        verb = inputLIST[index_list[0]+1:index_list[2]]
    return''.join(verb)

    
for i in whole_list:
    inputLIST = list(i)
    
    for j in inputLIST:
        if j == ' ' or j == '。':
            inputLIST.pop(inputLIST.index(j))
    
    resultDICT = {"Subject":extractSubject(inputLIST), "Object":extractObject(inputLIST), "Verb":extractVerb(inputLIST)}

    print(f"Results for sentence {whole_list.index(i)+1}: \nresultDICT = ","{")
    for k,v in resultDICT.items():
        print("\t\t",k,":",v)
    print('\t       }')