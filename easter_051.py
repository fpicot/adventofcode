#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import hashlib

input = "wtnhxymk"
password = ''
_reg = re.compile('^0{5}(.)')
_i = 0
_n = 0

while _n < 8:
  result = _reg.match(hashlib.md5(str(input + str(_i)).encode('utf-8')).hexdigest())
  if result:
    password += result.group(1)
    _n += 1
  _i += 1

print("Password : {}".format(password))
