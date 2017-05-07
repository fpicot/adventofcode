#!/usr/bin/python
# -*- coding: utf-8 -*-
import re,weakref,itertools

_input = 'easter_10.input'
bots = []
bins = []

class robot:
  bots = weakref.WeakValueDictionary()

  def __init__(self, name, low, high ):
    self.name = name
    self.low_id = low
    self.high_id = high
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
    if ((low == 17) and (high == 61)):
        print( "We found it : {}".format(self.name))
        quit() 
    if self.low_id:
        robot.bots[self.low_id].load_chip( low )
    if self.high_id:
        robot.bots[self.high_id].load_chip( high )
    self.A = None
    self.B = None

def read_file(input_file):
  # We don't care about output bins
  _re_bot = re.compile('^bot (\d+) gives low to (?:output \d+|bot (\d+)) and high to (?:output \d+|bot (\d+))$')
  _re_bin = re.compile('^value (\d+) goes to bot (\d+)$')
  
  with open(input_file) as f:
    for line in f:
      line = line.rstrip()
      bot = _re_bot.match(line)
      bin = _re_bin.match(line)
      if bot:
        bots.append( robot(bot[1],bot[2],bot[3]))
      elif bin:
        bins.append([bin[2],int(bin[1])])
      else:
        raise Exception ("Unable to interpret line : {}".format(line))


read_file(_input)
for input in itertools.cycle(bins):
    robot.bots[input[0]].load_chip(input[1])
