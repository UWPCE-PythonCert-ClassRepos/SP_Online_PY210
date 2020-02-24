#!/usr/bin/env python3


import os
import sys


def read_file(filename = 'sherlock_small.txt'):
    '''
    Read file contents, store in text variable.
    '''

    with open(filename, 'r') as f:
        text = f.read()
        return text


def clean_file_text(text = text):
    '''
    Clean text for processing:
    1. Replace non-alpha characters with whitespace
    2. Join characters together as lowercase
    3. Strip and split whitespace from text to get a list of words.
    '''

    for c in text:
        # print(c)
        if c.isalpha() is False:
            text = text.replace(c, ' ')
        else:
            continue
    text = "".join(text).lower()
    text = text.strip().split()
    return text


def build_trigram_dict(text = text):
    '''
    '''

    trigram_dict = {}

    for i in range(len(text) - 2):
        pair = tuple(text[i:i + 2])
        follower = text[i + 2]
        if pair not in trigram_dict.keys():
            entry = {pair: []}
            trigram_dict.update(entry)
        trigram_dict[pair].append(follower)


    return trigram_dict

def test_trigram(string):
    string = ''
    pass