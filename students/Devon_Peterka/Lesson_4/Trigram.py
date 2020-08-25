#!/usr/bin/env python3

import os
import random
import string

def fix_filename(text_file):
    '''
    Function to handle incorrect/incomplete file names from user.
    Specifically ones without .txt extension.  Simply adds it if not
    present.
    '''
    if text_file[-4:] != '.txt':
        text_file += '.txt'
    return text_file

def word_library(filename):
    '''
    Builds a big ol' list of every word in the file in the order in
    which they appear - all lowercase without punctuation.  Returns
    said list
    
    User is prompted to give a number on 'header' lines that will be
    ignored during reading.  I could have hardcoded this or had it
    search the Gutenberg "text starts here" line, but this would only
    work for Project Gutenberg files.  This way retains general
    applicability at the small expense of the user needing to briefly
    open the file to inspect.
    
    Function then reads file line by line, removing all punctuation
    (except for '.' as these are used to find proper nouns and "'" for
    contractions).  Then separated the lines into individual words.
    Proper nouns are found by comparing against a list of known proper
    nouns, which is itself populated with any word that does not follow
    a '.' (at end of prior word) and is title case.  This may mis some
    proper nouns, but will catch most of them.  If a period is present
    in the word, it is removed before being added to the words list.
    
    Function returns the words list for use by calling function
    '''
    words = []
    prop_noun = []

    header = int(input('How Many Lines is the File Header?'
                       ' (These lines will not be read): '))

    with open(text_file, 'r') as source:
        for ln, line in enumerate(source):
            intable = '!"#$%&\()*+,-/:;<=>?@[\\]^_`{|}~'
            outtable = ' ' * len(intable)
            trans_table = str.maketrans(intable, outtable)
            line = line.translate(trans_table)
            if ln >= header:
                for i,word in enumerate(line.split()):
                    if i > 0 and word.istitle() and line.split()[i-1][-1] != '.':
                        words.append(word.title())
                        if word not in prop_noun:
                            prop_noun.append(word.title())
                        continue
                    if word.title() in prop_noun and i == 0:
                        words.append(word.title())
                    else:
                        if word[-1] == '.':    # remove '.' here
                            words.append(word.lower()[:-1])
                        else:
                            words.append(word.lower())
    source.close()
    return words

def trigram_build(text_file):
    '''
    Builds the trigrams dictionary using a list of all the words in the
    text file, in order of appearance.  Takes first (2) words as a key,
    then the next as a value, then takes the 2nd and 3rd words as a key
    and 4th as value, and so-on...
    '''
    word_list = word_library(text_file)
    trigram = {}
    for i in range(len(word_list)-2):
        pair = tuple(word_list[i:i+2])
        nextword = word_list[i+2]
        trigram.setdefault(pair, []).append(nextword)
    return trigram
    
def create_new(text_file):
    '''
    Function creates new text from trigram dictionary.  First asks user
    how many trigrams should be used, then picks a key at random for
    the first and second words.  The function then enters a for loop to
    read the prior (2) words and use those as a key to find the next in
    the trigram dictionary.  If the prior (2) words don't exist as keys
    in the dictionary, a random key is selected.  All of the words are
    then joined with ' ' into a single run-on sentence.
    
    I opted not to re-introduce punctuation as doing so would likely be
    done randomly which would only make the readability improvement
    debatable at best.
    '''
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
        print(create_new(text_file))

