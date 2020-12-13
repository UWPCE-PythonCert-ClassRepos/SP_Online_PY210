#!/usr/bin/env python3
# Craig Simmons
# Python 210
# file_lab.py 
# Created 12/6/2020 - csimmons

import sys
import os 
import pathlib

donorlist_dict = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Rutolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

donor = ''
gift = ''

def generate_letter(donorlist_dict):
    isdir = os.path.isdir('letters')  
    print(isdir)
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
        
letter = (('\nDear {},\n\n'
        'We would like to thank you for your recent - and extremely\n'
        'generous - donation of ${:,.2f} to the Famous Charity of Seattle\n'
        'and Greater King County. Your gift will help thousands, perhaps\n'
        'even millions, enjoy the wonders of the Emerald city!\n\n'
        'Sincerely,\n\n'
        'H.P. Lovecraft \n'))

generate_letter(donorlist_dict)