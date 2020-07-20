#!/usr/bin/env python3

import random
import string

#words = "I wish I may I wish I might".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams


def build_text(word_pairs):
    # print(random.choice(word_pairs))
    word_choice = random.choice(list(word_pairs.keys()))
    list_words = []
    list_words.append(word_choice[0])
    list_words.append(word_choice[1])
    capitalize = True
    while word_choice in word_pairs and len(list_words) < 300:
        length_values = len(word_pairs.get(word_choice))
        new_word = word_pairs.get(word_choice)[
            random.randint(0, length_values - 1)]
        if capitalize:
            new_word.capitalize()
            capitalize = False
        list_words.append(new_word)
        word_choice = (word_choice[1], new_word)
        # if new_word has period
        if new_word[:-1] == ".":
            capitalize = True
    return " ".join(list_words)

def read_in_data(filename):
    words = []
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)
    return words

if __name__ == "__main__":
    #filename = sherlock.txt
    filename = input("Please type a filename: ")
    in_data = read_in_data(filename)
    word_pairs = build_trigrams(in_data)
    new_text = build_text(word_pairs)
    print(new_text)
