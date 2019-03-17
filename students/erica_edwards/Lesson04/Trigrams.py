#!/usr/bin/env python3
import os
import pprint
import random
import string
import sys
from collections import defaultdict

# words = "I wish I may I wish I might".split()
words = 'Mary had a little lamb little whose fleece was white as snow and everywhere that Mary went the lamb was sure to follow.'.split()

def open_file():
    print(os.path)
    with open(os.path.join(sys.path[0], 'Paragraphtest.txt'), 'r', encoding='utf8') as f:
        data = f.read()
        # print(data)

    intable  = ',.“”"?!_&$;'
    outtable = ' '*len(intable)
    transtable = str.maketrans(intable, outtable) 
    data = data.translate(transtable)
    
    words = data.split()
    print(words)

    build_trigrams(words)


def build_trigrams(words):
    '''Build up the trigrams dict from the list of words
       
       Returns a dict with:
        keys: word pairs
        values: List of followers
    '''
    trigrams = {}
    
    d = defaultdict(list)

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        d[pair].append(follower)
        # print(f'pair      {pair}')
        # print(f'follower  {follower}') 
        # if pair not in words:
        
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(d)
    build_story(trigrams)

def build_story(trigrams)
    new_book = []
    word1, word2 = 
    word3 = follower
    for i in range(100)
        new_book.append(word1)






if __name__ == "__main__":
    # build_trigrams(words)
    open_file()
