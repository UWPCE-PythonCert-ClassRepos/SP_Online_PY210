#!/usr/bin/env python


def build_trigrams(words):
    '''Build trigrams data structure using word list input
    
    returns a dict with:
        keys: word pairs
        values: list of following word(s)
    '''

    trigrams = {}

    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        key = tuple(pair)
        if key not in trigrams.keys():
            trigrams[key] = [follower]
        else:
            trigrams[key].append(follower)

    return trigrams


if __name__ == '__main__':
    
    words = "I wish I may I wish I might".split()
    print(build_trigrams(words))

