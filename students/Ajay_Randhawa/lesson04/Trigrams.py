#!/usr/bin/env python3

import random
import itertools

#words = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might', 'I', 'wish', 'might', 'wish']

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with: 
        keys: word pairs
        values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        curr_word = words[i]
        next_word = words[i+1]
        next1_word = words[i+2]
        key = (curr_word, next_word)
        if key in trigrams:
            trigrams[key].append(next1_word)
        else:
            trigrams[key] = [next1_word]
    print(trigrams)
    return trigrams

def build_text(word_pairs):
    '''
    returns new text using the trigrams dict

    starts with a known pair.
    checks if the known pair equals an existing dict key and adds the value to list
    '''

    l = []
    a = list(word_pairs.keys())
    a = a[:1]
    for x, y in a:
        l.append(x)
        l.append(y)
        
    for key, values in word_pairs.items():
        if key[0] == l[-2] and key[1] == l[-1]:
            l.append(values[0])
    l = " ".join(l)
    return l

def read_in_data():
    '''
    reads a text file and returns a list of words
    skips the first 62 lines
    '''
    a = []
    with open('sherlock.txt', 'r') as g:
        for _ in range(62):
            next(g)
        for line in g:
            lang = line.strip().split(" ")
            #append 'lang' to empty list 'list1'
            a.append(lang)
    a = list(itertools.chain.from_iterable(a))
    return a



if __name__ == "__main__":
    words = read_in_data()
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams)
    print(new_text)
    
    



