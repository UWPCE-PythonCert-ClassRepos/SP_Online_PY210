#!/usr/bin/env python3
import sys
import random



def make_list_of_words(line):
    replace_reference = {ord('-'): ' ', ord(','): '', ord(','): '', ord('.'): '', ord(')'): '',  ord('('): '', ord ('"'): ''}
    line = line.translate(replace_reference)
    words = line.split()
    return words

def read_file (file_name):
    big_line = []
    with open(file_name, 'r') as f:
        for line in f:
            big_line.append(line)
    return big_line


def build_trigrams(words):
    word_pairs = dict()
    for i in range(len(words) - 2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if pair not in word_pairs:
            word_pairs[pair] = [follower]
        else:
            word_pairs[pair].append(follower)
    return word_pairs


def new_text(trigrams_dic):
    a_list = []
    l = len(trigrams_dic.keys())
    for i in range(10):
        random_number = random.randint(0,l)
        key = list(trigrams_dic.keys())[random_number]
        a_list.append(" ".join(list(key)))
        a_list.append(" ".join(trigrams_dic[key]))


    return (" ".join(a_list))




if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    file_content = read_file (filename)
    list_of_words = make_list_of_words(" ".join(file_content))
    # list_of_words = make_list_of_words(" ".join(read_file('sherlock_small.txt.py')))

    trigrams = build_trigrams(list_of_words)

    print(new_text(trigrams))


