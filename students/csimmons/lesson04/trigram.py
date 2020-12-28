#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons

import sys
import os
import random
input = 'sherlock_small.txt'

welcome_prompt = "\nWelcome to the automatic book generator!\n"

# read file working solid
def read_file(input):
    all_lines = ''
    with open(input, 'r') as textfile:
        while True:
            line = textfile.readline()
            if not line:
                break
            all_lines = all_lines + line
    textfile.close()
    print('In read_file(): ', all_lines)
    cleaner(all_lines)

# cleaner working solid
def cleaner(all_lines):
    clean_lines = all_lines.replace('\n', ' ').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '').replace(':', '')
    clean_lines = clean_lines.split(' ')
    clean_lines = list(filter(None, clean_lines)) 
    print('In cleaner(): ', clean_lines)
    #process_text(clean_words)
    
'''
def process_text(clean_words):
    trigrams = {}
    for i in range(len(clean_words)-2):
        pair = tuple(clean_words[i:i+2])
        third = clean_words[i+2]
        if pair in trigrams:
            trigrams[pair].append(third)
        else:
            trigrams[pair] = [third]
    #build_text(trigrams)
    print(trigrams)
    

def pick_random(trigrams):
    key, value = random.choice(list(trigrams.items()))
    w_one, w_two = key
    w_three = random.choice(value)
    return(w_one, w_two, w_three) 

    

def build_text(trigrams):
    num_trigrams = len(trigrams.keys())
    print(num_trigrams)
    fair_copy = []
    for x in range(num_trigrams):
        print(x)
        pick_random(trigrams)
        #fair_copy = w_one + ' ' + w_two + ' ' + w_three + ' '
        print(fair_copy)

'''



def main(input):
    read_file(input)
    

if __name__ == '__main__':
    main(input)