#!/usr/bin/env python3
import os
import time
import sys
import operator
import contextlib
from operator import itemgetter

# Mailroom (Part 2)
donors_dictionary = {'first' : 'Jonny', 'last' : 'Gill', 'donationhistory' : [3.00, 15.00, 25.12],
            'first' : 'Bobby', 'last' : 'Brown', 'donationhistory' : [11.75, 45.01],
            'first' : 'Michael', 'last' : 'Bivins', 'donationhistory' : [345.99],
            'first' : 'Ricky' , 'last' : 'Bell' , 'donationhistory' : [232.33, 35.03, 123.78],
            'first' : 'Ronnie', 'last' : 'DeVoe' , 'donationhistory' : [456.00, 789.00]}

def list_donors_full_func():
    print('\n***** Printing Donors and Donations *****')
    for key, value in donors_dictionary.items(): # prints all donors (key) and donation (value)
        print(len(donors_dictionary))
        print(key, '\t', value)
    print()
    #main_menu_func() # returns to main menu
    return

def list_donors_func():
    #print('You selected \"Create a Report\"')
    print()
    print('***** Printing Donors *****')
    for key in donors_dictionary.keys():
        print(key)
        time.sleep(0.5)
    print('*'*25) # formatting
    print()
    #thank_you_func()
    return

def list_all_values():
    for value in donors_dictionary.values():
        print(value)
    return


if __name__ == "__main__":
    list_donors_full_func()
    list_donors_func()
    list_all_values()
