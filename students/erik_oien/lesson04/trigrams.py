#!/usr/bin/env python3

import sys
import os
import random
import string

words = "I wish I may I wish I might".split()

def read_in_data(filename):
    f = open(filename, 'r')
    return f.read()

def make_words(in_data):
    data = in_data.replace('-', ' ').replace('(', '').replace(')', '').replace(',', '').replace("\"", "").replace("'", "").replace(":", "").replace(";", "").replace('.', '').replace('!', '').replace('?', '').split()
    return data

def build_trigram(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2): # why -2 ?
        key = tuple(words[i:i + 2])
        follower = words[i + 2] 
        if key in trigrams:
            trigrams[key].append(follower)
        else:
            trigrams[key] = [follower]

    return trigrams

def build_text(word_pairs):
    sentence = []
    sentence_length = random.randint(5, 20)
    word_pair = random.choice(list(word_pairs))
    for word in word_pair:
        sentence.append(word)
    while len(sentence) < sentence_length:
        next_pair = tuple(sentence[-2:])
        if next_pair in word_pairs:
            sentence.append(random.choice(word_pairs[next_pair]))
        else:
            next_pair = random.choice(list(word_pairs))
            sentence.append(random.choice(word_pairs[next_pair]))
    return (" ".join(sentence).capitalize()+". ").replace(" i ", " I ").replace("i.", "I.")

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)