# Isabella Kemp
# Trigrams assignment

import random
import re
import sys


def build_trigrams(words_list):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    # First create a blank dict
    trigrams = {}
    # Loop through the words in the list, using an index.
    for w in range(len(words_list) - 2):
        pair = tuple(words_list[w:w + 2])
        follower = words_list[w + 2]
        # check if the key is in the dictionary, then add it.
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
            # add new if the pair is not yet in trigram
    return trigrams

# Takes a string of text and returns a list of words


def make_words(line):
    words_list = []
    with open(filename, 'r') as lines:
        for line in lines:
            # remove dashes and replace with spaces
            line = line.replace('--', ' ')
            line = line.replace('"', '')
            line = line.replace(',', '')  # no commas
            # replace parenthases
            line = line.replace('(', '')
            line = line.replace(')', '')
            # removes leading and trailing spaces from string 
            line = line.strip()
            # splits the string into a list
            for word in line.split():
                # returns the lowercase string and adds it to our words list
                words_list.append(word.lower())
    # return words list 
    return words_list

# n is the word max. This builds a random string of words
def build_text(trigrams, n=100):
    list_w = []
    # Here we get a random word pair from the dict and add it to the list.
    # turning trigrams from dict into list
    random_word = random.choice(list(trigrams))
    for word in random_word:
        list_w.append(word)
    # while length of the list is less than or equal to the max, add new pair 
    while len(list_w) <= n:
        new_pair = tuple(list_w[-2:])
        if new_pair in trigrams:
            list_w.append(random.choice(trigrams[new_pair]))
        else:
            random_word = random.choice(list(trigrams))
            list_w.append(random.choice(trigrams[random_word]))
    new = " ".join(list_w)
    return new


def read_in(filename):
    # Reads in lines in the file and returns them in a list
    file_lines = list()
    with open(filename, 'r') as file:
        for line in file:
            file_lines = file.read()
    return file_lines


if __name__ == '__main__':
    try:
        filename = 'sherlock.txt'
    except IndexError:
        print("Pass in a filename")
        sys.exit(1)

    in_data = read_in(filename)
    words = make_words(" ".join(in_data))
    new_text = build_trigrams(words)
    print(build_text(new_text))
