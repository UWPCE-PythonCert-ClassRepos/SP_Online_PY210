#!/usr/bin/env python3
import sys
import os
import random
import string


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i+2]
        trigrams.setdefault(pair,[]).append(follower)
    return trigrams

def in_data(in_file):
    #open file and return words
    mywords = " "
    with open(in_file, "r") as in_doc:
        for line in in_doc.readlines():
            for word in line.split():
                mywords += " " + word
                # remove special chars
                mywords = mywords.translate({ord(i):None for i in '-.:!@#$%^&*()_+-=,./<>?"'})
    return mywords.lower().split()


def generate_new_text(dict_of_trigrams):
    new_text = []
    # pick a workd pair as starting point
    start_pair = random.choice(list(dict_of_trigrams.keys()))
    # append to the list
    new_text = (list(start_pair))
    # lookup random next word using the pair
    new_value = random.choice(dict_of_trigrams[start_pair])
    new_text.append(new_value)
    for x in range(300):
        next_pair = tuple(new_text[-2:])
        if next_pair in dict_of_trigrams.keys():
            new_text.append(list(next_pair)[0])
            new_text.append(list(next_pair)[1])
            next_value = random.choice(dict_of_trigrams[next_pair])
            new_text.append(next_value)
        else:
            return " ".join(new_text)
    return " ".join(new_text)



if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    # check to see if file exists
    if os.path.isfile(filename):
        words = in_data(filename)
        trigrams = build_trigrams(words)
        new_story = generate_new_text(trigrams)
        print(new_story)
    else:
        print("You must pass in a valid filename")
        sys.exit(1)










