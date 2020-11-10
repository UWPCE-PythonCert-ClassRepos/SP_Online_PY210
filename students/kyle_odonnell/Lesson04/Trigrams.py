# ------------------------------------------------------------------------ #
# Title: Trigrams.py
# Description: Trigrams assignment for Lesson04
# KODonnell,11.08.2020,created script
# KODonnell,11.09.2020,updated text generation
# ------------------------------------------------------------------------- #


#!/usr/bin/env python3

import random
import sys


# Processing  ------------------------------------------------------------- #
def read_file(file):
    """ Read text from file
    :param file: (string) with name of file:
    :return: string
    """
    file_text = ""
    while True:
        try:
            with open(file) as a_file:
                for line in a_file:
                    file_text += line
            break
        except FileNotFoundError:
            file = input("{} not found. Please enter the name of an existing file: ".format(file_name))
    return file_text


def build_trigram(words):
    """ Generate trigrams from string
    :param words: (string) of original text:
    :return: dict
    """
    corpus = words.split()  # map to list of words
    word_list = []
    for w in corpus:  # remove punctuation at word boundaries
        t = w.strip("*:“”;()- ?!'\"").lower()
        word_list.append(t)
    trigram = {}
    for i in range(len(word_list)-2):  # create word pair tuples
        pair = (word_list[i], word_list[i+1])
        try:
            trigram[pair].append(word_list[i+2])  # add "follower" words to existing key values
        except KeyError:
            trigram.update({pair: [word_list[i+2]]})  # add new dict entry for new word pairs
    return trigram


def generate_text(trigrams, size=40):
    """Generate new text based on trigrams
    :param trigrams: (dictionary) of word pairings and following words:
    :param size: (integer) of desired word length for new text
    :return: string
    """
    text_list = []
    random_key = random.choice(list(trigrams.keys()))  # start new text list with random dict key
    for i in random_key:
        text_list.append(i)
    random_value = random.choice(trigrams[random_key])  # pull random "follower" word based on key
    text_list.append(random_value)
    for num in range(int(size)):
        key = text_list[-2], text_list[-1]  # call dict keys based on most recently added words in list
        while True:
            try:
                new_word = random.choice(trigrams[key])
                text_list.append(new_word)
                break
            except KeyError:
                key = text_list[-4], text_list[-3]  # look further back if last two words not in dict keys
    new_string = " ".join(text_list) + "."  # create new string based on list
    formatted_string = ""
    for i, x in enumerate(new_string):
        if i == 0:  # capitalize first word of text
            formatted_string += x.capitalize()
        elif i > 1 and new_string[i-2] == ".":  # capitalize letters after periods
            formatted_string += x.capitalize()
        elif new_string[i-1:i+2] == " i ":   # capitalize pronoun "I"
            formatted_string += x.capitalize()
        else:
            formatted_string += x
    return formatted_string


# Main Body of Script  ---------------------------------------------------- #

if __name__ == "__main__":
    # get the filename from the command line
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = input("Please enter a file name:\n")
    # get desired length of generated text
    try:
        text_length = int(input("How many words would you like to generate?\n"))
    except TypeError:
        text_length = int(input("Please enter the number of words you would like as an integer:\n"))
    # process data
    in_data = read_file(file_name)
    word_pairs = build_trigram(in_data)
    new_text = generate_text(word_pairs, text_length-3)
    # output new text
    print("***** Here is your excerpt *****")
    print(new_text)