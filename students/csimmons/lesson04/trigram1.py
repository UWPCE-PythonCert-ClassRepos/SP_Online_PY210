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


def open_file(input):
    all_lines =[]
    with open (input, 'r') as textfile:
        while True:
            line = textfile.readline()
            all_lines.append(line)
            if not line:
                break
            print(all_lines)
        print(all_lines)
            #clean_line(line)

def clean_line(line):
    line = line.replace('\n', '').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '').replace(':', '')
    clean_words = line.split(' ')
    print(clean_words)
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
    print(trigrams)
    #build_text(trigrams)
    

def pick_random(trigrams):
    key, value = random.choice(list(trigrams.items()))
    w_one, w_two = key
    w_three = random.choice(value)
    return(w_one, w_two, w_three) 

    

def build_text(trigrams):
    print(trigrams)
    # num_trigrams = len(trigrams.keys())
    num_trigrams = 100
    print(num_trigrams)
    fair_copy = []
    for x in range(num_trigrams):
        print(x)
        pick_random(trigrams)
        fair_copy.append(w_one)
        fair_copy.append(w_two)
        fair_copy.append(w_three)

        print(fair_copy)





def main(input):
    print(input)
    print(welcome_prompt)
    open_file(input)
    

if __name__ == '__main__':
    main(input)