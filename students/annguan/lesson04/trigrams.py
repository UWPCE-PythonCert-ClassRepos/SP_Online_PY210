#!/usr/bin/env python3

### Lesson 4 Kata Fourteen - Trigrams

import random
import sys

def open_book(book):
    """ open .txt file and extract the context"""
    text = []
    lines = f.readlines()

    with open(book,'r') as book:
        for i in range (65):
            book.readline()

    full_book = []

    for line in book:
        if line.startswith("End of the Project Gutenberg EBook"):
            break
        full_book.append(line)

    return " ".join(full_book)

def comp_trigrams(words):
    tripplet = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i+2])
        follows = words[i+2]
        if pair in tripplet:
            tripplet[pair].append(follows)
        else:
            tripplet[pair] = [follows]
    return tripplet

def extract_pairs(d):
    while True:
        pair = random.choice(list(d.keys()))
        if pair[0][0].isupper():
            return pair

def build_text(d):
    start = comp_trigrams(d)
    text_words = list(start)
    while len(text_words) < 500:
        pair = tuple(text_words[-2:])

        if pair in d:
            text_words.append(random.choice(d[pair]))
        else:
            text_words[-1] += "."
            alternate_pair = get_random_pair(d)
            text_words.extend(list(alternate_pair))

    new_text =  " ".join(text_words)
    return new_text

if __name__ == "__main__":
    try:
        book = sys.argv[1]
    except IndexError:
        print("book name required")
        sys.exit(1)

    in_book = open_book(book)
    in_words = comp_trigrams(in_book)
    new_text = build_text(in_words)

    print(new_text)
