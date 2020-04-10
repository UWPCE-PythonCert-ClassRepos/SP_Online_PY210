#!/usr/bin/env python3

import sys
import re

def read_file():
    with open('ion.txt', 'r') as book_file:
        book_text = book_file.read()
        book_file.close()
    words = re.split(r'\W+', book_text.lower())
    print(words)

def build_trigrams(words):
    trigrams = {}
    for item in range(len(words) - 2):
        pair = (words[item], words[item + 1])
        follower = words[item + 2]
        if pair not in trigrams:
            trigrams[(pair)] = [follower]
    print(trigrams)

    for item in trigrams.items():
        print(item)
    #return trigrams

# Exits the program
def exit_program():
    print('\nThank you for visiting.')
    sys.exit()

if __name__ == "__main__":
    #build_trigrams(words)'
    read_file()