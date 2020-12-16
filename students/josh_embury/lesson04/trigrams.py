#!/usr/bin/env python3
# ------------------------------------------------------------------------ #
# Title: Trigrams
# Description: Create text using trigrams

# ChangeLog (Who,When,What):
# JEmbury,12/13/2020,Created started script
# ------------------------------------------------------------------------ #

#--------------------------------------------#
# Text processing
#--------------------------------------------#
words = 'I wish I may I wish I might.'.split() # basic word list to start
def readText(str_filename):
    # this method reads a file and generates a list of words
    # input a filename as string
    # ouput a list of words
    pass
#--------------------------------------------#
# Trigram processing
#--------------------------------------------#
def buildTrigrams(lst_input_words):
    # desc: create a dict of trigrams
    # assumption: list must be len()>2
    # input: a list of words as string objects
    # output: dictionary with:
        # keys: str - all adjacent word pairs in input list
        # values: lst - all 'third' adjacent word to given key in input list
    dict_trigrams = {}
    for i in range(2,len(lst_input_words)):
        current_pair = lst_input_words[i-2] + ' ' + lst_input_words[i-1]
        dict_trigrams.setdefault(current_pair, []) # set it or get it
        dict_trigrams[current_pair].append(lst_input_words[i])
    return dict_trigrams

def buildSentence(dict):
    pass
    # pick random key from dict
    str_starter = 'I wish' # known key to test with
    lst_new_sentence = [str_starter]

    return str_newSentence
#-----------------------------------------------#
# Main
#-----------------------------------------------#
if __name__ == '__main__':
    print(buildTrigrams(words))
