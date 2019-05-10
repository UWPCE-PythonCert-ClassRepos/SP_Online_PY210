#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string, random

txt_file = "./great_expectations.txt"
dont_end_with = ['the', 'was', 'to', 'and', 'for', 'a', 'in', 'on', 'of', 'at', 'with', 'i', 'as', 'but', 'if', 'what', 'which']
punctuation = string.punctuation + "\n" + '”' + '“'


def translate_string(input_string):
    # Use string translation to remove all punctuation and newlines
    return ' '.join(input_string.translate(str.maketrans('', '', punctuation)).split())


def add_line_to_trigram(input_string):
    for i in range(len(input_string) - 2):
        trigram.update({(input_string[i], input_string[i + 1]): [input_string[i + 2]]})


def populate_dict(txt_file):
    # Poulate the dictionary from txt after passing to the translate function that remove punctuation and newlines
    f = open(txt_file)
    for line in f:
        line = translate_string(line)
        # Add to the dictionary that we'll use to generate the output
        add_line_to_trigram(line.split(' '))


def get_words(tg, first="", second=""):
    # Core algorithm to generate trigrams.
    if first == "" and second == "":
        words = list(tg.keys())
        rand = random.randint(1, len(trigram))
        first = words[rand][0]
        second = words[rand][1]
        third = tg.get((first, second)) # returns list
        third = ''.join(third[random.randint(0, len(third) - 1)]) # randomly select item from list, return string.
    else:
        third = tg.get((first, second))
        if third is not None:
            third = ''.join(third[random.randint(0, len(third)-1)])
        else:
            # At the end of a sentence an empty list gets returned. Return an emtpty string.
            third = ""
    return first, second, third


def get_wordsalad(tg, exclude_last):
    i = 0
    first = ''
    second = ''
    third = ''
    wordsalad = []

    for i in range(1, random.randint(12, 17)):
        first, second, third = get_words(trigram, second, third)
        if i == 1:
            wordsalad.append("{} {} {}".format(first.title(), second, third))
        else:
            if third != "":
                wordsalad.append(" {}".format(third))

    while True:
        if wordsalad[len(wordsalad)-1].lower().strip(' ') in exclude_last:
            # Don't with common prepositions or articles.
            wordsalad.pop(len(wordsalad)-1)
        else:
            break


    return ' '.join(wordsalad).replace('  ', ' ') # Remove any extra whitespace with replace


# Here's our datastructure that we'll use to generate the output
trigram = {}
# Pull the text into a dict
populate_dict(txt_file)

for i in range(0, random.randint(9, 12)):
    print(get_wordsalad(trigram, dont_end_with) + ".  ")



