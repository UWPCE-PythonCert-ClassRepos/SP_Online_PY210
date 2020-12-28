#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons

import sys
import os
import random
input = 'sherlock_small.txt'
w_one = w_two = w_three = ''

welcome_prompt = "\nWelcome to the automatic book generator!\n"


def open_file(input):
    with open (input, 'r') as textfile:
        while True:
            line = textfile.readline()
            if not line:
                break
            clean_line(line)

def clean_line(line):
    line = line.replace('\n', '').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '').replace(':', '')
    clean_words = line.split(' ')
    process_text(clean_words)
    

def process_text(clean_words):
    trigrams = {}
    for i in range(len(clean_words)-2):
        pair = tuple(clean_words[i:i+2])
        third = clean_words[i+2]
        if pair in trigrams:
            trigrams[pair].append(third)
        else:
            trigrams[pair] = [third]
    build_text(trigrams)
    

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
        fair_copy = w_one + ' ' + w_two + ' ' + w_three + ' '
        print(fair_copy)





def main(input):
    print(input)
    print(welcome_prompt)
    open_file(input)
    

if __name__ == '__main__':
    main(input)