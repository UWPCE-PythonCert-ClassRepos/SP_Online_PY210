#!/usr/bin/env python3
import random
import sys

'''
Trigrams program takes command line arguments for a text file to parse
along with an int.  The program will open up the text file, and then
parse along the file to create a trigram of the words.  The int argument
is used to build up a new text, with wordcount equal to the provided int.
'''


def build_trigrams(words):
    '''
    build up the trigrams dict from the list of words

    returns a dict with:
        keys: word pairs in tuple format
        values: list of words that follow key pair
    '''
    trigrams = {}

    for i in range(len(words) - 2):
        trigrams.setdefault((words[i], words[i + 1]), []).append(words[i + 2])

    return trigrams


def read_file(file_name):
    text = ""
    with open(file_name) as f:
        text = f.read().replace('\n', ' ')
    return text


def build_text(trigram, text_length):

    def random_key():
        # get a random key from the dictionary
        return random.choice(list(trigram.keys()))

    text = list(random_key())
    for i in range(text_length - 2):
        next_key = (text[i], text[i + 1])
        # use dictionary to find next word list, but if key doesn't exist then
        # pick a random word list
        next_word_list = trigram.setdefault(next_key, trigram[random_key()])
        text.append(random.choice(next_word_list))
    return " ".join(text)


if __name__ == "__main__":
    # get the filename from the command line
    try:
        file_name = sys.argv[1]
        length = sys.argv[2]
    except IndexError:
        print("You must pass in a filename argument in the form of "
              "'filename.txt' along with an int argument for the number of "
              "pages you'd like the created text to be. "
              "ex: trigrams.py text.txt 100")
        sys.exit(1)
    words = read_file(file_name)
    trigrams = build_trigrams(words.split())
    text = build_text(trigrams, int(length))
    print(text)
    # for k, v in trigrams.items():
    #     print(k, v)
