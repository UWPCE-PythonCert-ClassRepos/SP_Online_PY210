#!/usr/bin/env python3
import sys
import random

def read_in_data(filename):
    '''Reads the lines of the file'''
    with open(filename, 'r') as f:
        read_lines = f.read()
    return read_lines

def make_words(in_data):
    '''Splits the file into a list of words and removes header and footer'''
    lst_data = in_data.split() #creates list of words

    if '***' in lst_data: #for cleaning Project Gutenberg texts
        header_stars_index = lst_data.index('***') #finds first instance of stars
        lst_header_start_remove = lst_data[header_stars_index+1::] #removes all words up to first instance of stars

        second_header_stars_index = lst_header_start_remove.index('***') #finds second instance of stars
        lst_header_final_remove = lst_header_start_remove[second_header_stars_index+1::] #removes rest of header

        footer_stars_index = lst_header_final_remove.index('***') #finds first instance of footer stars
        lst_final = lst_header_final_remove[:footer_stars_index] #final list created with footer removed
        return lst_final

    else: #for non-Project Gutenberg texts that don't require cleaning
        return lst_data

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    #considers every word in words list except last two
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2]) #determines tuple key
        follower = words[i + 2] #determines value to go with tuple key
        if pair not in trigrams:
            trigrams[pair] = [follower]
        else: #if value not already assoc with key, adds it to value list
            trigrams[pair].append(follower)
    return trigrams

def build_text(word_pairs):
    '''Creates new text from trigrams'''
    dictlist = []
    for key, value in word_pairs: #creates list of key pairs
        temp = [key, value]
        dictlist.append(temp)
    the_list_of_words = random.choice(dictlist) #chooses key pair at random
    while len(the_list_of_words) < 60:
        last_two_words = the_list_of_words[-2::] #finds last two words in word list
        if last_two_words == dictlist[-1]: #skips last pair of words
            break
        else:
            tup_last_two_words = (tuple(last_two_words)) #turns last two words into tuple
            next_word = random.choice(word_pairs[tup_last_two_words]) #looks up next word (value) in dictionary based on first two words tuple (key)
            more_words = the_list_of_words.append(next_word) #appends next word to list of gathered words
            final_text = " ".join(the_list_of_words) #joins the list of words to make string of words
    return final_text

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
    new_text = build_text(word_pairs)

    print(new_text)
