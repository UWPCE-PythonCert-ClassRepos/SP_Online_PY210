#!/usr/bin/env python3
import sys
import os
import random
import string

def in_data(in_file):
    #open specified text file and format
    book_list = list()
    with open(in_file, "r") as book:
        for line in book:
            for word in line.split():
                word = word.lower()
                word = word.translate({ord(i): None for i in '.,:;"?!@#$%^&*()-'})
                book_list.append(word)
    return book_list

def build_trigrams(words):
    #use result from in_data function to build trigrams
    trigrams = {}
    for i in range(len(words)-2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        if tuple(pair) not in trigrams.keys():
            trigrams[tuple(pair)] = {follower}
        else:
            trigrams[tuple(pair)].add(follower)
    return trigrams

def random_three(word_pairs):
    #randomly select three words from build_trigrams function
    beginning = random.choice(list(word_pairs.keys()))
    next_word = random.choice(list(word_pairs[beginning]))
    rt = list(beginning)
    rt.append(next_word)
    return rt

def build_text(word_pairs):
    #write final text starting with three random words; remove quotes from list with 'join'
    final_text = random_three(word_pairs)
    for i in range(len(word_pairs.keys())):
        last_two = tuple(final_text[-2:])
        if last_two in word_pairs.keys():
            next_word = random.choice(tuple(word_pairs[last_two]))
            final_text.append(next_word)
        else:
            final_text.extend((random_three(word_pairs)))
    return " ".join(final_text)



if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    words = in_data(filename)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)

