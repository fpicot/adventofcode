#!/usr/bin/python

count=0

input_file = "easter_03.input" 
input = []

_A = []
_B = []
_C = []
_x=0

#Mise au propre de l'input
for line in open(input_file):
  values = line.rstrip('\n').split()
  _A.append(int(values[0]))
  _B.append(int(values[1]))
  _C.append(int(values[2]))
  _x+=1
  if (_x % 3 == 0):
    input.append(_A)
    input.append(_B)
    input.append(_C)
    _A = []
    _B = []
    _C = []

#Verification des triangles
for list in input:
  list.sort()
  if (list[0] + list[1]) > list[2]:
    count += 1

print 'Nombre de triangles : {}'.format(count)


