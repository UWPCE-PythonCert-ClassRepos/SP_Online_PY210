#!/usr/bin/env python3

import random

words = "I wish I may I wish I might".split()  # a list
new_text_length = 300

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = words[i], words[i+1]  # a tuple
        follower = words[i+2]
        # if pair (key) is in the dict, return the list (value) to add the follower
        # if not, insert the pair (key), return the empty list to add the follower
        trigrams.setdefault(pair, []).append(follower)
    return trigrams

def build_text(dict):
    random_key = random.choice(list(dict)) # convert to list first, return a tuple
    new_text = [random_key[0], random_key[1]]

    while True:
        if random_key in dict.keys(): # key in the dict
            new_text.append(random.choice(dict.get(random_key)))
        else:
            break

        if (len(new_text) > new_text_length):
            break

        random_key = new_text[-2], new_text[-1]

    return " ".join(new_text) + '.'

def make_words(file):
    """
    make a list of words from an input file

    returns a list of words
    """
    with open(file, 'r') as f:
        in_data = f.read()

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in in_data:
        if char in punctuations:
                in_data = in_data.replace(char, " ")

    return in_data.split()

if __name__ == "__main__":
    filename = 'sherlock_small.txt'

    words = make_words(filename)
    trigrams = build_trigrams(words)
    #print(trigrams)
    print(build_text(trigrams))



