#!/usr/bin/env python3

words = "I wish I may I wish I might".split()

#print(words)

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    for word in range(len(words)-2):
        pair = words[word:word+2]
        print(pair)

    trigrams = {}
    # build up the dict here!

    return trigrams

if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)
