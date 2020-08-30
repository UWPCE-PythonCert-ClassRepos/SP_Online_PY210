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
        temp_list = []
        pair = tuple(words[i:i+2])
        follower = words[i+2]
        temp_list.append(follower)
        if pair not in trigrams:
            trigrams[pair] = temp_list
        else:
            trigrams[pair].append(follower)

    return trigrams

#Main Exicutable
if __name__ == '__main__':
    trigrams = build_trigrams(words)
    print(trigrams)