#!/usr/bin/env python3
"""
Jack Anderson
02/24/2020
UW PY210
Lesson 04
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

    for word in range(len(words - 2):
        group = words[i:i + 2]

    # for i in range(len(words) - 2):
    #     pair = words[i:i + 2]
    #     follower = words[i + 2]
    #     key = tuple(pair)
    #     if key not in trigrams.keys():
    #         trigrams[key] = [follower]
    #     else:
    #         trigrams[key].append(follower)



    # build up the dict here!

    return trigrams


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)