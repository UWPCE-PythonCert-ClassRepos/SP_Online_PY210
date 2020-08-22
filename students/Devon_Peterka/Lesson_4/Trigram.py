#!/usr/bin/env python3

import os
import random
import string

def fix_filename(text_file):    # Handles improper filenames from user
    if text_file[-4:] != '.txt':    # specifically ones w/o ".txt"
        text_file += '.txt'
    return text_file

def word_library(filename):
    '''
    Builds just... a giant list of every word in the order in which
    they appear in the file - all lowercase.  Returns said list
    
    Does not extract the header information from the project
    Gutenberg files because this is not the only source of .txt files
    and I want to retain generality
    '''
    words = []
    with open(text_file, 'r') as source:
        for line in source:
            intable = string.punctuation
            outtable = ' ' * len(intable)
            trans_table = str.maketrans(intable, outtable)
            line = line.translate(trans_table)
            for i,word in enumerate(line.split()):
                if line.split()[i] == 'I':
                    words.append(line.split()[i])
                else:
                    words.append(line.split()[i].lower())
    source.close()
    return words

def trigram_build(text_file):
    '''
    Builds the trigrams dictionary using a list of all the words
    in the text file.
    '''
    word_list = word_library(text_file)
    trigram = {}
    for i in range(len(word_list)-2):
        pair = tuple(word_list[i:i+2])
        nextword = word_list[i+2]
        trigram.setdefault(pair, []).append(nextword)
    return trigram
    
def create_new(text_file):
    new_text = []
    trigram = trigram_build(text_file)
    length = int(input('How many trigrams shall we use?: '))
    first_words = random.choice(list(trigram.keys()))
    new_text += list(first_words)
    for i in range(2,length+1):
        key = new_text[i-2:i]
        if tuple(key) not in trigram:
            key = random.choice(list(trigram.keys()))
        new_text.append(random.choice(trigram[tuple(key)]))
    return " ".join(new_text)

if __name__ == '__main__':
    intro = True    # Turns on the intro message
    while True:    # allows for multiple trigrams to be run if desired
        if intro is True:    # Display intro message first time
            print('Welcome to Trigrams.\n',
                  'Please provide a text (.txt) file for us to read.\n',
                  '\n',
                  'If file is in the current directory, no path is\n',
                  'required (i.e. - file name alone will suffice).\n',
                  '\n',
                  'If file is in another directory, input absolute\n',
                  'filepath.\n',
                  '\n',
                  'If you wish to see this message again, type "help"',
                  '\n\n',
                  'If you are finished, type "quit" at prompt.\n')
            intro = False
        text_file = input('Name of File or Filepath (or quit): ')
        if text_file.lower() == 'quit':
            break
        elif text_file.lower() == 'help':
            intro = True    # Turn on intro message for next iteration
            continue
        text_file = fix_filename(text_file)
#        print(word_library(text_file))
#        print(trigram_build(text_file))
        print(create_new(text_file))
