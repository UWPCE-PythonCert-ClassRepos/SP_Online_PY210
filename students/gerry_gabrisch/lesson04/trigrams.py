#!/usr/bin/env python3
import random

def split_string(in_string):
    '''Takes a string and splits it by white spaces and returns a list...
    Input: String'''
    return in_string.split(' ')

def build_trigrams(word_list):
    '''Builds trigrams from a list of words
    Input: List of words'''
    trigrams = {}
    #Go through word_list list one item at a time...
    for item in range(len(word_list)-2):
        #Make the key a tuple  of the current word and the next word (keys must be immutable)...
        key_as_list = word_list[0:2]
        #Turn the key words from the list into a nice string...
        str_key = ' '.join(word[0:] for word in key_as_list)
        #For every two words make a list to hold the third words that follow...
        third_words =[]            
        third_word = (word_list[2])
        counter = 0
        for item in word_list:
            if word_list[counter] == key_as_list[0] and word_list[counter + 1] == key_as_list[1]:
                    third_words.append(word_list[counter + 2])
            counter += 1
        #If this key has already been added to the trigram then skip it...
        if str_key in trigrams:
            pass
        else:
            #Add the trigram to the trigrams dict...
            trigrams[str_key] = third_words        
        #Get rid of the first list item...
        '''maybe from a speed perspective it would be better to slice from the end???'''
        word_list = word_list[1:]
    return trigrams

if __name__=='__main__':
    in_string = 'I wish I may I wish I might'
    word_list = split_string(in_string)
   
    trigrams = build_trigrams(word_list)
    print(trigrams)  
    