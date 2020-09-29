#!/usr/bin/env python3

import sys
import random


def make_words(filename):
    #make words from a local .txt file.  Assuming from Project Gutenberg.
    words = []
    skip = False
    with open(filename, 'r', encoding="utf8") as file:
        for line in file:
            #don't process some lines
            if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:
                skip=True

            if "End of the Project Gutenberg EBook" in line:
                skip=True
            #process this line
            if skip=False:
                        words.extend(line.split())
            skip=False
    return words


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(0, len(words) - 2):
        pair = words[i:i+2]
        follower = words[i + 2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams

def build_text(word_pairs):
    #build some made up text
    size = random.randint(5,10)

    first = random.randint(0 , len(word_pairs))
    word_pair = list(list(word_pairs.keys())[first])
    new_text = word_pair

    while len(new_text) <= size:

        try:
            next = random.randint(0 , len(word_pairs))
            word_pair = list(list(word_pairs.keys())[next])
            new_text.extend([word_pair])
        except:
            break

    return " ".join(new_text).capitalize() + '.'


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    words = make_words(filename)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)
