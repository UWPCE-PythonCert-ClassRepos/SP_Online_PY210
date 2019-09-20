#!/usr/bin/env python3

words = "I wish I may I wish You might I wish I may I wish I might I wish I may I wish I might".split()


def build_trigrams(words):
    """
    Build up the trigrams dict from the list of words.

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = words[i:i + 2]
        key = (pair[0], pair[1])
        follower = [words[i + 2]]

        trigrams.setdefault(key, []).append(follower)

    return trigrams


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)

