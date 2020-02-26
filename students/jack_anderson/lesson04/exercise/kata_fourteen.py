#!/usr/bin/env python3
"""
Jack Anderson
02/24/2020
UW PY210
Lesson 04
"""
import random
import sys



#words = "I wish I may I wish I might".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words) - 2):
        word_pairs = words[i:i + 2]
        value = words[i + 2]
        key = tuple(word_pairs)
        if key not in trigrams.keys():
            trigrams[key] = [value]
        else:
            trigrams[key].append(value)
    return trigrams

def read_in_data(filename):
    start_of_text = get_doc_start()
    end_of_text = get_doc_end()
    in_data = []
    with open(filename, "r") as f:
        for num,line in enumerate(f, 1):
            if num > start_of_text and num < end_of_text:
                in_data.append(line)
    f.close()
    return in_data


def get_doc_start():
    start = "*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
    with open(filename, "r") as f:
        for num, line in enumerate(f, 1):
            if start in line:
                x = num
                start_line = 1 + x
                f.close()
                return start_line
            else:
                return 1

def get_doc_end():
    end = "*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
    with open(filename, "r") as f:
        for num, line in enumerate(f, 1):
            if end in line:
                x = num
                end_line = x - 1
                f.close()
                return end_line
            else:
                return sum(num)




def make_words(in_data):
    new_words = []
    invalid_chars = ['.', ',', '(', ')', '/']
    for line in in_data:
        line = line.replace('--', ' ')
        for x in invalid_chars:
            line = line.replace(x, '')
        line = line.split()
        for item in line:
            if item == 'I' or item[0].isupper():
                new_words.append(item)
            else:
                new_words.append(item.lower())

        new_words.append(line)
    return (new_words)


def build_text(word_pairs):
    return

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("you muster pass in a filename")
        sys.exit(1)

    print(read_in_data(filename))


    # in_data = read_in_data(filename)
    # words = make_words(in_data)
    # word_pairs = build_trigrams(words)
    # new_text = build_text(word_pairs)
    #
    # print(new_text)