#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

input_file = "easter_07.input"
count = 0

for line in open(input_file):
  TLS = False
  HS = False
  i=0

  while i < len(line)-3:
    #Start Hypernet Sequence
    if line[i] == '[': HS=True
    #End Hypernet Sequence
    elif line[i] == ']': HS=False
    elif line[i] != line [i+1] and line[i] == line[i+3] and line[i+1] == line[i+2]:
      #If in Hypernet, can't be TLS, skip end of line
      if HS== True: 
        TLS=False
        break
      else:
        TLS=True
    i+=1
  if TLS==True:
    count +=1

print(count)



