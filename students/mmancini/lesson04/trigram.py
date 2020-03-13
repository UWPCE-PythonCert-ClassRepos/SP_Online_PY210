#!/usr/bin/env python3

import sys


###################################


def get_file_data(in_filename):
    out_data = ""

    with open(in_filename, 'r') as fil:
        out_data = fil.read()
    fil.close()
    out_data = out_data.lower()

    return out_data


def filter_data(in_data):
    # filter out punctuation
    out_data = in_data
    out_data = out_data.replace(',', '')
    out_data = out_data.replace('.', '')
    out_data = out_data.replace(')', '')
    out_data = out_data.replace('(', '')
    out_data = out_data.replace('--', ' ')

    return out_data


def make_words(in_data):
    lst_words = data.split()
    return lst_words

def build_triagram(in_lst_words):
    """
        des: create dictionary with key==word pair, value==next word
        in: list
        out: dict
    """
    triagram = {} #each pair will have a follower
    for i in range(len(in_lst_words) - 2):
        key = tuple(in_lst_words[i:i + 2])
        next_word = in_lst_words[i + 2]
        if key not in triagram.keys():
            triagram[key] = [next_word]
        else:
            # key already exists
            triagram[key].append(next_word)
    return triagram


###################################


# main, test funcs

if __name__ == "__main__":

    data = ""
    filename="Sherlock_small.txt"
    data = get_file_data(filename)
    data = filter_data(data)
    word_lst = make_words(data)
    # print(data)
    trigram = build_triagram(word_lst)
