#!/usr/bin/env python3

import random
import string
import sys

test_words = 'I wish I may I wish I might'.split()
longer_test_words = 'I would like to go to the store to get groceries for the week. I would also like to go to the park to play fetch with my dog.'.split()

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
        keys: word pairs
        values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        pair_key = (pair[0], pair[1])
        if pair_key in trigrams:
            trigrams[pair_key].append(follower)
        else:
            trigrams[pair_key] = [follower]
    return trigrams


def build_text(word_dict):
    start_key = random.choice(list(word_dict.keys()))
    text = [start_key[0], start_key[1]]
    text.append(word_dict[start_key][random.randint(0, len(word_dict[start_key])-1)])
    for i in range(300):
        key = (text[i+ 1], text[i + 2])
        if key not in word_dict:
            break
        else:
            text.append(word_dict[key][random.randint(0, len(word_dict[key])-1)])
        i += 1
    return ('...' + " ".join(text) + '...')

def make_words(text):
    clean_text = ""
    with open(text, 'r') as f:
        for line in f:
            if '*** START OF THIS PROJECT GUTENBERG EBOOK' in line:
                for line in f:
                    if 'End of the Project Gutenberg EBook' in line:
                        break
                    else:
                        clean_text = clean_text + line
    return clean_text.split()

if __name__ == "__main__":
    #get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)


    words = make_words(filename)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)
