#!/usr/bin/env python3

import sys
import random
import string

#words = "I wish I may I wish I might".split()
words = "It was the best of times it was the worst of times".split()

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
    word_pair = random.randint(0, len(words)-1)
    first = words[word_pair]
    second = words[word_pair + 1]
    list_of_words = [first, second]    
    sen_start = tuple(list_of_words)
    sen_len = random.randint(5,20)
    #for k in range(15):
    while len(list_of_words) < sen_len:
        if sen_start in my_dict.keys():
            list_of_words.append(random.choice(list(my_dict[(list_of_words[-2], list_of_words[-1])])))
        else:
            list_of_words.append(random.choice(list(my_dict)))
        
    return " ".join(list_of_words).capitalize()


#Main Exicutable
if __name__ == '__main__':
    trigrams = build_trigrams(words)
    print(trigrams)
    print(write_text(trigrams))