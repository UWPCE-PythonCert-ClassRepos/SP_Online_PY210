#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 12/1/2019
# trigrams.py

import random
import sys
import string

def read_in_data(filename):
    '''
    Reads input file in as text.
     Input:  String: filename
     Output: String: input text '''

    # Copies the text of the file
    with open(filename, 'r') as f:
        file_text = f.read()

    header = '*** START OF THIS PROJECT GUTENBERG EBOOK'
    footer = 'End of the Project Gutenberg'

    # Removes the header from the text
    if header in file_text:
        file_text = file_text.split(header)[1]

    # Removes the footer from the text
    if footer in file_text:
        file_text = file_text.split(footer)[0]
    return file_text

def make_words(in_data):
    '''
    Creates a list of the text with punctuations and capitals removed.
     Input:  String: text
     Output: List: text '''

    # Removes the dashes and replaces them with spaces
    in_data = in_data.replace('-', ' ')

    # Splits the word into a list of words
    word_group = in_data.split()

    word_list = []
    temp = None

    # Loops throught the list and removes the punctuation and capitals from each word
    for word in word_group:
        word = remove_chapter_title(word)
        word_list.append(remove_punctuations(remove_capitals(word, temp)))

        if word != '':
            temp = word
    return word_list

def build_trigrams(words):
    '''
    build up the trigrams dict from the list of words.
     Input:  List: words
     Output: Dictionary: 
        keys: word pairs
        values: list of followers '''

    trigrams = {}

    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]

        # Adds pair and follower to trigrams, if pair exists adds follower to the value list
        trigrams.setdefault(pair, []).append(follower)
    return trigrams

def build_text(word_pairs):
    '''
    Creates a sentence using trigrams dict from the list of words
     Input:  Dictionary: (pair : list)
     Output: String: trigram sentence '''
 
    # Initial key set to a random key from word_pairs
    key = random.choice(list(word_pairs.keys())) 

    # Adds the key to the word_list
    word_list = list(key)

    try:
        while True:

            # Limits the size of the sentence to 20 words
            if len(word_list) > 20:
                break
            else:
                new_word = word_pairs[tuple(key)] 

                # Randomly chooses a word if it is a list
                if type(new_word) == list:
                    new_word = random.choice(list(new_word))

                word_list.append(new_word) 
                word_string = ' '.join(word_list)

                # Creates the next key from the last two words
                key = word_list[-2:]

    finally:
        return (word_string[0].capitalize() + word_string[1:] + '.')

def remove_chapter_title(word_string):
    '''
    Removes chapter titles from the text. 
     Input:  String: word_string
     Output: String: word_string'''
     
    # If word_string is all upper followed by a period, set the word to ''
    if word_string.isupper() and word_string != 'I':
        word_string.replace(word_string, '')
    return word_string

def remove_punctuations(word_string):
    '''
    Removes punctuation from the beginning and end of the word. 
     Input:  String: word_string
     Output: String: '''

    for i in range(len(word_string)):

        # Removes punctuation from the front of the word
        if word_string[0:1] in string.punctuation:
            word_string = word_string[1:]

        # Removes puctuation from the back-end of the word
        elif word_string[-1:] in string.punctuation:
            word_string = word_string[:-1]

    # If 'i', set to upper
    if word_string == 'i':
        word_string = word_string.upper()
    return word_string

def remove_capitals(current_word, prev_word):
    '''
    Removes capitalization from the first word of a sentence. 
    - If first word of the sentence is not I, the capitalization is removed. 
    - Proper names at the beginning of a sentence will be set to lower case.
     Input:  String: current word, String: previous word or None
     Output: String: lower case '''
    
    # Sets the first word of each sentence to lower if not 'I' 
    if current_word != 'I' and (prev_word == None or prev_word[-1] == '.' or current_word.isupper()):
        return current_word.lower()
    else:
        return current_word

if __name__ == "__main__":
    '''
    Main
     Input:  String: filename
     Output: Display: trigram text '''

    # Get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)