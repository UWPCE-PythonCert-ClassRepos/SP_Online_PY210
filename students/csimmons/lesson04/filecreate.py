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
def send_letters(donorlist_dict):
    #file = 'donorletter.txt'
    #os.mkdir('letters')
    donors = list(donorlist_dict.keys())
    all_gifts = list(donorlist_dict.values())
    print(donors)
    print(all_gifts)
    for gifts in all_gifts:
        gift = int(gifts[-1])
        print(gift)
    for donor in donors:
        donor = donor.replace(' ', '_')
        print(donor +'.txt')



def generate_letter(donorlist_dict):
    for key, value in donorlist_dict.items():
        donor = key.replace(' ', '_')
        print(donor)
        gifts = list(value)
        gift = int(gifts[-1])
        print(gift)
        print(letter)

letter = (('\nDear {},\n\n'
        'We would like to thank you for your recent - and extremely\n'
        'generous - donation of ${:,.2f} to the Famous Charity of Seattle\n'
        'and Greater King County. Your gift will help thousands!\n'
        'Sincerely,\n\n'
        'HP Lovecraft \n'.format(donor, gift)))

def send_letters(donorlist_dict):


generate_letter(donorlist_dict)