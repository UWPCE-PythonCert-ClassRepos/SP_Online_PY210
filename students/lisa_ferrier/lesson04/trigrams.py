#!/usr/bin/env python3
# trigrams.py
# Lisa Ferrier, Python 210, Lesson 04

# import sys
import random


def read_file(filename):
    '''
    Read file contents, store in text variable.
    '''
    with open(filename, 'r') as f:
        text = f.read()
        return text


def clean_file_text(text):
    '''
    Clean text for processing:
    1. Replace non-alpha characters with whitespace
    2. Join characters together as lowercase
    3. Strip and split whitespace from text to get a list of words.
    '''
    for c in text:
        # print(c)
        if c.isalpha() is False:
            text = text.replace(c, ' ')
        else:
            continue
    text = "".join(text).lower()
    text = text.strip().split()
    return text


def build_trigram_dict(text):
    '''
    Build a trigram dictionary of the file text.
    '''
    trigram_dict = {}
    for i in range(len(text) - 2):
        pair = tuple(text[i:i + 2])
        follower = text[i + 2]
        if pair not in trigram_dict.keys():
            entry = {pair: []}
            trigram_dict.update(entry)
        trigram_dict[pair].append(follower)
    return trigram_dict


def build_trigram(trigram_dict, story_length=200):
    '''
    References the trigram_dict and generates a new story by reusing the key:value pairs in a random order.
    '''
    new_story = []
    dict_length = len(trigram_dict)
    for num in range(story_length):
        random_key = random.randint(0, dict_length)
        key = list(trigram_dict.keys())[random_key]
        new_story.append(' '.join(list(key)))
        new_story.append(' '.join(trigram_dict[key]))
    return ' '.join(new_story)


if __name__ == '__main__':
    # I can't get the try/except block to work, not sure what I'm missing, so it's commented out.

    '''
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    '''

    text = read_file('sherlock.txt')
    words = clean_file_text(text)
    word_pairs = build_trigram_dict(words)
    new_story = build_trigram(word_pairs)

    print(new_story)
