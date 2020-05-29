#!/usr/bin/env python3

import random

words_test = "I wish I may I wish I might".split()


def make_words(file):
    f = open(file, 'r')
    words_ready = f.read()
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in words_ready:
        if char in punctuations:
            words_ready = words_ready.replace(char, " ")
    return words_ready


def build_trigrams(words_raw):
    trigrams = {}
    words = words_raw.split()
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams.setdefault(pair, []).append(follower)
    return trigrams


def build_text(word_pairs):
    first_pair = random.choice(list(word_pairs.keys()))
    third = random.choice(word_pairs[first_pair])
    new_text = list(first_pair) + [third]

    for i in range(0, 50):
        new_pair = new_text[-2:]
        if tuple(new_pair) in word_pairs.keys():
            new_text = new_text + [random.choice(word_pairs[tuple(new_pair)])]
        else:
            break
    return ' '.join(new_text).capitalize() + '.'


if __name__ == "__main__":
    file_test = 'sherlock_small.txt'
    words_raw_test = make_words(file_test)
    word_pairs_test = build_trigrams(words_raw_test)
    new_text_test = build_text(word_pairs_test)
    print(new_text_test)
