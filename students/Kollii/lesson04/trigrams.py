#!/usr/bin/env python3

##### Trigrams #####

###  Trigrams – Simple Text Manipulation  ###

import random
import re
import sys


def read_in_data(file_name):
    file_lines = []
    with open(file_name, 'r') as f:
        for line in f:
            file_lines.append(line)
   # print(file_lines)
    return file_lines


def words(line):
    wordslist = []
    with open(filename,'r') as lines:
        for line in lines:
            line = re.sub('--',' ',line)
            line = line.strip('(')
            line = line.strip(')')
            for word in line.split():
                wordslist.append(word.lower())
    #print(wordslist)
    return wordslist




def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = dict()
    for x in range(len(words) - 2):
        pair = tuple(words[x:x + 2])
        follower = words[x + 2]
        if pair not in trigrams:
            trigrams[pair] = [follower]
        else:
            trigrams[pair].append(follower)
    #print(trigrams)
    return trigrams 


def output_text(trigrams_dic):
    list_x = []
    l = len(trigrams_dic.keys())
    for x in range(10):
        random_number = random.randint(0,l)
        key = list(trigrams_dic.keys())[random_number]
        list_x.append(" ".join(list(key)))
        list_x.append(" ".join(trigrams_dic[key]))


    return (" ".join(list_x))




if __name__ == "__main__":
     # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    #filename = 'C:\\Users\\ikolliv\\SP_Online_PY210\\students\\Kollii\\lesson04\\sherlock_small.txt'
    in_data= read_in_data(filename)
    word_pairs = words(" ".join(in_data))
    new_text = build_trigrams(word_pairs)

    print(output_text(new_text))


