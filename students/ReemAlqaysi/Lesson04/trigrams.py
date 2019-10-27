#!/usr/bin/env python3
import random


#words = "I wish I may I wish I might".split()


def build_trigram(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
        # build up the dict here!
    for i in range(len(words) - 2):
        # words pair
        pair = tuple(words[i:i + 2])
        # word after match for values
        follower = words[i + 2]
        # check if key is in dictionary and add it
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            # add list as value
            trigrams[pair] = [follower]

    return trigrams

def build_text(word_pairs):
    #Create a new string 
    temp_list = []
    #convert dictionary (word_pairs) to list type
    for key, value in word_pairs.items():
        temp_list.extend([key[0], key[1], value[0]])
    #create a list of rendom words pairs from word_pair list
    new_list = []
    for i in range (len(temp_list)-1):
        first = random.choice(temp_list)
        second = random.choice(temp_list)
        third = random.choice(temp_list)
        if [second, third] not in new_list:
            new_list.append(first)
            new_list.append(second)
            new_list.append(third)
            new_text = " ".join(new_list)
        else: 
            break
    return new_text


def write_txt(new_text):
    #Write the story into a new file.
    new_filename = input('What is the new file name?')
    with open(new_filename + '.txt', 'w') as f:
        f.write(' '.join(new_text))



def read_in_data(filename):

    #make alist of words from .txt file
    words = list()
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)

    return words


if __name__ == "__main__":

    # get the filename from the command line
    filename = input('What is the filename name? \nplease make sure that  the filename ends with .txt\n >> ')
    words = read_in_data(filename)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)