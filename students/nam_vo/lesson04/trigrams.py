#!/usr/bin/env python3

import sys, random

def read_in_data(filename):
    """Return a list of all words in filename"""

    words = []

    # Read input file
    with open(filename, 'r') as f:
        while True:
            # Read each line
            line = f.readline()
            # Done reading
            if not line:
                break
            # Skip header
            if line.find('***'):
                # Add all words from each line
                words += line.split()

    return words

def build_trigram(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        # trigrams.setdefault(pair, [follower])
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    return trigrams

def build_text(trigrams, pair):
    """
    build up some new text from the trigrams

    return a new text
    """

    if pair in trigrams:
        # Get the first word associated with the pair and remove it from the list
        word = trigrams[pair].pop(0)
        # Remove the pair if there is no word associated with it
        if len(trigrams[pair]) == 0:
            trigrams.pop(pair)
        # Update the pair
        pair = (pair[1], word)
        # Continue building new text from the reduced trigrams
        return " ".join([word, build_text(trigrams, pair)])
    else:
        return ''

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    words = read_in_data(filename)

    print(f"words = {words}\n")

    word_pairs = build_trigram(words)

    # Pick a random pair from the trigrams
    pair = random.choice(list(word_pairs.keys()))

    new_text = build_text(word_pairs, pair)

    print(f"new_text = {new_text}\n")
