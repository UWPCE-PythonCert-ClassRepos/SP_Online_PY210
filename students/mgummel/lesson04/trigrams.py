#!/usr/bin/env python3
import random
from pprint import pprint

HEADER = "*** START OF THIS PROJECT GUTENBERG EBOOK"
FOOTER = "End of the Project Gutenberg EBook"

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    # build up the dict here!
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if follower:
            trigrams.setdefault(pair, list())
            trigrams[pair].append(follower)
    return trigrams

def read_in_data(file_to_parse):
    word = list()
    line =""
    with open(file_to_parse, mode='r', encoding='utf-8') as a_file:
        while HEADER not in line:
            line = a_file.readline()

        while FOOTER not in line:
            line = a_file.readline()
            line = line.replace("\n", "")
            word += line.split(" ")
    return word

def clean_words(rogue_word_list):
    """
    Parses through the list of words and "cleans" all punctuation

    returns the same list void of many common punctiations.
    """

    translate_map = {ord('\n'): None, ord("\""): None, ord(';'): None,
            ord(','): None, ord('!'): None, ord('?'): None, ord('.'): None}       
    index = len(rogue_word_list) - 1

    while index >= 0:
        rogue_word_list[index] = rogue_word_list[index].translate(translate_map)
        rogue_word_list[index] = rogue_word_list[index].replace('.', '')
        rogue_word_list[index] = rogue_word_list[index].rstrip("\'")
        rogue_word_list[index] = rogue_word_list[index].rstrip(":")
        rogue_word_list[index] = rogue_word_list[index].lstrip("\'")

        index -= 1
    
    return rogue_word_list

def build_text(word_pairs):
    word_list = list()
    random_key = tuple()

    while len(word_list) < 300:
        if random_key not in word_pairs:
            if len(word_list) > 0:
                word_list[-1] += "."
            random_key = list(word_pairs)[random.randint(0, len(word_pairs))]
            word_list.append(random_key[0].title())
            word_list.append(random_key[1])

        third_word = random.choice(word_pairs[random_key])
        word_list.append(third_word)
        random_key = (word_list[-2], word_list[-1])

    word_list[-1] += "."
    return " ".join(word_list)

if __name__ == "__main__":
    in_data = read_in_data('sherlock.txt')
    clean_text = clean_words(in_data)
    word_pairs = build_trigrams(clean_text)
    new_text = build_text(word_pairs)
    print(new_text)