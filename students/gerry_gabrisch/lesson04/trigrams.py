#!/usr/bin/env python3
import random

def split_string(in_string):
    '''Takes a string and splits it by white spaces and returns a list...
    Input: String'''
    return in_string.split(' ')


def build_trigrams_dict(word_list):
    '''Builds trigrams from a list of words
    Input: List of words'''
    trigram_dict = {}
    third_words_list = []
    #Go through word_list list one item at a time...
    for i in range(len(word_list)-2):
        #Get the first two items and cast them to a tuple...
        pair = tuple(word_list[i:i + 2])
        #Get the third or following letter...
        follower = word_list[i + 2]
        #if this pair is already a key then this combination has been evaluated so pass...
        if pair not in trigram_dict.keys():
            #Build an new dictionary item
            new_dict_item = {pair: []}
            #add the new item to the dictionary
            trigram_dict.update(new_dict_item)
        #When this key turns up, add the follower...
        trigram_dict[pair].append(follower)
    return trigram_dict        


def get_random_dict_item(in_dict):
    '''builds the first three trigram words by randomly selecting a dict entry and randomly selecting a list item...'''
    #Get keys as a list so that you can choose a random key.  You cannot get a dict item my index...
    this_key = list(in_dict)[random.randint(0, len(in_dict)-1)]
    #Add these key items to the beginning of the list...
    return this_key


def add_to_trigram(in_dict, this_key, wacky_list): 
    '''adds three list items to the trigam words in a list...'''
    wacky_list.append(this_key[0])
    wacky_list.append(this_key[1])
    third_letter = random.choice(in_dict[this_key])
    wacky_list.append(third_letter)
    return wacky_list


def make_trigram(in_dict, trigram_lenth):
    '''Builds the actual trigram and returns it as a string...'''
    wacky_list = []
    #Pick a random starting point...
    random_key = get_random_dict_item(in_dict)
    #Add the first random key and random third letter to the list...
    wacky_list = add_to_trigram(in_dict, random_key, wacky_list)
    
    for i in range(trigram_length):
        new_key =(wacky_list[-2], wacky_list[-1])
        #This new key might not be a key in the dictionary, if so, forget about it an pick a randon key...
        while new_key not in in_dict.keys():
            new_key = get_random_dict_item(in_dict)
        wacky_list = add_to_trigram(in_dict, new_key, wacky_list)
    trigram_story = ' '.join(wacky_list)
    return trigram_story
       

if __name__=='__main__':
    in_string = 'When chickens are outlawed only outlaws will have chickens'
    #in_string = 'a chicken and a half layed an egg in a day and a half'
    
   #Some number to limit the size of the trigram...
    trigram_length = 21
    #the words come in threes (and always include a starting triplet so....
    trigram_length = int((trigram_length -3)/3)
    #Split the string by blank spaces...
    word_list = split_string(in_string)
    
    in_dict = build_trigrams_dict(word_list)

    print(make_trigram(in_dict, trigram_length))