#!/usr/bin/env python3

import random
import itertools
import string
import re

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
    #print(trigrams)
    return trigrams

def build_text(word_pairs):
    '''
    returns new text using the trigrams dict

    starts with a known pair.
    checks if the known pair equals an existing dict key and adds the value to list
    else
    it find a random pair to keep going
    '''

    l = []
    a = list(word_pairs.keys())
    a = a[:1]
    for x, y in a:
        l.append(x)
        l.append(y)
    a = list(word_pairs.keys())
    for key, values in word_pairs.items():
        if key[0] == l[-2] and key[1] == l[-1]:
            z = random.randint(1,2)
            try:
                l.append(values[0])
            except IndexError:
                l.append(values[0])
        else:
            random_entry = random.choice(a)
            random_entry = random_entry[:2]
            l.append(random_entry[0])
            l.append(random_entry[1])

    l.append('......TO BE CONTINUED.')
    l = " ".join(l)
    return l

def read_in_data(filename):
    '''
    reads a text file and returns a list of words
    skips the first 62 lines
    '''
    a = []
    with open(filename, 'r') as g:
        for _ in range(62):
             next(g)
        for line in g:
            words = line.split()
            #convert to lower case
            words = [word.lower() for word in words]
            #translate each word to remove the punctuation
            table = str.maketrans('', '', string.punctuation)
            stripped = [w.translate(table) for w in words]
            a.append(stripped)
    a = list(itertools.chain.from_iterable(a))
    return a




if __name__ == "__main__":
    words = read_in_data('sherlock.txt')
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams)
    print(new_text)
    
    



