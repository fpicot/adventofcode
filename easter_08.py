#!/usr/bin/python
import re,sys,time,curses

screen = [[0 for x in range(50)] for y in range(6)]

_input = 'easter_08.input'
_re = re.compile('^(?:rotate|rect) (?:(?:row|column) (x|y)=(\d+) by (\d+)|(\d+)x(\d+))$')

def rotate(l, n):
    return l[-n:] + l[:-n]

with open(_input) as f:
  for line in f:
    line = line.rstrip()
    result = _re.match(line)
    if result:
      if result.group(1): #Rotate
        row = 1 if result.group(1) == "y" else 0 
        index = int(result.group(2))
        value = int(result.group(3))
        if row:
          screen[index] = rotate(screen[index], value)
        else:
          column = [screen[y][index] for y in range(6)]
          column=rotate(column,value)
          for y in range(6):
            screen[y][index] = column[y]

      else: #Rect
        _x=int(result.group(4))
        _y=int(result.group(5))
        for x in range(_x):
          for y in range(_y):
            screen[y][x] = 1
    else:
      print ("This should not happen")


result = sum([sum(screen[y]) for y in range(6)])

print ("Nombre de pixels : {}".format(result))
print ('')
#Print
for y in range(6):
  for x in range(50):
    state = "X" if screen[y][x]==1 else "."
    print(state, end='')
  print('')

