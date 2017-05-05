#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

_input = 'easter_09.input'
_re = re.compile('([^(]*)?(?:\((\d+)x(\d+)\))?(.*)?')

with open(_input) as f:
  compressed=f.read().replace('\n', '')

def uncomp_size(working): 
  if len(working):
    results=_re.search(working)
    length=int(results[2]) if results[2] else 0
    count=int(results[3]) if results[3] else 0
    return len(results[1]) + uncomp_size(count*results[4][0:length]) + uncomp_size(results[4][length:])
  else:
    return 0

print("Taille Décompressée : {}".format(uncomp_size(compressed)))

