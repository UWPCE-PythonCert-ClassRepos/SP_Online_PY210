#!/usr/bin/env python3

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
    print(list_of_words[-1])
    print(list_of_words[-2])
    for k in range(len(my_dict.items())-2):
        ans_opt = len(my_dict[(list_of_words[-2], list_of_words[-1])])
        ran_num = random.randint(0, ans_opt)
        print(ran_num)
        list_of_words.append(my_dict[(list_of_words[-2], list_of_words[-1])][random.randint(0, ans_opt-1)])
        print(f"{list_of_words} / {k}")





        '''
        if k == 0:
            if len(my_dict[(starter)]) > 1:
                
            else:
                ran_num = 0
            list_of_words.append(my_dict[starter][ran_num])
            
        else:
            pair = (list_of_words[len(list_of_words)-1], list_of_words[len(list_of_words)])
            print(pair)
            if pair not in my_dict.keys():
                if len(my_dict[pair]) > 1:
                    ran_num = random.randint(0, len(my_dict[pair]))
                else:
                    ran_num = 0
            list_of_words.append(my_dict[pair][ran_num])
            print(f"{list_of_words} / {k}")
        '''

    return list_of_words


#Main Exicutable
if __name__ == '__main__':
    trigrams = build_trigrams(words)
    print(trigrams)
    print(write_text(trigrams))