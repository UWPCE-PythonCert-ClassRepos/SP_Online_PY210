#!/usr/bin/env python3

"""Produce a trigram using The Adventures of Sherlock Holmes.

"""
#testing the script using a small string to get the code correct
words = "I wish I may I wish I might".split()
more_words = "I am trying to come up with a longer string than words".split()

"""more_words should look like:

"I am" = 'trying'
'am trying' = 'to'
'trying to' = 'come'
'to come' = 'up'
'come up' = 'with'
'up with' = 'a'
'with a' = 'longer'
a longer = string
longer string = than
string than = words
"""

"""#create pairs of 2 adjacents words (will be tuples and keys) that return the next adjacent word/s (will be lists and values)
"I wish" = ["I", "I"]
"wish I" = ["may", "might"]
"I may" = ["I"]
"may I" = ["wish"]"""

"""example of how the dict should look:

trigrams = 
{("I wish"): ["I", "I"],
("wish I"): ["may", "might"],
("I may"): ["I"],
("may I"): ["wish"],}
"""

def build_trigrams(more_words):
    """Build up the trigrams dict from the list of words above.
    
    returns a dict of:
        keys: adjacent word pairs
        values: the word that immediately follows the last word of the key
    """
    trigrams = {}
    
    #build the dict
    for x in range(len(more_words) - 2):
        pair = tuple(more_words[x:x + 2]) # converts to tuple; will be the keys in trigrams
        follower = more_words[x + 2] # will be the values in trigrams

        #assigns pair and follower to trigrams as keys and values
        #if the pair is already in trigrams, follower is appended to that pair instead
        #update this to use defaultdict(list) instead
        if pair in trigrams:
            trigrams[pair].append(follower)
        else:
            trigrams[pair] = [follower]
    
    return trigrams

if __name__ == "__main__":
    trigrams = build_trigrams(more_words)
    print(trigrams)