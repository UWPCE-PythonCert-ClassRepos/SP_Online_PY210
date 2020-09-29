#!/usr/bin/env python

def xyz_there(str):
  #return (str.find('xyz') >= 0 and str.find('.xyz') == -1)
  loc = str.find('xyz')
  if loc == -1: return False
  else:
    if loc == 0: return True
    if str[loc-1:loc] == '.':
      if loc+3 >= len(str): return False
      else: return xyz_there(str[loc+3:])
    else: return True
