#!/usr/bin/env python
# coding: utf-8


import re     #Regualr expression
role = re.compile(r'が')
result_split = role.split('私がリンゴを食べます')
print(result_split)   #['私', 'リンゴを食べます']





