#!/usr/bin/python
import re
import operator

input_file = "easter_04.input" 
_reg = re.compile('([a-z\-]*)-([0-9]*)\[([a-z]{5})\]')

#Analyse frequentielle
def freq(text):
   _d = dict()
   for letter in text:
     if letter not in _d:
       if letter != '-': 
	 #On multiplie par -1 pour pouvoir trier dans le meme ordre
         _d[letter] = -1 * text.count(letter) 
   
   _od = sorted(_d.items(), key = operator.itemgetter(1,0))
   return _od

#Dechiffrement du nom
def decypher(id,text):
  _key = list("abcdefghijklmnopqrstuvwxyz")
  _result = ''
  for l in text:
    _result += _key[(_key.index(l) + id) % 26] if not l == "-" else ' '
  return _result
   
#Parcours du fichier
for line in open(input_file):
  #Extraction des elements
  match = _reg.match(line)
  name = match.group(1)
  id = int(match.group(2))
  checksum = match.group(3)
  
  #Calcul du checksum
  _od = freq(name)
  checksum_calc = '{}{}{}{}{}'.format(_od[0][0],_od[1][0],_od[2][0],_od[3][0],_od[4][0])

  #Comparaison  
  if checksum_calc == checksum:
    cleartext = decypher(id,name)
    if cleartext == "northpole object storage":
      print id




