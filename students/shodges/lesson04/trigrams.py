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

def gutenberg_clean(guten_text):
    guten_text = guten_text.split('*** START OF THIS PROJECT GUTENBERG EBOOK') # Get rid of the first part of the header
    guten_text = guten_text[1][(guten_text[1].find('***')+3):] # Prior to the next '***' there may be arbitrary text
    guten_text = guten_text.split('*** END OF THIS PROJECT GUTENBERG EBOOK') # Cut out the footer and T's & C's
    return guten_text[0]

def add_next_word(trigrams, wip):
    global in_quote
    next = trigrams[tuple(wip.split()[-2:])]
    next = random.choice(next)
    if next[0] == '"':
        in_quote = True
    if next[-1] == '"':
        in_quote = False
    return ' '.join((wip, next))

def literature_complete(literature):
    global in_quote, target_length
    if len(literature.split()) < target_length:
        return False # Keep going if we haven't hit the minimum word length
    if in_quote == True:
        return False # Always keep going if we have an ongoing quote
    if literature[-1] == '"':
        # Since we end with a quote, we need to find out whether we end with the proper punctuation inside that in_quote
        if literature[-2] == '.' or literature[-2] == '!' or literature[-2] == '?':
            return True
        else:
            return False
    if literature[-1] == '.' or literature[-1] == '!' or literature[-1] == '?':
        return True
    return False

if __name__ == '__main__':
    if len(argv) == 3:
        if argv[2].isnumeric():
            target_length = int(argv[2])
        else:
            print("Invalid target_length {}".format(argv[1]))
            quit()
    elif len(argv) == 2:
        target_length = 200
    else:
        print("Syntax: {} [filename] [OPTIONAL: target_length]".format(argv[0]))
        quit()
    textfile = Path(argv[1])
    try:
        with textfile.open() as fileio:
            words = gutenberg_clean(fileio.read()).split()
    except FileNotFoundError:
        print("Unable to read {}".format(argv[1]))
        quit()
    trigrams = build_trigrams(words)

    literature = "It is"
    in_quote = False # sentinel value to help us finish a quote

    while literature_complete(literature) == False:
        try:
            literature = add_next_word(trigrams, literature)
        except KeyError:
            literature += '...'
            break
    print(literature)
