#!/usr/bin/python
# -*- coding: utf-8 -*-
import operator

input_file = "easter_06.input"
letters = ['','','','','','','','']
result = ''

#Analyse frequentielle
def freq(text):
   _d = dict()
   for letter in text:
     if letter not in _d:
       _d[letter] = text.count(letter)

   #Tri par nombre d'occurences
   _od = sorted(_d.items(), key = operator.itemgetter(1), reverse=False)
   return _od[0][0]

#Lecture du fichier, et extraction par colonne
for line in open(input_file):
  values = line.rstrip('\n')
  for i in range(8):
    letters[i-1]+=values[i-1]

#Récupération de la lettre la plus présente de chaque colonne
for text in letters:
  result+=freq(text)


print(result)




