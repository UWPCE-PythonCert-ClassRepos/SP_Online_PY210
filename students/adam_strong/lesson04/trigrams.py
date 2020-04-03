#!/usr/bin/env python3
# Trigrams - Assingment 3
import random
import os
import pathlib
import sys

story_length = 200

def get_file():
    source = pathlib.Path.home() / filename
    with open(str(source), 'r') as infile:
        words = infile.read()
    return words

def clean_words(words):
    ''' The text changes slightly between E-Books so I am just using the raw file
    and not parsing out the START and end, this was the code which works for 
    Sherlock.txt but not other things:

    #start_mark = "START OF THE PROJECT GUTENBERG EBOOK"
    #end_mark = "END OF THE PROJECT GUTENBERG EBOOK"
    #words = words.split(start_mark)
    #words = str(words[1])
    #words = words.split(end_mark)
    #words = str(words[0])
    #table = str.maketrans(dict.fromkeys('"!.,'))
    #words = words.translate(table)
    '''
    
    words = words.replace("'","")
    words = words.replace('"',"")
    words = words.split()
    return words

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words
    
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    for i in range(len(words)-2): # why -2 ?
        pair = words[i:i + 2]
        follower = words[i + 2]
        tuppair = tuple(pair)
        if trigrams.get(tuppair) == None:
            trigrams[tuppair] = [follower]
        else:
            trigrams.get(tuppair).append(follower)
    return trigrams


def rand_story(trigrams):
    ''' Assembles a story from the trigrams, 
    adjust story length using:
     story_length var, 100 words are the default
     '''
    starter = random.choice(list(trigrams))
    print("Seed words ---> ", starter)
    nov = list(starter)
    for x in range(0,story_length):
        try:
            nxt = trigrams[(nov[len(nov)-2]),(nov[len(nov)-1])]
        except:
            break
        nov.append(random.choice(nxt))
    nov[0] = nov[0].capitalize()
    output = " ".join(nov) + "."
    return output


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    words = get_file()
    words = clean_words(words)
    trigrams = build_trigrams(words)
    output = rand_story(trigrams)
    print(output)
