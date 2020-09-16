#!/usr/bin/env python3

import os
import pathlib
import sys
import random
import io
import string

#Trial Words
#words = "I wish I may I wish I might".split()
#words = "It was the best of times it was the worst of times".split()

def con_path():
    home = pathlib.Path.cwd()
    if os.path.split(home)[1] == 'IanMayther':
        home = pathlib.Path.cwd().joinpath('Lesson04')

    return home

def get_text(file_name):
    home = con_path()

    translator = str.maketrans('','', string.punctuation)

    with open(home.absolute()/file_name, 'r') as f:
        text = f.read()
    
    text = text.lower()
    text = text.replace('-',' ')
    text = text.translate(translator)

    return text.split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}

    for i in range(len(words)-2):
        temp_list = []
        pair = tuple(words[i:i+2])
        follower = words[i+2]
        temp_list.append(follower)
        if pair not in trigrams:
            trigrams[pair] = temp_list
        else:
            trigrams[pair].append(follower)

    return trigrams

def write_text(my_dict):    
    first, second = random.choice(list(my_dict.keys()))
    list_of_words = [first, second] 
    sen_len = random.randint(5,(len(my_dict.keys())-3))
    while len(list_of_words) < sen_len:
        new_start = tuple(list_of_words[-2:])
        if new_start in my_dict.keys():
            list_of_words.append(random.choice(list(my_dict[(list_of_words[-2], list_of_words[-1])])))
        else:
            list_of_words.append(random.choice(list(my_dict.values())))

        
    return " ".join(list_of_words).capitalize()


#Main Exicutable
if __name__ == '__main__':
    filename = input("What is the text you would like to input: ")
    #Please use 'sherlock_small.txt' 
    
    in_txt = get_text(filename)
    trigrams = build_trigrams(in_txt)
    print(write_text(trigrams))