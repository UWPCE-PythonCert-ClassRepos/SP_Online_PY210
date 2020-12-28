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
    cleaner(all_lines)

# cleaner working solid
def cleaner(all_lines):
    clean_lines = all_lines.replace('\n', ' ').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '').replace(':', '')
    clean_lines = clean_lines.split(' ')
    clean_words = list(filter(None, clean_lines)) 
    create_trigrams(clean_words)
    
def create_trigrams(clean_words):
    trigrams = {}
    for i in range(len(clean_words)-2):
        pair = tuple(clean_words[i:i+2])
        third = clean_words[i+2]
        if pair in trigrams:
            trigrams[pair].append(third)
        else:
            trigrams[pair] = [third]
    build_text(trigrams)

def build_text(trigrams):
    multiplier = 1
    num_trigrams = len(trigrams.keys())
    word_list = []
    for i in range(num_trigrams * multiplier):
        key, value = random.choice(list(trigrams.items()))
        w_one, w_two = key
        w_three = random.choice(value)
        word_list.extend([w_one, w_two, w_three])
    process_text(word_list)
    
def process_text(word_list):
    output_text = ' '.join([str(word) for word in word_list]) 
    print(output_text)


def main(input):
    read_file(input)
    

if __name__ == '__main__':
    try:
        input = 'sherlock_small.txt'
        print(welcome_prompt)
        main(input)
    except IndexError:
        print('Error, program exiting')
        sys.exit()