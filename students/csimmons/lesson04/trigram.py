#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons

import sys
import os
import random
#input = 'small.txt'
input = 'sherlock_small.txt'
welcome_prompt = "\nWelcome to the automatic book generator!\n"
trigrams = {}

def open_file(input):
    with open (input, 'r') as textfile:
        while True:
            line = textfile.readline()
            if not line:
                break
            print('line is type: ', (type(line)))
            print(line)
            clean_line(line)

def clean_line(line):
    line = line.replace('\n', '').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '')
    clean_words = line.split(' ')
    print('clean_words type: ', type(clean_words))
    print(len(clean_words))
    #print('clean_words themselves: ', clean_words)
    process_text(clean_words)

def process_text(clean_words):
    for i in range(len(clean_words)-2):
        pair = tuple(clean_words[i:i+2])
        third = clean_words[i+2]
        if pair in trigrams:
            trigrams[pair].append(third)
        else:
            trigrams[pair] = [third]
    create_text(trigrams)

def create_text(trigrams):
    starting_pair = random.choice(tuple(trigrams.keys()))
    print(starting_pair, type(starting_pair))
    new_text = ''.join(starting_pair)
    print(new_text)
    while starting_pair in trigrams:
        word = random.choice(trigrams[starting_pair])
        print(word)
        new_text = new_text + ' ' + word
        print(new_text)
        starting_pair = starting_pair[1], word
        print(starting_pair)




def main(input):
    print(input)
    print(welcome_prompt)
    open_file(input)
    

        

if __name__ == '__main__':
    main(input)