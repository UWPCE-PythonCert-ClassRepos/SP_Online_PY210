#!/usr/bin/env python3
import random
from collections import defaultdict
import pprint
import re


def words(file_in):
    with open(file_in, 'r') as infile:
        x = infile.read()
        x = re.sub(r'[^\w\s]', ' ', x).lower()
        x = x.split()
    return x


def build_trigrams(words):
    trigrams = defaultdict(list)
    for i in range(len(words) - 2):
        element = (words[i], words[i+1])
        trigrams[element].append(words[i+2])
    return trigrams


def build_text(trigram_dict, length):
    working_text = list(random.choice(list(trigram_dict.keys())))
    key = tuple(working_text[-2:])
    while key in trigram_dict:
        value = random.choice(trigram_dict[key])
        working_text.append(value)
        key = tuple(working_text[-2:])
        if len(working_text) > length:
            break
    return working_text


def paragraph(trigram_dict, num_para, length):
    for number in range(num_para):
        text = " ".join(build_text(trigram_dict, length))
        text = text.capitalize()
        print("\t{}.".format(text))
    return


if __name__ == "__main__":
    file_in = "./sherlock.txt"
    trigrams = build_trigrams(words(file_in))
    paragraph(trigrams, 2, 100)
