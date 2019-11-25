#!/usr/bin/env python3

import random
import sys

"""
Steve Morehouse - Lesson 04
trigrams
"""

"""
read in the book and return raw data
"""
def read_in_data (filename):
    with open (filename, "r") as input:
        for line in input:
            book = input.read()
    return book


"""
from the raw data read in, return a list
"""
def make_words (in_data):
    # clean up
    translate_chars = str.maketrans(',.?!;()-\"', '         ')
    in_data = in_data.translate (translate_chars)
    return in_data.split()

"""
build up the trigrams dict from the list of words
returns a dict with:
   keys: word pairs
   values: list of followers
"""
def build_trigram (words):

    trigrams = {}

    # build up the dict here!
    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        next = words[i+2]
        if pair in trigrams:
            trigrams[pair].append(next)
        else:
            trigrams[pair] = [next]

    return trigrams

"""
from a dictionary, return new_text
"""
def build_text (word_pairs):
    word_list = []

    random_pair = random.choice(list(word_pairs))
    for word in random_pair:
        word_list.append(word)

    while len(word_list) <= 999:
        new_pair = tuple(word_list[-2:])

        if new_pair in word_pairs:
            word_list.append(random.choice(word_pairs[new_pair]))
        else:
            random_pair = random.choice(list(word_pairs))
            word_list.append(random.choice(word_pairs[random_pair]))

    new_text = " ".join(word_list)
    return new_text


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
