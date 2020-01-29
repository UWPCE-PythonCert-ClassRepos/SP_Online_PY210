#!/usr/bin/env python3


def build_trigrams(words_list):
    """
    create trigrams dict from a list of words
    :param words_list: a list of words
    :return: returns a dict of pairs(key) and their followers
    """
    trigrams = {}
    for i in range(len(words_list)-2):
        pair = words_list[i:i + 2]
        pair = tuple(pair)
        follower = words_list[i + 2]
        follower = list(follower.split())
        if pair in trigrams:
            trigrams[pair].extend(follower)
        else:
            trigrams.update({pair: follower})
    return trigrams
