#!/usr/bin/env python3
import random

"""Produce a trigram using The Adventures of Sherlock Holmes.

"""
#testing the script using a small string to get the code correct
words = "I wish I may I wish I might".split()

"""example of how the dict should look:

trigrams = 
{("I wish"): ["I", "I"],
("wish I"): ["may", "might"],
("I may"): ["I"],
("may I"): ["wish"],}

Examples of generated text to expect if using words as the original text:
[I wish I may I wish I might]
[I wish I might]
[I wish I may I wish I may I wish I might] #and so on...
"""
trigrams = {}

def build_trigrams(a_seq):
    """Build up the trigrams dict from the list of words above.
    
    returns a dict of:
        keys: adjacent word pairs
        values: the word that immediately follows the last word of the key
    """
    for x in range(len(a_seq) - 2):
        pair = tuple(a_seq[x:x + 2]) # will be the keys in trigrams. try frozen sets instead of tuples
        follower = a_seq[x + 2] # will be the values in trigrams

        #try to update this to use defaultdict(list) instead
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    return trigrams

def generator():
    #TESTING: update first word pair in new_text to be determined randomly & test with longer string
    new_text = ["I", "wish"]

    while tuple(new_text[-2:]) in trigrams:
        new_text.append(random.choice(trigrams[tuple(new_text[-2:])]))
    
    return new_text

def main():


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)
    
    #test that a longer string works
    more_words = "I am trying to come up with a longer string than words".split()

    assert build_trigrams(more_words)
    print("test passed")