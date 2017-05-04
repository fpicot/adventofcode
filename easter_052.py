#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import hashlib

input = "wtnhxymk" 
password = list('________')
_reg = re.compile('^0{5}(.)(.)')
_i = 0
_n = 0

while _n < 8:
  hash = hashlib.md5(input + str(_i)).hexdigest()
  result = _reg.match(hash)
  if result:
    pos = result.group(1)
    letter = result.group(2)
    if pos.isdigit() and int(pos) < 8 and password[int(pos)] == '_':
      _n += 1
      password[int(pos)] = letter
      print "Password : {}".format(''.join(password))
  _i += 1

