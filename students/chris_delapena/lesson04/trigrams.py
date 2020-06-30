#!/usr/bin/env python3

#Chris Dela Pena
#UW PCE PY210
#Assignment 4 - Trigrams
#2020/6/28

"""
implementing a trigram algorithm that generates a couple
of hundred words of text using a book-sized file as input
"""
import sys
import random

def read_in_data(filename):
    with open(filename, 'r') as file:
        for line in file:
            #Remove non-letters
            line = line.strip()
            line = line.replace('--', '')
            line = line.replace('"', '')
            line = line.replace(',', '')
            line = line.replace('(', '')
            line = line.replace(')', '')
            text_line = file.read()
    return text_line

def make_words(in_data):
#split lines into separate words
    words_list = in_data.split()
    return words_list

def build_trigram(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        #Check if pair is in the trigrams dictionary
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    return trigrams

def build_text(word_pairs):
    line = []
    # returns a number between a and b (including a and b)
    line_length = random.randint(4, 1000)

    # pick a random item from a sequence
    first_words = random.choice(list(word_pairs.keys()))
    for i in first_words:
        line.append(i)
    while len(line) < line_length:
        next_words = tuple(line[-2:])
        if next_words in word_pairs:
            line.append(random.choice(word_pairs[next_words]))
        else:
            next_words = random.choice(list(word_pairs))
            line.append(random.choice(word_pairs[next_words]))
    text = " ".join(line)
    return text



if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = 'sherlock.txt'
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)
