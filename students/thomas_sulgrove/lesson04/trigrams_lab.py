#!/usr/bin/env python3
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/kata_fourteen.html

import sys
import string
import random

#read in the data and trip off all unnessesary stuff
def read_in_data(source):
    with open(source, 'r') as infile:
        #build blank list
        story_list = []
        #boolean to read in line or not
        read = False
        for lines in infile:
            #if the 1st chapter, skip then start reading lines
            if lines =='I.\n':
                read = True
                continue
            #stop reading at the end of the book
            if 'End of the Project Gutenberg' in lines:
                read = False
            #if its a chapter title skip
            if lines.rstrip().lstrip().isupper():
                continue
            if read:
                #removes puncuation and splits it up into a list
                story_list.extend(lines.translate(lines.maketrans("","", string.punctuation)).split())
    return story_list

def build_trigram(words):
    #Build empty dict
    trigrams = {}
    #loop through the words, stopping 2 before the end
    for i in range(0, len(words) - 2):
        #phrases as a string
        #phrase = words[i] + " " + words[i + 1]
        #phrase as a tuple
        phrase = tuple(words[i:i+2])
        #word following the phrase (why we stop 2 before)
        following_word = words[i + 2]
        #check if phrase is in dict
        if phrase in trigrams:
            #append following word to the list
            trigrams[phrase].append(following_word)
        else:
            #add on key and following word to dict
            trigrams[phrase] = [following_word]

    return trigrams


def build_text(word_pairs):
    #generate a length to the senetence
    sentence_length = random.randint(3,15)
    #generate an intex to start from
    start_index = random.randint(0 , len(word_pairs))
    #find the first word pair
    word_pair = list(list(word_pairs.keys())[start_index])
    #start the list with that pair
    sentence = word_pair
    #keep going until it is the detmined length
    while len(sentence) <= sentence_length:
        #if it cant find a new pair, then stop this maddness
        try:
            #get list of all the possible next words
            next_words = word_pairs[tuple(word_pair)]
            #choose next one at random
            next_word_choice = next_words[random.randint(0, len(next_words)-1)]
            #add onto the list
            sentence.extend([next_word_choice])
            #set up next pair to search
            word_pair = sentence[-2:]
        except:
            break
    #join the sentence list together, capitalize, and add peroid.
    return " ".join(sentence).capitalize().replace(' i ', ' I ') + '.'

if __name__ == "__main__":
        # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    #filename = 'C:\\Users\\tsulgrov\\Documents\\Scripts\\School Work\\PY210\\lesson04\\sherlock.txt'
    
    words = read_in_data(filename)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)
