#!/usr/bin/env python3

"""PY210_SP - trigrams
author: Nick Miller"""

import sys
import os
import random
import re


def read_text(file_name):
    """
    takes in a text file, strips punctuation, makes everything lowercase, puts all words in a list
    :param file_name: file_name in same dir as program
    :return: list of words
    """
    with open(file_name, 'r') as f:
        words_list = f.read().split()
    f.close()
    words_list = [re.sub(r"([a-z])--([a-z])", r"\1 \2", i, 0, re.IGNORECASE) for i in words_list]
    words_list = [re.sub(r'[^\w\s]', '', i) for i in words_list]
    words_list = [words for segments in words_list for words in segments.split()]
    words_list = [i.lower() for i in words_list]
    return words_list


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


def make_new(words_dict, words_list):
    """
    given a dict of trigrams and a list of words, return a new text based on the dict
    :param words_dict: a dictionary with key pairs and a list of their followers
    :param words_list: a list of words
    :return: a string of new text, the list of words processed based on the dict
    """
    rand_int = random.randint(0, len(words_list)-3)
    text = words_list[rand_int:rand_int + 2]
    choice = tuple(text)
    random_text = random.choice(words_dict.get(choice))
    while len(text) < 250:
        while choice == (words_list[-2], words_list[-1]):
            text.pop()
            choice = (text[-2], text[-1])
            print(text)
            while len(words_dict.get(choice)) == 1:
                if len(text) == 2:
                    text.pop()
                    rand_int = random.randint(0, len(words_list)-3)
                    text.extend(words_list[rand_int:rand_int + 2])
                    choice = tuple(text)
                    break
                else:
                    text.pop()
                    choice = (text[-2], text[-1])
        random_text = random.choice(words_dict.get(choice))
        text.append(random_text)
        choice = (choice[-1], random_text)
    return " ".join(text)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("please supply the name of a valid base file to use")
        sys.exit(1)
# filename = "sherlock.txt" testing
if os.path.isfile(filename):
    words_in = read_text(filename)
    trigram = build_trigrams(words_in)
    hot_off_the_press = make_new(trigram, words_in)
    print(hot_off_the_press)
else:
    print("please supply the name of a valid base file to use")
    sys.exit(1)