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


###################################


# main, test funcs

if __name__ == "__main__":

    data = ""
    filename="Sherlock_small.txt"
    data = get_file_data(filename)
    data = filter_data(data)
