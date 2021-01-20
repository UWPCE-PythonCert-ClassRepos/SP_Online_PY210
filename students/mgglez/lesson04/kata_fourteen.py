#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson04 - Assignment 3 - Kata Fourteen
# Description: Assignment from Lesson04 - Kata Fourteen (Graded)
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-16-2021, Created Kata Fourteen Script
# ------------------------------------------------------------------------------ #
import os
import sys
import random
import string


words = "I wish I may I wish I might".split()

def read_in_data(filename):
    if not os.path.exists(filename):
        filename = 'sherlock_small.txt'
    with open(filename, 'r') as fh:
        data = fh.readlines()
    return data

def make_words(in_data):
    words = []
    for line in in_data:
        if line.strip() != '':
            formatted_line = line.replace("--", " ")
            formatted_line = formatted_line.strip().translate(str.maketrans('', '', string.punctuation))
        words.extend(formatted_line.split())
    return words

def build_trigram(words):
    """
    Build up the trigrams dict from the list of words
    :params words: (list) List of words
    :return: (dict) with keys as (tuple) of word pairs & values as (list) of followers
    """
    trigram = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigram.setdefault(pair, [])
        trigram[pair].append(follower)
    return trigram

def build_text(word_pairs):
    words = []
    key = random.choice(list(word_pairs.keys()))
    print("Starting random key: {}".format(key))
    words.extend(list(key))

    while (key in word_pairs):
        follower_list = word_pairs[key]
        follower_index = random.randint(0, len(follower_list) - 1)
        follower_chosen = follower_list[follower_index]
        words.append(follower_chosen)
        key = tuple(words[-2:])

    return " ".join(words)

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    print(words)
    word_pairs = build_trigram(words)
    print(word_pairs)
    new_text = build_text(word_pairs)
    print(new_text)

