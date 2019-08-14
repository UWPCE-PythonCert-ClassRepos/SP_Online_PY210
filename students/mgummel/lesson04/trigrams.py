#!/usr/bin/env python3
import random
from pprint import pprint


words = "I wish I may I wish I might".split()
HEADER = "*** START OF THIS PROJECT GUTENBERG EBOOK"


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if follower:
            trigrams.setdefault(pair, list())
            trigrams[pair].append(follower)
    return trigrams

def read_in_data(file_to_parse):
    word = list()
    with open(file_to_parse, mode='r', encoding='utf-8') as a_file:
        for line in a_file:
            line = line.replace("\n", "")
            word += line.split(" ")
    return word
        




if __name__ == "__main__":
    text = read_in_data('sherlock.txt')
    trigrams = build_trigrams(text)
    #print(trigrams)