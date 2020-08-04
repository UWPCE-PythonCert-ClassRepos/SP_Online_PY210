#!/usr/bin/env python3

"""
Lesson 3: Trigram assignment
Course: UW PY210
Author: Jason Jenkins
"""

import random
import sys


def build_trigram(words):
    """
    build up the trigrams dict from the list of words
    """

    trigrams = dict()

    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if(pair in trigrams):
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    # build up the dict here!

    return trigrams


def make_words(text):
    """
    Splits a long string of text into an list of words
    """

    return text.split()


def build_text(word_pairs, iterations=100000):
    """
    Creates new text from a trigram
    """

    text_list = []

    # Create the start of the text
    first_two = random.choice(list(word_pairs.keys()))

    text_list.append(first_two[0])
    text_list.append(first_two[1])
    text_list.append(random.choice(word_pairs[first_two]))

    # Iterate to create a long text stream
    for i in range(iterations):
        last_two = tuple(text_list[-2:])
        if last_two in word_pairs:
            text_list.append(random.choice(word_pairs[last_two]))

    return " ".join(text_list)


def read_in_data(filename):
    """
    Reads in text from a file
    """

    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]

    except IndexError:
        print("You must pass in a valid filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)
