#!/usr/bin/env python3
import os
import pprint
import random
import string
import sys
from collections import defaultdict


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# words = "I wish I may I wish I might".split()
words = 'Mary had a little lamb little whose fleece was white as snow and everywhere that Mary went the lamb was sure to follow.'.split()


def open_file():
    print(os.path)
    with open(os.path.join(sys.path[0], 'Pride_Prejudicetest.txt'), 'r', encoding='utf8') as f:
        data = f.read()
        # print(data)

    intable = ',.“”"?!_&$;'
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
    # trigrams = {}

    trigrams = defaultdict(list)

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        trigrams[pair].append(follower)
        # print(f'pair      {pair}')
        # print(f'follower  {follower}')

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(d)

    key = ('It', 'is')
    key = random.choice(list(trigrams))
    new_text = []

    for i in range(1000):
        words = trigrams[key]
        word = words[0]
        new_text.append(word)
        # cls()
        # print(f'Current Text      : \n{" ".join(new_text)}')
        # print()
        # print(f'Current Key       : {key}')
        # print(f'Current Word List : {dd.get(key)}')
        # print(f'Current Word      : {word}')
        trigrams[key] = words[1:] + words[:1]
        key = (key[1], word)

    end_sentences(new_text)
    comma_chameleon(new_text)
    print(" ".join(new_text))


def end_sentences(new_text):
    paragraph_max_sentences = random.randrange(5, 10)
    sentence_min_words = random.randrange(4, 12)
    # TODO: Make the first pass generate list of proper nouns by
    # capturing all the capitalized words that are not at the 
    # beginning of a sentence.  Use that list here. 
    keep_upper = ['I', 'Mr', 'Mrs', 'Miss', 'Bennett', 'Sir', 'Lady', 'Lucas', 'William','Bingley']    
    sentence_counter = 0
    word_counter = 0
    # Find indexes of words that are capitalized
    # If it's been more than soft_limit words since
    # the last period, insert a period at the end
    # of the previous word.
    for index in range(len(new_text)):
        word = new_text[index]
        word_counter += 1
        if word[0].isupper():
            if word_counter > sentence_min_words:
                new_text[index-1] += '.'
                sentence_counter += 1
                word_counter = 0
                sentence_min_words = random.randrange(4, 12)
                if sentence_counter > paragraph_max_sentences:
                    new_text[index-1] += '\r\n\r\n'
                    sentence_counter = 0
                    paragraph_max_sentences = random.randrange(5, 9)
            else:
                # word is upper, but we will not begin new sentence here
                # make the word lower case, unless it's in keep_upper    
                if not keep_upper.__contains__(new_text[index]):
                    new_text[index] = new_text[index].lower()

def mr_mrs(new_text):
    # If the word is mr or mrs, capitalize it and put a dot.
    pass

def comma_chameleon(new_text):
    # smells_like_a_comma_before = ['if', 'was']
    comma_before = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'though', 
                    'although', 'while', 'if', 'unless', 'until', 'lest', 'than', 'whether', 
                    'whereas', 'after', 'before', 'once', 'since', 'till', 'until', 'when', 
                    'whenever', 'while', 'because', 'since', 'why', 'that', 'what', 'whatever', 
                    'which', 'whichever', 'who', 'whoever', 'whom', 'whomever', 'whose', 'how', 
                    'where', 'wherever']
    for index in range(len(new_text)):
        word = new_text[index]
        if comma_before.__contains__(word):
            new_text[index-1] += ','


if __name__ == "__main__":
    # build_trigrams(words)
    open_file()
