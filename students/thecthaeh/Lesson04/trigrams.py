#!/usr/bin/env python3
import random
from collections import defaultdict
import sys

"""Produce a trigram using The Adventures of Sherlock Holmes. 

The trigram breaks the given text into groups of three adjacent words where the first two words 
act as a dict key and the third word acts as a value. The next word group starts with the second 
word of the previous group. This pattern continues through the end of the text.

Example of how a trigrams dict should look using the string "I wish I may I wish I might":

trigrams = 
{("I wish"): ["I", "I"],
("wish I"): ["may", "might"],
("I may"): ["I"],
("may I"): ["wish"],}

Examples of generated text to expect if using the above string as the original text:
[I wish I may I wish I might]
[I wish I might]
[I wish I may I wish I may I wish I might] #and so on...
"""

filename = './sherlock_small.txt'

def build_trigrams(words):
    """Build up the trigrams dict from a list of words.
    
    returns a dict with:
        keys: adjacent word pairs
        values: a list of words that immediately follow the key
    """
    trigrams = defaultdict(list)
    pf_list = []
    
    for x in range(len(words) - 2):
        pair = words[x:x + 2] # will be the keys in trigrams.
        follower = words[x + 2] # will be the values in trigrams.
        pf_list.append([pair, follower])

    for pair, follower in pf_list:
        trigrams[tuple(pair)].append(follower)

    return trigrams

def use_trigrams(trigrams, words):
    """Create the new text using the trigrams dict.
    
    """
    
    #determine a random first word pair
    text = [pair for pair in random.choice(list(trigrams.keys()))]
    
    #build the rest of the list
    while len(text) < len(words):
        if tuple(text[-2:]) not in trigrams:
            text.append(random.choice(words))
            if text[-1] == text[-2]:
                del text[-1]
                text.append(random.choice(words))
        else:
            text.append(random.choice(trigrams[tuple(text[-2:])]))
    
    text_str = " ".join(text)

    return f"{text_str}."

def text_processor(filename):
    """Take in a given file and use it to create the word list.
    
    """

    with open(filename, 'r') as f:
        read_data = f.read()
        words = read_data.split()
    
    return words

if __name__ == "__main__":
    
    words = text_processor(filename)
    trigrams = build_trigrams(words)
    new_text = use_trigrams(trigrams, words)
    
    print(new_text)