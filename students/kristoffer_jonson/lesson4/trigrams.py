#!/usr/bin/env python3

import random
import sys

#words = "I wish I may I wish I might I wish kris".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
for i in range(len(words)-2): # why -2 ?
   pair = words[i:i + 2]
    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    trigrams = {}
    for i in range(len(words)-2): # why -2 ?
        pair = words[i:i + 2]
        pair = tuple(pair)
        follower = words[i + 2]
        trigrams.setdefault(pair,[follower])
        if trigrams[pair] != [follower]:
            trigrams[pair].append(follower)
    # build up the dict here!

    return trigrams

def read_in_data(filename):
    with open(filename, 'r') as f:
        read_data = f.read()
    f.closed
    return read_data

def make_words(in_data):

    text_start = '*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***'
    text_end = 'End of the Project Gutenberg EBook of The Adventures of Sherlock Holmes'
    start_index = in_data.index(text_start)
    in_data = in_data[start_index + len(text_start):]

    end_index = in_data.find(text_end)
    in_data = in_data[:end_index]

    in_data = in_data.split()
    return in_data

def build_text(word_pairs):
    # returns a number between a and b (including a and b)
    #ord_pair_length = len(word_pairs)
    #random.randint(0, word_pair_length-1)
    # pick a random item from a sequence
    word_pairs_keys = list(word_pairs.keys())
    initial_words = random.choice(word_pairs_keys)
    story = list(initial_words)
    for i in range(100):
        first_word = initial_words[0]
        second_word = initial_words[1]
        if initial_words not in word_pairs:
            initial_words = random.choice(word_pairs[initial_words])
            story[-1] = story[-1] + '.'
        third_word = random.choice(word_pairs[initial_words])
        story.append(third_word)
        initial_words = (second_word,third_word)
    story = " ".join(story)
    return story



if __name__ == "__main__":

    # get the filename from the command line
    prompt = "\n".join(("","Please type a file name",
          ">>> "))
    filename = input(prompt)


    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)

