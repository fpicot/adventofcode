#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import operator 

base = "L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2"

coordinates = [0,0]
axe = 0

#Internal use
_dir = [[0,1],[1,0],[0,-1],[-1,0]]
_reg = re.compile('([LR])([0-9]*)')

#Preparation
inputs = base.split(', ')
for input in inputs:
	#Extraction
	result = _reg.match(input)

	#Conversion de la la direction
	axe += 1 if  result.group(1) == "L" else -1
	axe = axe % 4

	#Recuperation de la distance
	dist=int(result.group(2))

	#Calcul des coordonnees
	coordinates =  map(operator.add, coordinates, [x*dist for x in _dir[axe]])
	
print "Distance = {}".format(sum(map(abs,coordinates)))
