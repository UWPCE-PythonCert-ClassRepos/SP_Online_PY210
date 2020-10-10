#!/usr/bin/env python3
# Title: Trigrams (Lesson 4)
# Dev: Roslyn Melookaran
# Date: 10/2/20
# Change Log: (Who, When, What)
# R. Melookaran, 10/7/20, created script)
# --------------------------------------------------------------
import random
import string
import sys


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words) - 2):  # why -2 ?
        pair = ()
        pair = words[i:i + 2]
        key = " "
        key = key.join(pair)
        follower = []
        follower.append(words[i + 2])
        follower = words[i + 2]
        if key in trigrams.keys():
            existing_value = trigrams[key]
            list(existing_value)
            existing_value.append(follower)
            trigrams[key] = existing_value
        else:
            trigrams.update({key: list(follower.split(" "))})
    return trigrams


def read_in_file(filename):
    """
    Reads in text from file, also scrubs puntuation and extra lines/spaces. Also scrubs the initial Gutenberg text (prior to "*** START OF...".

    returns text:
       filname: file name string
    """
    with open(filename, 'r') as file:
        lines = file.readlines()  # reads all the file lines into one list
        text = ""
        for item in lines:
            text += str(item)
            text = text.replace('\n', " ")
            for c in string.punctuation:
                text = text.replace(c, " ")
            text = text.replace("  ", " ")
        if "START OF THIS PROJECT GUTENBERG EBOOK POOR BLOSSOM" in text: # This starts the text after the "***START OF THIS PROJECT GUTENBERG EBOOK POOR BLOSSOM***" text
            index = text.index("START OF THIS PROJECT GUTENBERG EBOOK POOR BLOSSOM ")
            text = text[index + 51:]
            print(text)
        else:
            print("FYI, this is not a Gutenberg Book")
        print(text)
    return text


def build_new_text(tgram, start_words, max_words):
    """ Build up a string of text based on an input trigrams dict
        tgrams = trigrams dictionary
        start_words = word pair to start the sequence
        max_words = Max number of words in the string
        """
    out_words = []
    for i in range(max_words - 2):
        if start_words in tgram:
            next_word = random.choice(tgram[start_words])
            out_words.append(next_word)
            start_words = start_words.split()
            start_words = start_words[1] + " " + next_word
        else:
            break
    out_words = " ".join(out_words)
    return out_words


if __name__ == "__main__":

    option = 3
    if option == 1:
        print("This is a small test case:")
        test_text = "I wish I may I wish I might".split()
        print(test_text)
        trigrams = build_trigrams(test_text)
        print(trigrams)
    elif option == 2:
        print("This is another test, using the sherlock holmes text:")
        file = 'sherlock_small.txt'
        sherlock_string = read_in_file(file)
        sherlock_string = sherlock_string.split()
        trigrams = build_trigrams(sherlock_string)
        print("Here is the trigram dictionary: ")
        print(trigrams)
        print("Here is the new story: ")
        starting_words = "on the" # This is the starting key
        max_count = 50 # This is the max count of the new story
        new_text = build_new_text(trigrams, starting_words,max_count)
        print(new_text)
    elif option == 3:
        print("This is to practice using a Gutenberg Book: ")
        file = 'Gutenberg.txt'
        gut_string = read_in_file(file)
        gut_string = gut_string.split()
        trigrams = build_trigrams(gut_string)
        print("Here is the trigram dictionary: ")
        print(trigrams)
        print("Here is the new story: ")
        starting_words = "and the" # This is the starting key
        max_count = 50 # This is the max count of the new story
        new_text = build_new_text(trigrams, starting_words,max_count)
        print(new_text)

