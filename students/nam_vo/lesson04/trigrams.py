#!/usr/bin/env python3

import random

words = "I wish I may I wish I might".split()

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    print(f"words = {words}")

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
    trigrams = build_trigrams(words)
    print(f"trigrams = {trigrams}")

    # Pick a random pair from the trigrams
    pair = random.choice(list(trigrams.keys()))
    print(f"pair = {pair}")

    # Build new text from the trigrams
    text = build_text(trigrams, pair)
    print(f"text = {text}")

