#!/usr/bin/env python3

'''
Objectives
Katas are about trying something many times. In this one, what we’re experimenting with is not just the code, but the heuristics of processing the text. What do we do with punctuation? Paragraphs? Do we have to implement backtracking if we chose a next word that turns out to be a dead end?

I’ll fire the signal and the fun will commence…
'''

#!/usr/bin/env python3
import random
import sys

#words = "I wish I may I wish I might".split()
filename = (r"C:\Users\cliff\SP_Online_PY210\students\clifford_butler\lesson04\sherlock.txt")

def read_in_data(filename):
    # read and clean the data to be used for the process
    lines = list()
    translate_chars = str.maketrans(',.?!;()', '       ')
    header = ('*** START OF THIS PROJECT GUTENBERG EBOOK')
    
    try:
        read_file = open(filename, 'r')
    except FileNotFoundError:
        print(filename, ': this file was not found.')
        sys.exit()
    
    
    # skip past the header of the file
    for line in read_file:
        if line.find(header) != -1:
            break

    # read until the end-of-book line is found
    for line in read_file:
        if line.isspace():
            continue
        elif line.find('End of the Project Gutenberg EBook') != -1:
            break
        else:
            line = line.translate(translate_chars)
            line = line.replace('"', '')
            line = line.replace('--', ' ')
            lines.append(line.lower())
    return lines

def make_words(in_data):
    words = list()
    for line in in_data:
        words.extend(line.split())

    return words

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    
    trigrams = {}
    for i in range(len(words) -2):
        pair = words[i:i + 2]
        follower = words[i + 2]
        trigrams.setdefault(tuple(pair),[]).append(follower)
    return trigrams
    
def build_text(trigrams):
    word_limit = int(input('Enter the desired number of words in the new text\
(minimum of 3)>'))
    #Pick the first random word pair from the dictionay
    first_pair = random.choice(list(trigrams))
    new_list = list(first_pair)
    new_list.append(random.choice(trigrams[first_pair]))
    #add a new word to the list using the last two words in the list as
    #word pairs
    count = 3
    while count < word_limit:
        if tuple(new_list[-2:]) in trigrams:
            new_list.append(random.choice(trigrams[tuple(new_list[-2:])]))
            count += 1
        elif count == word_limit-1:
            new_list.append(first_pair[0])
            count += 1
        elif count == word_limit-2:
            new_list.append(first_pair[0])
            new_list.append(first_pair[1])
            count += 2
        else:
            new_list.append(first_pair[0])
            new_list.append(first_pair[1])
            new_list.append(random.choice(trigrams[first_pair]))
            count += 3
    new_text = " ".join(new_list)
    return new_text 

if __name__ == "__main__":    
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)
    print(new_text)