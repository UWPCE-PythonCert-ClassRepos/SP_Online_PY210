#!/usr/bin/env python3
# Craig Simmons
# Python 210
# dict_lab.py 
# Created 12/4/2020 - csimmons

import sys
import os 
import pathlib
from operator import itemgetter

donorlist_dict = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Rutolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }
    for i in range(len(words)-2): # why -2 ?
   pair = words[i:i + 2]
   follower = words[i + 2]
word_list = word_library(text_file)
    trigram = {}
    for i in range(len(word_list)-2):
        pair = tuple(word_list[i:i+2])
        nextword = word_list[i+2]
        trigram.setdefault(pair, []).append(nextword)
    return 

def dict_list(donorlist_dict):
    donors = donorlist_dict.keys()
    gifts = donorlist_dict.values()
    print(donors)
    print(type(donors))
    print(gifts)
    print(type(gifts))
    print('______________')
    for key, value in donorlist_dict.items():
        donor = str(key.replace(' ', '_'))
        gift = (list(value))[-1]
        print(donor, gift)

dict_list(donorlist_dict)

def generate_letters(donorlist_dict):
    isdir = os.path.isdir('letters')  
    if isdir == True:
        pass
    else:
        os.mkdir('letters')
    for key, value in donorlist_dict.items():
        donor = str(key.replace(' ', '_'))
        gifts = list(value)
        gift = float(gifts[-1])
        full = letter.format(donor, gift)
        print(full)
        filename = 'letters/' + donor + '.txt'
        with open(filename, 'w') as output:
            output.write(full)
        output.close
