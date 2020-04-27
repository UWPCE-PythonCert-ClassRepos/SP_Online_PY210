#!/usr/bin/env python3

'''
Objectives
Katas are about trying something many times. In this one, what we’re experimenting with is not just the code, but the heuristics of processing the text. What do we do with punctuation? Paragraphs? Do we have to implement backtracking if we chose a next word that turns out to be a dead end?

I’ll fire the signal and the fun will commence…
'''

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
    for i in range(len(words) -2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        trigrams.setdefault(tuple(pair),[]).append(follower)
    return trigrams

def random_text(text, length):
    new_text = list(random.choice(list(text.keys())))
    key = tuple(new_text[-2:])
    while key in text:
        value = random.choice(text[key])
        new_text.append(value)
        key = tuple(new_text[-2:])
        if len(new_text) > length:
            break
    return new_text

if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)