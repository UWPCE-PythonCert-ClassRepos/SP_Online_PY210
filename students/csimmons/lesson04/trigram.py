#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons

import sys
import os
import random
input = 'small.txt'

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


def build_text(trigrams):
    masterpiece_size = 500
    #first, second = random.choice(tuple(trigrams.keys()))
    # starting_key = [first.title(), second]
    starting_key = random.choice(tuple(trigrams.keys()))
    masterpiece = ' '.join(starting_key)
    print(starting_key, type(starting_key))
    print(masterpiece, type(masterpiece))
    #while len(masterpiece) <= len(trigrams.items()):
    while len(masterpiece) <= masterpiece_size:
        print(len(masterpiece), len(trigrams.items()), len(trigrams.keys()))
        next = random.choice(trigrams[starting_key])
        print(next)
        masterpiece = masterpiece + ' ' + next
        print(masterpiece)
        starting_key = starting_key[1], next
        print(starting_key)
    
    # trigram_len = len(trigrams.items())
    # print(trigram_len)
    
   

 
    '''
     text_len = random.randint(5,(len(trigrams.keys())-3))
    key_test = tuple(word_list[-2:])
    print(word_list, len(word_list), text_len, key_test)
    while len(word_list) < text_len:    
        if key_test in trigrams.keys():
            word_list.append(random.choice(list(trigrams[(word_list[-2],word_list[-1])])))
        else:
            word_list.append(random.choice(list(trigrams.values())))
    '''

    
    
    #return " ".join(list_wof_words).capitalize()clear
    #for i in range(len(trigrams)):
        #key = random.choice(tuple(trigrams.keys()))
        #print(key)
 


'''
    while (start_key in wp and len(text) <= max_size):
        w = random.choice(wp[start_key])  # get a random word from dictonary
        text = text + " " + w
        start_key = start_key[1], w  # new key of 2nd word and new word
        #print("current key ", start_key)
    return text
    new_text = ''.join(starting_pair)
    #print(new_text)
    #print(len(trigrams))

    for i in range(len(trigrams)):
        key = random.choice(tuple(trigrams.keys()))CLEr
        print(key)
'''





def main(input):
    print(input)
    print(welcome_prompt)
    open_file(input)
    

        

if __name__ == '__main__':
    main(input)