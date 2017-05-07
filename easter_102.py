#!/usr/bin/python
# -*- coding: utf-8 -*-
import re,weakref,itertools

_input = 'easter_10.input'
bots = []
inputbins = []
outputbins = {}


class robot:
  bots = weakref.WeakValueDictionary()

  def __init__(self, name, low_type, low_id, high_type, high_id ):
    self.name = name
    self.low_type = low_type
    self.low_id = low_id
    self.high_type = high_type
    self.high_id = high_id

    self.A = None
    self.B = None
    self.bots[self.name] = self

  def load_chip(self,value):
    if not self.A:
      print("Bot {} is loading first chip ({})".format(self.name,value))
      self.A = value
    elif not self.B:
      print("Bot {} is loading second chip ({})".format(self.name,value))
      self.B = value
      self.unload_chips()
    else:
      raise Exception("Bot {} is loading a third chip".format(self.name))

  def unload_chips(self):
    print("Bot {} is giving chips {} and {}".format(self.name,self.A,self.B))
    low = min(self.A,self.B)
    high = max(self.A,self.B)
    if self.low_type == "bot":
        robot.bots[self.low_id].load_chip( low )
    else:
        outputbins[self.low_id] = low        
    if self.high_type == "bot":
        robot.bots[self.high_id].load_chip( high )
    else:
        outputbins[self.high_id] = high
    self.A = None
    self.B = None

def read_file(input_file):
  _re_bot = re.compile('^bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)$')
  _re_bin = re.compile('^value (\d+) goes to bot (\d+)$')
  
  with open(input_file) as f:
    for line in f:
      line = line.rstrip()
      bot = _re_bot.match(line)
      bin = _re_bin.match(line)
      if bot:
        bots.append( robot(bot[1],bot[2],bot[3],bot[4],bot[5]))
      elif bin:
        inputbins.append([bin[2],int(bin[1])])
      else:
        raise Exception ("Unable to interpret line : {}".format(line))


read_file(_input)
for inputbin in itertools.cycle(inputbins):
  robot.bots[inputbin[0]].load_chip(inputbin[1])
  if (('0' in outputbins) and ('1' in outputbins) and ('2' in outputbins)):
    print ('Resultat : {}'.format(outputbins['0']*outputbins['1']*outputbins['2']))
    quit()
