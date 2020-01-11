#!/usr/bin/env python3
import sys
import random
from collections import defaultdict


def read_in_data(filename):
    """
    read in filename
    :param filename: name of .txt file
    :return: string of filename input
    """
    with open(filename, 'r') as f:
        translation_dict = {9: ' ', 10: ' ', 13: ' ', 33: None, 40: None, 41: None, 44: None, 45: None, 46: None,
                            59: None}
        text = f.read().translate(translation_dict)
        return text


def make_words(text):
    """
    creates a list of all words in text
    :param text: string of input
    :return: list of words in text
    """
    words = text.split()
    return words


def build_trigram(words):
    """
    build trigram out of words
    :param words: list of words
    :return: defaultdict using tuple of word pairs as key and dict as values
    """
    trigrams = defaultdict(list)
    for i in range(len(words) - 2):
        trigrams[tuple(words[i:i + 2])].append(words[i + 2])
    return trigrams


def build_text(trigrams={}):
    """
    reconstruct the text in filename as a kata
    :param trigrams: dict of words consisting of a tuple and list
    :return: kata string of words_dict
    """
    kata = []
    kata.extend(random.choice(list(trigrams)))
    for i in range(50):
        kata.append(random.choice(trigrams.get(tuple(kata[-2:]))))
    kata = " ".join(kata)
    return kata


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)
    print(new_text)
else:
    print("Running %s as imported module", __file__)
