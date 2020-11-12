#! /usr/bin/env python3
## Lesson 4 Exercise, Trigrams Kata 14
## By: B. Matthews
## 10/21/2020
## https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/kata_fourteen.html

import os
import sys
import string
import random

new_text = "nothing"

def read_in_data(fn):
    """gets text from a file to use in generating new text file"""

    with open(fn, 'r') as f:
        all_lines = f.readlines()
    return all_lines

def make_words(data):
    """strips out the words from a big chunk of text file, returns list of strings"""
    lots_of_words = []

    for eachLine in data:
        lots_of_words = lots_of_words + eachLine.split()

    return lots_of_words

def build_trigram(w):
    """build a dictionary using word pairs from the file as keys"""

    key_words = w[0] + ' ' +w[1]
    third_word = w[2]
    print("key words=", key_words)
    print("third=", third_word)

    trigrams = {}
    return

def build_text(wp):
    """generate a new text file using the word order data from the input file"""


    return


if __name__ == "__main__":
    ## get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please enter a filename of a text file after the executable name")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    #new_text = build_text(word_pairs)

    print(new_text)


