#!/usr/bin/env python3

'''
Objectives
Katas are about trying something many times. In this one, what we’re experimenting with is not just the code, but the heuristics of processing the text. What do we do with punctuation? Paragraphs? Do we have to implement backtracking if we chose a next word that turns out to be a dead end?

I’ll fire the signal and the fun will commence…
'''

#!/usr/bin/env python3
import random
import sys

words = "I wish I may I wish I might".split()

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

def read_in_data(filename):
    with open(filename) as file:
        in_data = file.readlines()
    return in_data
    
def make_words(in_data):
    in_words = []
    for line in in_data:
        #remove headers & footers
        if line[0:3] == '***':
            in_data.remove(line)
            
        else: in_data.extend(line.split())
    return in_words
    
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
    
    filename = r"C:\Users\cliff\SP_Online_PY210\students\clifford_butler\lesson04\sherlock.txt"
    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigrams(words)
    new_text = build_text(word_pairs)

    print(new_text)