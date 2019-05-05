#!/usr/bin/env python3
import random
from collections import defaultdict
import pprint
import re
import random


def words(file_in):
    with open(file_in, 'r') as infile:
        x = infile.read()
        x = re.sub(r'[^\w\s]', ' ', x).lower()
        x = x.split()
    return x


def build_trigrams(words):
    trigrams = defaultdict(list)
    for i in range(len(words) - 2):
        element = "{} {}".format(words[i], words[i+1])
        trigrams[element].append(words[i+2])
    return trigrams


def build_text(trigrams):
    seed_key = random.choice(list(trigrams.keys()))
    sentence_length = random.randint(15, 20)
    while True:
        current_key

    return first_key


if __name__ == "__main__":
    file_in = "./sherlock.txt"
    # print(words(file_in))
    trigrams = build_trigrams(words(file_in))
    pprint.pprint(trigrams)
    # build_text(trigrams)
