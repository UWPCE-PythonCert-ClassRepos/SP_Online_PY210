#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons
# Edited: 12/27/2020 - csimmons

import sys
import random
input = 'sherlock_small.txt'
welcome_prompt = "\nWelcome to the automatic book generator!"

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

def cleaner(all_lines):
    clean_lines = all_lines.replace('\n', ' ').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '').replace(':', '')
    clean_lines = clean_lines.split(' ')
    # removes any null entries in clean_lines
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
    # multiplier used to determine size of text generated for
    # variable output sizes
    multiplier = 5
    num_trigrams = len(trigrams.keys())
    word_list = []
    for i in range(num_trigrams * multiplier):
        key, value = random.choice(list(trigrams.items()))
        w_one, w_two = key
        w_three = random.choice(value)
        word_list.extend([w_one, w_two, w_three])
    process_text(word_list, trigrams)
    
def process_text(word_list, trigrams):
    # Can add other types of trigram post processing here, including 
    # re-adding punctuation, capitalization, etc. This function is
    # easily extendable
    output_text = ' '.join([str(word) for word in word_list])
    # prints both trigram dict and randomly generated text.
    print('\nHere is the trigram dictionary:\n\n', trigrams)
    print('\nHere is your randomly generated text:\n\n', output_text)


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