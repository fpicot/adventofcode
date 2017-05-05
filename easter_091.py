#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

_input = 'easter_09.input'
_re = re.compile('([^(]*)?(?:\((\d+)x(\d+)\))?(.*)?')

uncompressed=''
with open(_input) as f:
  compressed=f.read().replace('\n', '')

working=compressed
while len(working):
  results=_re.search(working)
  length=int(results[2]) if results[2] else 0
  count=int(results[3]) if results[3] else 0
  uncompressed+=results[1]+count*results[4][0:length]
  working=results[4][length:]


print("Taille Décompressée : {}".format(len(uncompressed)))

