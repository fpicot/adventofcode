#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

input_file = "easter_07.input"
count = 0
    
for line in open(input_file):
  HS = []
  SS = []
  seq = ''
  for char in line:
  
    #Start Hypernet Sequence
    if char == '[':
      HS.append(seq)
      seq = ''
    elif char == ']':
      SS.append(seq)
      seq = ''
    else:
      seq += char
  SS.append(seq) 
  
  print line
  print HS
  print SS
  print 'XXXX'

#line[i] != line [i+1] and line[i] == line[i+3] and line[i+1] == line[i+2]:


