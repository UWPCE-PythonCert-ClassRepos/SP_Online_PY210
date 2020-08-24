#!/usr/bin/env python3
"""Trigrams assignment."""
import sys
import random
import string

# test out words
# test_words = ("I wish I may I wish I might I wish I could go home tonight"
#               " I wish upon a star tonight visible from home a star upon my"
#               " sight".split()
#               )


def read_in_data(filename):
    """Read text file."""
    body = False
    data = ''
    with open(filename, 'r') as file:
        for line in file:
            if line[:9] == '*** START':
                body = True
            if line[:7] == '*** END':
                body = False
            if body and not line.isupper():
                data += line.replace('\n', ' ')
    return data


def get_words(data):
    """Get useable trigram-worthy words from text data."""
    data = data.lower()
    for i in string.punctuation:
        if i not in ["'", "."]:
            data = data.replace(i, ' ')
    # print(data)
    return data.split()


def build_trigrams(words):
    """Build a trigrams dictionary.

    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
        if follower[-1] == '.':
            trigrams[pair].append(follower[:-1])
    return trigrams


def use_trigrams(trigrams):
    """Use the trigrams dictionary to create new text."""
    pair = random.choice([key for key in trigrams])
    text = list(pair)
    text[0] = text[0].capitalize().rstrip('.')
    text[1] = text[1].rstrip('.')
    period = False
    counter = len(text[0]) + len(text[1]) + 2
    while pair in trigrams and len(text) < 100:
        follower = random.choice(trigrams[pair])
        pair = (text[-1].lower().replace('\n', ''), follower)
        if period or follower == "i" or follower[:2] in ["i.", "i'"]:
            follower = follower.capitalize().rstrip('.')
            period = False
        if follower[-1] == '.':
            period = True
        if follower[0] == "'":
            follower.lstrip("'")
        counter += len(follower)+1
        if counter >= 60:
            follower = follower + '\n'
            counter = 0
        # print(counter, follower)
        text.append(follower)
    return ' '+' '.join(text) + '.'


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename)
    words = get_words(in_data)
    trigrams = build_trigrams(words)
    # for n, item in enumerate(trigrams.items()):
    #     if n < 30:
    #         print(item)
    #     else:
    #         break
    print(use_trigrams(trigrams))
