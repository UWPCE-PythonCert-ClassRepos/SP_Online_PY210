#!/usr/bin/env python3

"""
Lesson 3: Trigram assignment
Course: UW PY210
Author: Jason Jenkins
"""


words = "I wish I may I wish I might".split()


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
    trigrams = build_trigrams(words)
    print(trigrams)