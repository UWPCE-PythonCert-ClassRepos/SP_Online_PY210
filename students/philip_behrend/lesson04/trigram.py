# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:12:33 2019

@author: Philip Behrend
"""
import random
import os
import re
import sys
os.chdir(r'C:\Users\Gemini\UW_PYTHON\SP_Online_PY210\students\philip_behrend\lesson04\\')

#!/usr/bin/env python3

words = "I wish I may I wish I might".split()
filename = 'sherlock_small.txt'

def read_data(filename):
    with open(filename, 'r') as f:
        contents = f.read().split()
    
    # Strip punctuation and make lowercase
    contents = [re.sub(r'[^\w\s]','',i) for i in contents]
    contents = [i.lower() for i in contents]
    return contents

def make_trigram(words):
    """
    Build up trigram dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """   
    trigram = {}
    for i in range(len(words)-2):
        new_key = (words[i], words[i+1])
        if new_key not in trigram.keys():
            trigram[new_key] = []
        if words[i+2] not in trigram[new_key]:
            trigram[new_key].append(words[i+2])
    return trigram

    
def generate_text(trigram, word_count = 100):
    """
    Given input trigram dict, returns randomly generated text
    """
    word_ls = []
    start_key = random.choice(list(trigram))
    word_ls.append(start_key[0])
    word_ls.append(start_key[1])
    curr_key = start_key
    
    # Generate next words
    for i in range(word_count):
        next_index = random.randint(0,len(trigram[curr_key])-1)
        word_ls.append(trigram[curr_key][next_index])
        curr_key = tuple(word_ls[-2:])
        
        if curr_key not in trigram.keys():
            curr_key = random.choice(list(trigram))
            word_ls.append(curr_key[0])
            word_ls.append(curr_key[1])
    return word_ls

if __name__ == "__main__":
    try:
        filename = sys.argv[1]  
    except IndexError:
    print("You must pass in a filename")
    sys.exit(1)
    
    in_data = read_data(filename)
    trigram = make_trigram(in_data)
    new_text = generate_text(trigram)

    print(new_text)