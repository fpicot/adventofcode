#!/usr/bin/python

count=0
input_file = "easter_03.input" 

#Mise au propre de l'input
input = [[int(x) for x in line.rstrip('\n').split()] for line in open(input_file)]

#Verification des triangles
for list in input:
  list.sort()
  if (list[0] + list[1]) > list[2]:
    count += 1


print 'Nombre de triangles : {}'.format(count)


