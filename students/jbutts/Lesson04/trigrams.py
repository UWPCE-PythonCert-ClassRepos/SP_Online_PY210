#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import random

'''
James Butts
Python-210 -- Trigrams

'''

TXT_FILE = "./great_expectations.txt"
#  Skip ending with words that don't naturally end most English sentences
DONT_END_WITH = ['the', 'was', 'to', 'and', 'for', 'a', 'in', 'on', 'of',
                 'at', 'with', 'i', 'as', 'but', 'if', 'what', 'which']
PUNCTUATION = string.punctuation + "\n" + '”' + '“'


def populate_dict(txt_file):
    '''
    Populate the dictionary from txt after passing to the translate function
    that remove punctuation and newlines
    '''

    input_file = open(txt_file)
    for line in input_file:
        # Use string translation to remove all punctuation and newlines
        line = ' '.join(line.translate(str.maketrans('', '', PUNCTUATION)).split())
        word_list = line.split(' ')
        # Add to the dictionary that we'll use to generate the output
        for word in range(len(word_list) - 2):
            TRIGRAM.update({(word_list[word], word_list[word + 1]): [word_list[word + 2]]})


def get_words(trigram, first="", second=""):
    '''
    Core algorithm to generate trigrams
    '''

    if first == "" and second == "":
        words = list(trigram.keys())
        rand = random.randint(1, len(TRIGRAM))
        first = words[rand][0]
        second = words[rand][1]
        third = trigram.get((first, second)) # returns list
        third = ''.join(third[random.randint(0, len(third) - 1)])  # randomly select item from list,
        #  return string.
    else:
        third = trigram.get((first, second))
        if third is not None:
            third = ''.join(third[random.randint(0, len(third)-1)])
        else:
            # At the end of a sentence an empty list gets returned. Return an empty string.
            third = ""
    return first, second, third


def get_wordsalad(trigram, exclude_last):
    '''
    Pull it all together, construct the sentences.
    '''

    second = ''
    third = ''
    wordsalad = []  # List to contain our constructed trigram sentence.

    for word in range(1, random.randint(12, 17)):
        #  Create a sentence that's between 12-17 words long.
        first, second, third = get_words(trigram, second, third)
        if word == 1:
            #  for the beginning of a sentence, take the first three words
            wordsalad.append("{} {} {}".format(first.title(), second, third))
        else:
            if third != "":
                wordsalad.append(" {}".format(third))

    while True:
        if wordsalad[len(wordsalad)-1].lower().strip(' ') in exclude_last:
            # Don't end with common prepositions or articles.
            wordsalad.pop(len(wordsalad)-1)
        else:
            break
    return ' '.join(wordsalad).replace('  ', ' ')  # Remove any extra whitespace with replace


# Here's our data structure that we'll use to generate the output
TRIGRAM = {}
# Pull the text of the book/article into a dict
populate_dict(TXT_FILE)

for i in range(0, random.randint(9, 12)):
    #  Write 9-12 sentences of trigrams
    print(get_wordsalad(TRIGRAM, DONT_END_WITH) + ".  ")
