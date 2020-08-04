#!/usr/bin/env python3

"""
Lesson 3: Trigram assignment
Course: UW PY210
Author: Jason Jenkins
"""

# Global
words = "I wish I may I wish I might".split()
trigrams = {}

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!

    return trigrams


if __name__ == "__main__":
    # get the filename from the command line
    print("Program Started")
    """
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)
    """