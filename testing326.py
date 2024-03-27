#!/usr/bin/env python
# coding: utf-8


#testing1
import re     #Regualr expression
a= re.compile(r'が')
result_split = a.split('私がリンゴを食べます')
print(result_split)   #['私', 'リンゴを食べます']


#tesing2
import re
text = '私がリンゴを食べます'
result_split = re.split(r'が|を|ます', text)    # pattern
print(result_split)

final= []
for i in result_split:
    if i:
        final.append(i)
print(final)

#tesing3
S = '私がリンゴを食べます'
rule = r'^(.*?)が(.*?)を(.*?)ます$'     #^是符合的那個字串的起點，$是符合那個字串的最後面
r = re.match (rule, S)                 #re.match來找匹配的字串，

if r:
    Sub = r.group(1)                   #然後用group的語法來分組
    Obj = r.group(2)
    Vb = r.group(3)
    
    print("Sub", Sub)
    print("Obj:", Obj)
    print('Vb:', Vb)
