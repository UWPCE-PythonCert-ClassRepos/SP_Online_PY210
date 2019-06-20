#!/usr/bin/env python3
import random
import string

"""
NEED TO CHANGE DICTIONARY KEYS TO BE ('Word1', 'Word2') NOT 'Word1 Word2'
"""


def cleanup_text(file):
    """
    Clean input text and make a list of words

    data_final: List of word originally seperated by whitespace.
    """
    with open(file, 'r') as f:
        data = f.read()
    f.closed

    data = data.lower()
    translation_dict = dict.fromkeys(string.punctuation, ' ')
    translation_dict.update(dict.fromkeys('\r\t\n', ' '))
    translation_table = data.maketrans(translation_dict)
    data = data.translate(translation_table)
    data = data.split(" ")
    data_final = [word for word in data if word is not '']
    return data_final


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
    # keylist = list(trigram_dict.keys())
    line = make_new_line(trigram_dict, ['one', 'night'])
    seed = [line[-2], line[-1]]
    paragraph.append(" ".join(line))

    while len(paragraph) < random.choice(range(5,15)):
        line = make_new_line(trigram_dict, seed)
        seed = [line[-2], line[-1]]
        paragraph.append(" ".join(line[2:]))

    return paragraph


if __name__ == "__main__":
    # 1. Open file
    # 2. Parse text and translate into input string
    # 3. Build trigram dictionary with input string
    # 4. Create new text with trigram dictionary
    data = cleanup_text('sherlock_small.txt')
    trigram_dict = build_trigrams(data)
    paragraph = make_new_paragraph(trigram_dict)
    book = ". ".join(paragraph)

    print(book)
    #dummy_input = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']
    #trigram_dict = build_trigrams(dummy_input)
    #paragraph = make_new_paragraph(trigram_dict)
    #print(" ".join(paragraph))
