#!/usr/bin/env python3
import random

"""Produce a trigram using The Adventures of Sherlock Holmes.

"""
#testing the script using a small string to get the code correct
words = "I wish I may I wish I might".split()
file_path = "./Lesson04/sherlock_small.txt"

#test that a longer string works
more_words = "I believe I am that I believe I can be who I believe".split()

"""example of how the dict should look:

trigrams = 
{("I wish"): ["I", "I"],
("wish I"): ["may", "might"],
("I may"): ["I"],
("may I"): ["wish"],}

Examples of generated text to expect if using words as the original text:
[I wish I may I wish I might]
[I wish I might]
[I wish I may I wish I may I wish I might] #and so on...
"""
trigrams = {}

def build_trigrams(words):
    """Build up the trigrams dict from a given string.
    
    returns a dict of:
        keys: adjacent word pairs
        values: the word that immediately follows the last word of the key
    """
    for x in range(len(words) - 2):
        pair = tuple(words[x:x + 2]) # will be the keys in trigrams. try frozen sets instead of tuples
        follower = words[x + 2] # will be the values in trigrams

        #try to update this to use defaultdict(list) instead
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]

    return trigrams

def generator(trigrams):
    """Creates a random "sentence" using trigrams."""
    
    #determine first word pair randomly
    new_text = [word for word in random.choice(list(trigrams.keys()))]

    while tuple(new_text[-2:]) in trigrams:
        if len(new_text) > (len(words) * 2):
            break
        else:
            new_text.append(random.choice(trigrams[tuple(new_text[-2:])]))
    
    new_text[0].upper()
    
    new_string = " ".join(new_text)
    
    print(f"{new_string}.")
    
    return trigrams

def build_words(file_path):
    file_string = ""
    
    try:
        with open(file_path, 'r') as f:
            file_string = f.read()
            words = file_string.split()
    except OSError:
        print("File path invalid, using more words.")
        words = more_words
        
    return words

def main():
    file_path
    build_words(file_path)
    build_trigrams(words)
    generator(trigrams)


if __name__ == "__main__":
    main()
