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
trigrams = {}

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
    for i in range(len(clean_words)-2):
        pair = tuple(clean_words[i:i+2])
        third = clean_words[i+2]
        if pair in trigrams:
            trigrams[pair].append(third)
        else:
            trigrams[pair] = [third]
    print(trigrams)
    build_text(trigrams)



    # print(trigram_len)
def build_text(trigrams):
    masterpiece_size = 500
    first, second = random.choice(tuple(trigrams.keys()))
    word_pair = (first.title(), second)
    masterpiece = list(word_pair)
    print('Starting key: ', word_pair)


    while len(masterpiece) <= masterpiece_size:
        if word_pair in trigrams:
            print('word_pair in trigrams:')
            print(word_pair)
            print(len(masterpiece), masterpiece_size)
            masterpiece.append(random.choice(trigrams[word_pair]))
            print(masterpiece)
            word_pair = tuple(masterpiece[-2:])
            print('new word pair: ', word_pair)
        else:
            print('word_pair NOT in trigrams:')
            word_pair = random.choice(list(trigrams.keys()))
            print(word_pair)
    


def main(input):
    print(input)
    print(welcome_prompt)
    open_file(input)
    

        

if __name__ == '__main__':
    main(input)