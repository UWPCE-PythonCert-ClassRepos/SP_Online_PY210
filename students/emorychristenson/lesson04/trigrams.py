#!/usr/bin/env python3

import sys
import random
import string

#test_words = "I wish I may I wish I might".split()

def read_in_data(file):
    # Read the text file 
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

def make_words(data):
    # Make words out of the text fle. 
    data = data.lower()
    for i in string.punctuation:
        if i not in ["'", "."]:
            data = data.replace(i, ' ')
    words = data.split()
    return words

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follows = words[i+2]
        if pair in trigrams:
            trigrams[pair].append(follows)
        else:
            trigrams[pair] = [follows]
    return trigrams


def build_text(trigrams):
    first_trigram = random.choice(list(trigrams.keys()))
    new_text = list(first_trigram)
    new_text.append(random.choice(trigrams[first_trigram]))
    for _ in range(100):
        new_pair = tuple(new_text[-2:])
        if new_pair in trigrams:
            new_text.append(random.choice(trigrams[new_pair]))

    sentences = " ".join(new_text)
    sentences = sentences.replace(' i ', ' I ')
    sentences = sentences.split('. ')
    capitalized_sentences = []
    for sentence in sentences:
        capitalized_sentences.append(sentence[0].upper() + sentence[1:])
    new_sentences = '. '.join(capitalized_sentences)
    sentences = new_sentences + '.'

    return sentences


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    data = read_in_data(filename)
    words = make_words(data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)
