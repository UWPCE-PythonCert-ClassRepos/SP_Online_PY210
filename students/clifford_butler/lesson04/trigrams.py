#!/usr/bin/env python3

'''
Objectives
Katas are about trying something many times. In this one, what we’re experimenting with is not just the code, but the heuristics of processing the text. What do we do with punctuation? Paragraphs? Do we have to implement backtracking if we chose a next word that turns out to be a dead end?

I’ll fire the signal and the fun will commence…
'''

#!/usr/bin/env python3

words = "I wish I may I wish I might".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        
        pair = words[i:i + 2]
        follower = words[i + 2]
        #trigrams[pair].append(follower)
        trigrams.setdefault(tuple(pair),[]).append(follower)
    return trigrams

if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)