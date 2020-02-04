#!/usr/env python3
import urllib.request
import numpy as np
import re
import sys

sample_url = "https://uwpce-pythoncert.github.io/PythonCertDevel/_downloads/sherlock.txt"


def get_data_array_from_file(file_name: str):
    """parse a text url for a list of words.  Do not include special characters"""
    if file_name.startswith("http"):
        data = urllib.request.urlopen(sample_url).read().decode('utf-8')
    else:
        data = open(file_name, 'w').read()
    # remove quotations
    data = re.sub("\W'", " ", data)
    data = re.sub("'\W", " ", data)
    # remove line breaks
    data = re.sub("[\r\n]", " ", data)
    # return array split on white space(s)
    return np.array(re.split(pattern=r"\s+", string=data, flags=re.MULTILINE))


def build_trigrams(words_array: np.ndarray):
    """parse a strig for word pairs, building a trigram dictionary"""
    d_tri = {}
    for i in range(0, words_array.size - 2, 3):
        key = tuple(words_array[i:i + 2])
        value = d_tri.get(key, set())
        value.add(words_array[i + 2])
        d_tri.update({key: value})
    return d_tri


def build_new_text(d: dict, seed: tuple = ()):
    if not seed:
        seed = list(d.keys())[np.random.randint(len(d))]

    new_words = []
    new_words.extend(seed)
    while len(new_words) < np.random.randint(500,700):
        if d.get(tuple(new_words[-2:])):
            lst = d.get(tuple(new_words[-2:]))
            new = [np.random.choice(list(lst))]
        else:
            new = list(d.keys())[np.random.randint(len(d))]
        new_words.extend(new)

    new_str = " ".join(new_words)
    return "\n".join([line for line in re.findall(r".{1,60}(?:\s)", new_str)])


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    data_array = get_data_array_from_file(file_name=filename)
    tri_dict = build_trigrams(words_array=data_array)
    new_text = build_new_text(tri_dict)

    print(new_text)
