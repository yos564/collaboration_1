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
