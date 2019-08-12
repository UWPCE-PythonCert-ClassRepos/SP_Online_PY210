'''
Andrew Garcia
Trigrams
7/27/19
'''

#!/usr/bin/env python3

import random
import string

def get_file():
    """ Gets a text file to convert """

    filename = input('What is the name of the file you would like to convert?: ')
    if filename[-4:] == '.txt':
        pass
    else:
        filename = filename + '.txt'

    with open(filename, 'r') as file:
        words = ''
        for line in file:
            line = line.translate(str.maketrans('', '', string.punctuation))
            words += line
    words_stripped = words.split()
    return words_stripped


def make_pairs(words):
    """ Makes pairs of words to build a trigram """

    word_pairs = {}

    for i in range(len(words)-2):
        # Makes a new pair
        pair = ' '.join(words[i:i + 2])
        follower = words[i + 2]

        # Adds a new item to a pair if it exists, creates new if it doesnt
        if pair not in word_pairs:
            word_pairs[pair] = [follower]
        elif pair in word_pairs:
            word_pairs[pair] += [follower]
    build_text(word_pairs)


def build_text(word_pairs):
    """ Uses pairs to build a new form of text """

    building_text = []

    # Gets a random pair to start off with
    pair_choice = random.choice(list(word_pairs))
    building_text += pair_choice.split()

    # Proceeds to get value of pair
    pair_follower = random.choice(list(word_pairs[pair_choice]))
    building_text.append(pair_follower)

    # Continues getting new pairs
    if len(building_text) < 100:
        new_pair = ' '.join(building_text[-2:])
        while True:
            if new_pair in word_pairs:
                building_text.append(random.choice(list(word_pairs[new_pair])))
                new_pair = ' '.join(building_text[-2:])
            else:
                break
    print(' '.join(building_text))


if __name__ == '__main__':
    make_pairs(get_file())






