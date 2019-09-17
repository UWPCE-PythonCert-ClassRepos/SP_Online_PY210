#!/usr/bin/env python
import random, sys, string

words = '''Testing 1 2 3 1 3 Testing 2 4 5 Testing 3 Testing 1 4 1 2 2 4 5'''.split()

def build_trigrams(words):
    '''Build trigrams data structure using word list input
    
    returns a dict with:
        keys: word pairs
        values: list of following word(s)
    '''

    trigrams = {}

    for i in range(len(words) - 2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        key = tuple(pair)
        if key not in trigrams.keys():
            trigrams[key] = [follower]
        else:
            trigrams[key].append(follower)

    return trigrams


def build_text(trigram_dict):
    key = random.choice(list(trigram_dict.keys()))
    new_word_list = list(key)
    new_word_list[0] = new_word_list[0].capitalize()
    try:
        for i in range(100):
            next_follower = trigram_dict[key][random.randint(0,(len(trigram_dict[key]) - 1))]
            new_word_list.append(next_follower)
            key = tuple(new_word_list[-2:])
    except KeyError:
        print('\nLast key not in dictionary of trigrams. Process aborted.\n')
    finally:
        new_text = " ".join(new_word_list) + '.'
        return new_text



if __name__ == '__main__':
    
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams)

    print(new_text)
    
        

