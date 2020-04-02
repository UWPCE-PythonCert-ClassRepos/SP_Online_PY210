#!/usr/bin/env python3
import random
import sys
import re
import string



def read_in_data(filename):
    print(filename)
    start = False
    in_data = ''
    with open(filename, 'r') as f:
        for line in f:
            if '***' in line: #start the reading after this symbol
                start = True
                continue
            if start:
                line = re.sub("[^0-9a-zA-Z' ]+",' ',line)
                line = re.sub('  ',' ',line.lower())
                quote1 = line.replace(" '", '')
                quote = quote1.replace("' ", '')
                precaps = ['george', 'burnwell', 'holmes', 'sherlock', ' i ', 'mr ', 'mrs ',"i'll", "i'm", "i'd", "i've"]
                postcaps = ['George', 'Burnwell', 'Holmes', 'Sherlock', ' I ', 'Mr. ', 'Mrs. ', "I'll", "I'm", "I'd", "I've"]
                for i in range(len(precaps)):
                    quote = quote.replace(precaps[i], postcaps[i])
                final = quote.replace(' i ', ' I ')


                in_data += final
    return in_data

def make_words(in_data):
    words_list = in_data.split()

    return words_list

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    pair = []
    follower = []

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if pair not in trigrams.keys():
            trigrams[pair] = [follower]
        else:
            trigrams[pair].append(follower)

    return trigrams

def build_text(word_pairs):

    t_keys = random.choice(list(word_pairs.keys()))
    #print(list(word_pairs.keys())[:250])
    text = list(t_keys)
    #print(text)
    try:
        while True:
            if len(text) > 250: # generates a couple of hundred words of text
                break
            else:
                next_word = word_pairs[tuple(t_keys)]
                if type(next_word) == list:
                    next_word = random.choice(list(next_word))
                text.append(next_word)
                word_text = ' '.join(text)
                t_keys = text[-2:]
    finally:
        return (word_text[0].capitalize() + word_text[1:] + '.')




if __name__ == "__main__":
        # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)
