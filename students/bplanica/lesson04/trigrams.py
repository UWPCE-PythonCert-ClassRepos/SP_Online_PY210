#!/usr/bin/env python3
import random

# ------------------------------ #
# Assignment 4 (Trigrams!) for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/18/2019, Created and tested script
# ------------------------------ #

# ----- Data ----- #
# ---------------- #
lst_words = [] # list to store words from txt file
lst_story = [] # list to store word sequences using trigrams
file_name = "./sherlock.txt" # text file to read/process

# ----- Processing ----- #
# ---------------------- #
def read_file(obj_file_name):
    """ reads text file and gathers all words within the story """
    try:
        obj_file = open(obj_file_name, "r") # open file as read only
    except:
        print("This program requires 'sherlock.txt' file.")
        raise SystemExit
    switch = False # detemines start of the story in Project Gutenberg texts
    for row in obj_file: # for each line in the text file...
        row = row.replace(",", "") # remove commas
        row = row.replace("(", "") # remove parenthesis
        row = row.replace(")", "") # remove parenthesis
        row = row.replace("--", " ") # remove double hyphens
        if switch == True:
            words = row.split() # split words by spaces
            for item in words:
                lst_words.append(item) # append each word to store all words from txt file
        if row[:41] == "*** START OF THIS PROJECT GUTENBERG EBOOK": # detmines start
            switch = True
        if row[:39] == "*** END OF THIS PROJECT GUTENBERG EBOOK": # determines the end
            switch = False
    return lst_words


def build_trigrams(words):
    """ build up the trigrams dict from the list of words """
    trigrams = {} # define/empty dictionary
    for i in range(len(words) - 2): # for all words in list except last 2
        pair = words[i], words[i + 1] # create a tuple from the pair
        follower = words[i + 2] # 
        trigrams.setdefault(pair, []) # create a key from a pair if not found alreay in existance
        trigrams[pair].append(follower) # append the follower to the list
    return trigrams


def build_story(dictionary):
    length =  len(dictionary) # find the length of the dictionary
    start = random.randint(0, length) # select a random location to start
    pair = list(dictionary.keys())[start] # find the first pair
    for item in pair:
        lst_story.append(item) # append to the story
    follower = random.choice(dictionary[pair])
    lst_story.append(follower)
    try:
        i = 1
        while i < 100: # do this 100 times (to keep the story shorter)
            follower = random.choice(dictionary[lst_story[-2], lst_story[-1]]) # find the new pair
            lst_story.append(follower) # append the follower to the story list
            i += 1
        return (lst_story)
    except:
        return (lst_story) # if there is an exception(pair/key not found), stop before 100


# ----- Presentation ----- #
# ------------------------ #
if __name__ == "__main__":
    lst_words = read_file(file_name) # gather the list of words
    trigrams = build_trigrams(lst_words) # build the dictionary
    #for key, value in trigrams.items():
    #    print(f"{key}, {value}")
    lst_story = build_story(trigrams) # build the story
    print(" ".join(lst_story)) # print the list/story with spaces in between words
