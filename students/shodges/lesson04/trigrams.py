#!/usr/bin/env python3

import random
from pathlib import Path
from sys import argv

def build_trigrams(words):
    trigrams = {}
    for k, w in enumerate(words):
        if k + 2 < len(words):
            if not (w, words[k+1]) in trigrams.keys():
                trigrams[(w, words[k+1])] = []
            trigrams[(w, words[k+1])].append(words[k+2])
    return trigrams

if __name__ == '__main__':
    if not len(argv) == 2:
        print("Syntax: {} [filename]".format(argv[0]))
        quit()
    textfile = Path(argv[1])
    try:
        with textfile.open() as fileio:
            words = fileio.read().split()
    except FileNotFoundError:
        print("Unable to read {}".format(argv[1]))
        quit()
    trigrams = build_trigrams(words)

    literature = "It is"

    for i in range(0,210):
        try:
            next = trigrams[tuple(literature.split()[-2:])]
            literature = ' '.join((literature, random.choice(next)))
        except KeyError:
            literature += '.'
            break
    print(literature)
