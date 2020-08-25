#!/usr/bin/env python3
import random
import sys

'''
'''

# words = "I wish I may I wish I might".split()

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
        next_word_list = trigram.setdefault(next_key, trigram[random_key()])
        text.append(random.choice(next_word_list))
    return " ".join(text)

if __name__ == "__main__":
    # get the filename from the command line
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("You must pass in a filename in the form of 'filename.txt'")
        sys.exit(1)
    words = read_file(file_name)
    trigrams = build_trigrams(words.split())
    text = build_text(trigrams, 100)
    print(text)
    print(len(text))
    # for k, v in trigrams.items():
    #     print(k, v)
