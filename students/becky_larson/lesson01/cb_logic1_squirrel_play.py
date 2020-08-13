#!/usr/bin/env python

def squirrel_play(temp, is_summer):
  lowTemp=60
  highTemp=90
  if is_summer: highTemp=100
  
  if (temp >= lowTemp) and (temp <= highTemp):
    return True
  else:
    return False
    
squirrel_play(70, False)
squirrel_play(95, False)
squirrel_play(95, True) 