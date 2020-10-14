#!/usr/bin/env python3

#+------------------------------------+
#| Trigrams (Assignment 3) - Lesson 4 |
#+------------------------------------+

import os.path, string, random, sys


current_dir = os.getcwd()
# retrieve default working directory just in case to point to read_in .txt files

text = 'I wish I may I wish I might'
words = text.split()

ltext = 'Those following words look a lot like they are in a list, yes? Perfect, the list structure keeps order, and you can keep adding (appending) new words to it. Each of those lists of words needs to be mapped to a particular pair. Each pair is unique; it only shows up once (when that same pair is encountered again in the text, you add the follower to the list). That sounds a lot like a dictionary. The keys (word pairs) are unique, and map to a list of following words. (Note that, technically, in python the dictionary is only one implementation of a Mapping.)'


def read_in_data(filename="sherlock_small.txt", skip = 0):
    tfile = open(filename,'r')
    text = '' # initiate
    for i, line in enumerate(tfile):
        if i >= skip : # skip header
            text_line = line.strip() + " " # strip newlines and add trailing space
            text += text_line
    return(text)


def make_words(in_data): #in_data is a string with newlines replaced by whitespace
    cleanstr = in_data.strip() # remove newlines and extra whitespace if any
    cleanstrp = cleanstr.translate(str.maketrans('', '', string.punctuation)) # remove punctuation 
    lwords = cleanstrp.split() # list of words with the order preserved
    return(lwords)    
    

# start building here
def build_text(word_pairs):
    # random.choice(a_list) to randomly select a value in a list 
    ntext = random.choice(list(word_pairs)) # init generated text
    idx = ntext
    ntext_lst = ntext.split() # new text as a list of words
    
    # add in some literal limiting factor so program doesnt hang/crash for long input text file
    limiter = 110000
    cnt = 0
    while idx in word_pairs:
        next_list = word_pairs[idx]
        next_word = random.choice(next_list)
        ntext_lst.append(next_word) # add new value word to the list of new text words
        idx = " ".join(ntext_lst[-2:]) # update index
        # keeping track of words total to compare against the limiting factor
        cnt += 1
        # when word count exceeds limiting factor break out of building loop
        if cnt > limiter:
            break
        
    ntext = " ".join(ntext_lst) # simple word list converter to text
    return(ntext)
# end build_text


# build dictionary data structure from wordstream
def build_trigrams(words):  
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    tridict = {} # init empty dict
    for idx, word in enumerate(words[:-2]):
        key = word + " " + words[idx+1]
        val = words[idx+2]
        if key in tridict:
            tridict[key].append(val) # update existing key
        else:    
            tridict[key] = [val] # add new key
    return(tridict)
    

if __name__ == "__main__":
    os.chdir(current_dir) # to be safe and ensure that in the same dir as read in text files
    
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)
    
    # provide specific header skip for long version and omit any superflous details, e.g. chapter index etc.
    if filename == "sherlock.txt":
        in_data = read_in_data(filename,61)
    else:
        in_data = read_in_data(filename)
        
    print()
    print("Reading in data from file:", filename, "\n")
    print("Located in directory:", current_dir, "\n")
    
    words = make_words(in_data)
    print("Making words...\n")
    print("Total words length:",len(words),"\n")
    
    word_pairs = build_trigrams(words)
    print("Building trigrams based on word pairs...\n")
    
    new_text = build_text(word_pairs)
    print("Printing generated text...\n")
    print(new_text)
    print()
    print("-------End of Generated Text-------\n")
    
