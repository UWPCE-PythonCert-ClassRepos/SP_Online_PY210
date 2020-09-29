# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:00:11 2020

@author: Grant Dowell
Activity 3 - Trigrams
"""
import random
import string

def build_trigrams(words):
    """
    Build up the trigrams dict from an ordered input list of words

    Return the dict with keys of word-pair tuples and values of follower lists
    """
    trigrams = {}
    for n in range(len(words)-2):
        pair = (words[n], words[n+1])
        follower = words[n+2]
        trigrams.setdefault(pair, []).append(follower)

    return trigrams

def generate_txt(trigrams, start_words, max_words):
    """
    Build up a string of text based on an input trigrams dict

    start_words = word pair to start the sequence
    max_words = Max number of words in the string
    """
    key1 = start_words[0]
    key2 = start_words[1]
    out_words = [key1, key2]
    for _ in range(max_words-2):
        if (key1, key2) in trigrams:
            next_word = random.choice(trigrams[(key1, key2)])
            out_words.append(next_word)
            key1, key2 = key2, next_word
        else:
            break
    return out_words

def read_file(filename):
    """ Reads in a file and scrubs Gutenberg Header/Footer"""
    with open(filename, 'r') as file:
        text = file.readlines()
    text = [text[n].strip() for n, _ in enumerate(text)] #Del whitspace
    is_gutenberg = False
    for n, line in enumerate(text):
        if line.startswith('*** START OF THIS PROJECT GUTENBERG EBOOK'):
            header_end = n+6
            is_gutenberg = True
        elif line.startswith('*** END'):
            footer_start = n-3
    if is_gutenberg:
        text = text[header_end:footer_start]
    return ' '.join(text)

def make_word_list(text):
    """Scrubs punctuation and returns a list of words"""
    exclude = set(string.punctuation)
    exclude.remove("'") #Leave the apostrophe's in
    # Replace the excludes with whitespace that gets cleaned up by .split()
    for ch in exclude:
        text = text.replace(ch, ' ')
    text = text.split()
    return text

if __name__ == "__main__":

    user_option = 2

    # Simple test case
    if user_option == 1:
        test = "I wish I may I wish I might".split()

        tgrams = build_trigrams(test)
        print(tgrams)
        out_list = generate_txt(tgrams, ('I', 'wish'), 20)
        print(' '.join(out_list))

    # Sherlock_small.txt
    elif user_option == 2:
        txt = read_file('sherlock_small.txt')
        print("Here's the raw text:\n\n")
        print(txt+"\n\n")
        word_list = make_word_list(txt)
        print("Here's the word list:\n\n")
        print(word_list)
        tgrams = build_trigrams(word_list)
        print("Here's the trigrams:\n\n")
        print(tgrams)
        out_list = generate_txt(tgrams, ('and', 'was'), 50)
        print("Here's the output:\n\n")
        print(' '.join(out_list))
