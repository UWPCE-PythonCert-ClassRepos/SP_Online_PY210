#!/usr/bin/env python3

import sys
import random

def read_in_data(filename):
    """ Open a file and return the contents """
    with open(filename, "r") as input:
        for line in input:
            content = input.read()
    return content

def make_words(content):
    """ Take a string of text and return a list of words """
    content = content.replace("--", " ")
    content = content.lower()
    words = content.split()
    return words

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    
    # Create a blank dictionary
    trigrams = {}

    # Loop through words in list and create tuple/list values
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]

        # Loop through the dictionary and add/update
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    return trigrams

def build_text(trigrams):
    """ Take a dictionary of trigrams and return new text """
    
    # Start an empty list
    word_list = []

    # Get a random word pair from dictionary and add to list
    rand_pair = random.choice(list(trigrams))
    for word in rand_pair:
        word_list.append(word)

    max_words = 200
    while len(word_list) <= max_words:
        # Get the last two words in list
        new_pair = tuple(word_list[-2:])
        
        if new_pair in trigrams:
            # Add a random follower to the list
            word_list.append(random.choice(trigrams[new_pair]))
        else:
            # Pick a new random pair of words and add follower
            rand_pair = random.choice(list(trigrams))
            word_list.append(random.choice(trigrams[rand_pair]))

    # Join the word list and return new text
    new_text = " ".join(word_list)
    return new_text

if __name__ == "__main__":
    # Get the filename from the command line, assumes same directory
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