#!usr/bin/env python3
#Trigrams exercise created by Niels Skvarch

#import modules needed to run
import random
import sys
import os


#define global variables
#words = "I wish I may I wish I might".split()


#define functions
def read_in_data(filename):
    """takes in the file of text and creates a list of words removing punctuation"""
    in_data = list()
    translate_chars = str.maketrans({"," : " ", "." : " ", "?" : " ", "!" : " ", ";" : " ", "(" : " ", ")" : " "})
    with open(filename, 'r') as f:
        for line in f:
            if line.isspace():
                continue

            elif line.find('End of the Project Gutenberg EBook') != -1:
                break

            else:
                line = line.translate(translate_chars)
                line = line.replace('"', '')
                line = line.replace('--', ' ')
                in_data.append(line.lower())

    return in_data


def make_words(in_data):
    """go through the list of words and maintain capitals for the pronoun "I" """
    words = list()
    capitals = ['I', 'I\'m', 'I\'ll', 'I\'ve', 'I\'d']
    for line in in_data:
        words.extend(line.split())
    for indx, word in enumerate(words):
        if word.capitalize() in capitals:
            words[indx] = word.capitalize()
    return words


def build_trigram(words):
    """
    build up the trigrams dict from the list of words
    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    seed = words[0:2]

    for i in range(len(words)-2):
        wordpair = words[i:i+2]
        wordkey = tuple(wordpair)
        wordval = words[i+2]
        if wordkey not in trigrams.keys():
            trigrams[wordkey] = [wordval]
        else:
            trigrams[wordkey].append(wordval)
            
    return trigrams, seed


def build_text(trigrams, seed):
    """build a random text list from the trigrams dictionary"""
    new_text = seed[:]
    counter = 0
    while counter < 500:
        key_pair = new_text[counter : counter + 2]
        key_pair_tup = tuple(key_pair)

        if key_pair_tup not in trigrams:
            next_word = random.choice(new_text)

        else:
            next_word = random.choice(trigrams[key_pair_tup])
        new_text.append(next_word)
        counter += 1
    return new_text


def write_text(new_text):
    """join the text together in a string and return it to the main program"""
    text_string = ' '.join(new_text)
    return text_string


if __name__ == "__main__":
#using the main program given in the example
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    trigrams, seed = build_trigram(words)
    new_text = build_text(trigrams, seed)
    text_string = write_text(new_text)
    

    print(text_string)
