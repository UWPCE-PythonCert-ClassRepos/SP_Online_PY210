#!/usr/bin/env python3
import random
import defaultdict

def words(file_in):
        with open(file_in, 'rb') as infile:
                infile.read().split
                infile.close()

def build_trigrams(words):

    trigrams = {}
    for i in range(len(words) - 2)
    element = "{} {}".format(words[i], words[i+1])
    trigrams[element] = {words[i+3]}

    # build up the dict here!

    return trigrams


if __name__ == "__main__":
    file_in = "sherlock.txt"
    trigrams = build_trigrams(words(file_in))
    print(trigrams)
