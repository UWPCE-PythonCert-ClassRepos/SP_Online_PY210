#!/usr/bin/env python

import random
import sys

def read_in_data(in_filename):
    with open(in_filename) as infile:
        in_lines = infile.readlines()
    return in_lines

def make_words(in_lines):
    in_words = []
    for line in in_lines:
        #Remove headers and footers
        if line[0:3] == '***':
            in_lines.remove(line)
        #Remove punctuation
        else:
            new_line = line.translate(str.maketrans(
                    '''0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'''
                    ,'                                         ' ))
            #Break each line to wrods and feed into the word list
            for word in new_line.split():
                if word is not "I":
                    word = word.lower()
                in_words.append(word)
    return in_words

def build_trigrams(words):
    trigrams = {}
    for i in range(len(words)-2):
       pair = words[i:i + 2]
       follower = words[i + 2]
       trigrams.setdefault(tuple(pair),[]).append(follower)
    return trigrams

def build_text(trigrams):
    word_limit = int(input('Enter the desired number of words in the new text\
(minimum of 3)>'))
    #Pick the first random word pair from the dictionay
    first_pair = random.choice(list(trigrams))
    new_list = list(first_pair)
    new_list.append(random.choice(trigrams[first_pair]))
    #add a new word to the list using the last two words in the list as
    #word pairs
    count = 3
    while count < word_limit:
        if tuple(new_list[-2:]) in trigrams:
            new_list.append(random.choice(trigrams[tuple(new_list[-2:])]))
            count += 1
        elif count == word_limit-1:
            new_list.append(first_pair[0])
            count += 1
        elif count == word_limit-2:
            new_list.append(first_pair[0])
            new_list.append(first_pair[1])
            count += 2
        else:
            new_list.append(first_pair[0])
            new_list.append(first_pair[1])
            new_list.append(random.choice(trigrams[first_pair]))
            count += 3
    new_text = " ".join(new_list)
    return new_text    
   
if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_story = build_text(word_pairs)
    print(new_story)