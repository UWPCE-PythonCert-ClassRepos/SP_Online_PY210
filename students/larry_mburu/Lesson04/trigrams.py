#!/usr/bin/env python3

import sys
import random
import string

#words = "I wish I may I wish I might I might have seen magic do bigger texts make triagrams a thing of specialty ?".split()


def build_trigram(words_list):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!
    # ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']

    for words in words_list: 
        for i in range(len(words) - 2): #why - 2?
            pair = tuple(words[i:i + 2])
            follower = words[i + 2]

            #if key not in dict, return empty list, then append follower
            #if key in in dict, return mapped list, then append follower
            trigrams.setdefault(pair, []).append(follower) 

    return trigrams

def build_text(word_pairs): 
    """
    build new form text from a trigrams dict. 

    param: word_pairs: dict of trigrams

    returns a newly formed string
    """

    #print(word_pairs)
    fake_text = []

    #retrieve an initial starting word_pair(key)
    intial_word_pair = random.choice(list(word_pairs))
    fake_text.extend(intial_word_pair)
    following_word = word_pairs.get(intial_word_pair)
    if len(following_word) >= 1: 
        fake_text.append(random.choice(following_word))
    #print(fake_text)

    while True: 
        #dict key is in tuple form
        next_key = tuple(fake_text[-2:])
        next_words = word_pairs.get(tuple(next_key)) 
        if next_words is None: 
            break
        if len(next_words) >= 1: 
            fake_text.append(random.choice(next_words))
    
    return ' '.join(fake_text).capitalize()

def read_in_data(filename):
    """
    reads filename per line, calls remove_characters that removes: 
        punctuation marks, new line '\n' char, 
    Finally, splits clean line sentence into a list of words. 

    returns a list of list of words
    """
    words_data = []

    with open(filename) as fobj: 
        for line in fobj: 
            if line.startswith('***'): #begin read after, beginning header.
                break 
        for line in fobj: 
            if line.startswith('***'): #stop read before, ending header. 
                break
            cleaned_line = remove_characters(line)
            words = cleaned_line.split()
            words_data.append(words)

    return words_data

def remove_characters(line):
    """
    removes punctuation marks, new line '\n' char
    
    param: line: line to clean up

    returns a string
    """
    # remove punctuation marks
    line = line.translate(str.maketrans('', '', string.punctuation))
    # remove end-of-line '\n', char. 
    line = line.strip()
    # split() line into list of words. 
    return line

if __name__ == "__main__":
    #get the filename from the command line
    try: 
        filename = sys.argv[1] 
    except: 
        print("You must pass in a filename")
        sys.exit(1)

    words = read_in_data(filename)
    for r in range(len(words)):
        word_pairs = build_trigram(words)
        new_text = build_text(word_pairs)
        print(new_text)