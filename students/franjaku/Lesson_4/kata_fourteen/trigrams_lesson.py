#!/usr/bin/env python3
import random
import string

"""
NEED TO CHANGE DICTIONARY KEYS TO BE ('Word1', 'Word2') NOT 'Word1 Word2'
"""


def cleanup_text(file):
    with open(file, 'r') as f:
        data = f.read()
    f.closed

    initial = string.punctuation + string.whitespace
    final = 6*" " + "'" + (32-7)*" " + len(string.whitespace)*' '
    translation_table = data.maketrans(initial, final)
    data = data.translate(translation_table)
    #data = data.split(" ")

    return data


def build_trigrams(inputtext):
    """
    Build a trigram dictionary from a list of words.

    return a dict
        keys: word pairs
        values: list of words that follow
    """
    trigrams = {}

    for idx in range(len(inputtext)-2):
        key = (inputtext[idx], inputtext[idx+1])
        if key in trigrams:
            trigrams[key].append(inputtext[idx+2])
        else:
            trigrams.setdefault(key, [inputtext[idx+2]])

    return trigrams


def make_new_line(trigram_dict, line):
    """
    Build a new line based on a trigram dictionary.
    trigram dict
        key
        value

    line
        List of 2 words that represent a key in in the trigram_dict

    Returns a list of words that has
    + 3 to 25 words inclusive

    """
    sentence_len = range(3,25)
    while len(line) < 26:
        key = (line[-2], line[-1])

        if key in trigram_dict:
            values = trigram_dict.get(key)  # get values from key
            word = random.choice(values)  # pick a value
            line.append(word)  # append the values
        else:
            break

        if len(line) == random.choice(sentence_len):
            break

    return line


def make_new_paragraph(trigram_dict):
    """
    Build a new block of text by stringing lines together.

    Return a list of lists?
    # What defines the end of file? aomount of lines/words/characters?
    """
    paragraph = []
    line = make_new_line(trigram_dict,['I', 'wish'])
    paragraph.append(" ".join(line) + '.')
    while len(paragraph) < random.choice(range(5,15)):
        line = make_new_line(trigram_dict,['I', 'wish'])
        paragraph.append(" ".join(line) + '.')

    return paragraph


if __name__ == "__main__":
    # 1. Open file
    # 2. Parse text and translate into input string
    # 3. Build trigram dictionary with input string
    # 4. Create new text with trigram dictionary
    data = cleanup_text('sherlock_small.txt')
    print(data)
    #dummy_input = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']
    #trigram_dict = build_trigrams(dummy_input)
    #paragraph = make_new_paragraph(trigram_dict)
    #print(" ".join(paragraph))
