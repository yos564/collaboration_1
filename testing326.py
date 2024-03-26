#!/usr/bin/env python
# coding: utf-8


#testing1
import re     #Regualr expression
role = re.compile(r'が')
result_split = role.split('私がリンゴを食べます')
print(result_split)   #['私', 'リンゴを食べます']


#tesing2
import re
text = '私がリンゴを食べます'
result_split = re.split(r'が|を|ます', text)    # pattern
print(result_split)

