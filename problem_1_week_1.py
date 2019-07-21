# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:16:39 2019

@author: DESSHAM2
"""

s = 'azcbobobegghakl'

count = 0

for char in range (len(s)-2):
    if s[char:char+3] == 'bob':
        count += 1
print("Number of times bob occurs is: " + str(count))

