# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:05:53 2020

@author: miriam
"""
import random
import sys


def read_in_data(my_file):
    start = False
    words = ''
    with open(my_file, 'r') as f:
        for line in f:
            if '*** START OF THIS PROJECT GUTENBERG EBOOK' in line:
                start = True
                continue
            if start:
                no_dashes = line.replace('--', ' ')
                no_commas = no_dashes.replace(',', '')
                no_paren_1 = no_commas.replace('(', '')
                no_paren_2 = no_paren_1.replace(')', '')
                words += no_paren_2
    return words


def make_words(data):
    words_list = data.split()
    return words_list


def build_triagram(words_list):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    word_pairs = {}
    for i in range(len(words_list)-2):
        pair = tuple(words_list[i:i + 2])
        follower = words_list[i + 2]
        if pair not in word_pairs.keys():
            word_pairs[pair] = [follower]
        else:
            word_pairs[pair].append(follower)
    return word_pairs


def build_text(word_pairs):
    new_text = []
    tri_keys = list(word_pairs.keys())
    word_pair = tri_keys[0]
    new_text.extend(word_pair)
    sent_count = 0
    while True:
        if word_pair in word_pairs:
            next_word = random.choice(word_pairs[word_pair])
            print(word_pair, next_word)
            new_text.append(next_word)
            if new_text[-1].endswith('.') and new_text[-1] not in ['Mr.']:
                if len(new_text) > 150:
                    break
                word_pair = random.choice(tri_keys)
                new_text.extend(word_pair)
                new_text[-2] = new_text[-2].capitalize()
                print(new_text[-2:], word_pair)
                sent_count = sent_count + 1
            word_pair = tuple(new_text[-2:])
        else:
            word_pair = random.choice(tri_keys)
    text = ' '.join(new_text)
    return text


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = 'sherlock.txt'
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_triagram(words)
    new_text = build_text(word_pairs)
    print(new_text)